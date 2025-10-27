from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import fitz, os, tempfile, json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

# ✅ CORS configuration - allow all localhost origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Serve output files publicly
if not os.path.exists("outputs"):
    os.makedirs("outputs")

app.mount("/outputs", StaticFiles(directory="outputs"), name="outputs")


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/highlight")
async def highlight_pdf(file: UploadFile, reading_time: int = Form(...)):
    try:
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        tmp.write(await file.read())
        tmp.close()

        doc = fitz.open(tmp.name)
        text = ""
        for page in doc:
            text += page.get_text("text") + "\n"

        token_limit = reading_time * 350

        prompt = f"""
        From the following text, select the most important sentences that together
        can be read in about {reading_time} minutes (~{token_limit} tokens).
        Return JSON: [{{"sentence": "..."}}, ...]
        Text: {text[:8000]}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )

        content = response.choices[0].message.content.strip()
        try:
            highlights = json.loads(content)
        except:
            import re
            json_str = re.search(r'\[.*\]', content, re.S)
            highlights = json.loads(json_str.group()) if json_str else []

        for page in doc:
            for h in highlights:
                for area in page.search_for(h["sentence"]):
                    page.add_highlight_annot(area)

        output_path = f"outputs/highlighted_{file.filename}"
        doc.save(output_path)
        doc.close()

        return {"file_url": f"http://127.0.0.1:8000/{output_path}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
