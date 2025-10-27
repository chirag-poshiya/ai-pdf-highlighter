# AI PDF Highlighter

An intelligent PDF highlighting application that uses AI to automatically identify and highlight the most important sentences in a PDF document based on your desired reading time.

## 🌟 Features

- **AI-Powered Highlighting**: Uses OpenAI's GPT-4o-mini model to intelligently extract key information
- **Customizable Reading Time**: Set your preferred reading time (in minutes) to get highlights tailored to your schedule
- **User-Friendly Interface**: Clean and intuitive web interface built with Next.js
- **Automatic Processing**: Upload a PDF, set your reading time, and get a highlighted PDF instantly
- **Smart Token Management**: Automatically calculates token limits based on reading time for optimal content extraction

## 🚀 Getting Started

### Prerequisites

- Python 3.8+ (for backend)
- Node.js 18+ (required for running Next.js)
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/chirag-poshiya/ai-pdf-highlighter.git
   cd ai-pdf-highlighter
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   
   # Activate virtual environment
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Frontend Setup**
   ```bash
   cd ../frontend
   npm install
   ```

4. **Environment Configuration**
   
   Create a `.env` file in the `backend` directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

### Running the Application

1. **Start the backend server**
   ```bash
   cd backend
   # Make sure your virtual environment is activated
   uvicorn app.main:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`

2. **Start the frontend development server** (in a new terminal)
   ```bash
   cd frontend
   npm run dev
   ```
   The application will be available at `http://localhost:3000`

## 💻 Usage

1. Open your browser and navigate to `http://localhost:3000`
2. Click "Choose File" and select a PDF document
3. Enter your desired reading time in minutes (e.g., 5, 10, 15)
4. Click "Highlight" to process your PDF
5. Wait for the processing to complete
6. Download your highlighted PDF

## 🏗️ Project Structure

```
ai-pdf-highlighter/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI application
│   │   └── utils/
│   │       └── pdf_utils.py     # PDF processing utilities
│   ├── outputs/                 # Generated highlighted PDFs
│   ├── uploads/                 # Temporary uploads
│   ├── venv/                    # Virtual environment
│   ├── requirements.txt         # Python dependencies
│   └── .env                     # Environment variables
├── frontend/
│   ├── src/
│   │   └── app/
│   │       ├── page.tsx         # Main UI component
│   │       ├── layout.tsx       # App layout
│   │       └── globals.css      # Global styles
│   ├── package.json             # Node dependencies
│   └── README.md                # Frontend README
└── README.md                     # This file
```

## 🔧 Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **PyMuPDF** - PDF processing and manipulation
- **OpenAI API** - AI-powered text analysis
- **Uvicorn** - ASGI server
- **Python-dotenv** - Environment variable management

### Frontend
- **Next.js 16** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **React 19** - UI library

## 📝 API Endpoints

### `POST /highlight`
Processes a PDF and returns a highlighted version.

**Parameters:**
- `file`: PDF file (multipart/form-data)
- `reading_time`: Integer representing desired reading time in minutes

**Response:**
```json
{
  "file_url": "http://127.0.0.1:8000/outputs/highlighted_filename.pdf"
}
```

### `GET /health`
Health check endpoint.

**Response:**
```json
{
  "status": "ok"
}
```

## 🧪 How It Works

1. **PDF Extraction**: The backend uses PyMuPDF to extract text from each page of the uploaded PDF
2. **AI Analysis**: The extracted text is sent to OpenAI's GPT-4o-mini model with instructions to:
   - Select the most important sentences
   - Consider the user's specified reading time (approximately 350 tokens per minute)
   - Return the highlights in JSON format
3. **Highlighting**: The identified sentences are automatically highlighted in the original PDF using annotation features
4. **Delivery**: The highlighted PDF is saved and made available for download

## 🔒 Environment Variables

Create a `.env` file in the `backend` directory with the following:

```env
OPENAI_API_KEY=your_api_key_here
```

You can obtain an API key from [OpenAI's website](https://platform.openai.com/api-keys).

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⚠️ Limitations

- Currently processes up to 8000 characters of text to manage API costs
- Requires an active internet connection for AI processing
- Best results with well-structured PDFs containing readable text (not scanned images)

## 🐛 Troubleshooting

**Issue**: "Server error: 500"
- **Solution**: Make sure your `.env` file contains a valid OpenAI API key

**Issue**: PDF not highlighting properly
- **Solution**: Ensure your PDF contains selectable text (not scanned images)

**Issue**: Frontend can't connect to backend
- **Solution**: Verify both servers are running and backend is on port 8000

## 📧 Contact

For questions or issues, please open an issue on GitHub.

---

Made with ❤️ using FastAPI, Next.js, and OpenAI
