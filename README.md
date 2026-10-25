# NoteGenius AI

**Your Personal AI Study Assistant**

NoteGenius AI is an AI-powered study assistant that transforms lengthy study notes into clear, concise, and easy-to-understand summaries using Google's Gemini API.

##  Features

-  Summarizes long study notes into simple language.
-  Uses Google's Gemini AI for text summarization.
-  Organizes summaries with headings and bullet points.
-  Simple and user-friendly interface.
-  Uses environment variables to keep API credentials out of the source code.

##  Tech Stack

- **Python** — Core programming language
- **Streamlit** — Web application interface
- **Google Gemini API** — AI-powered summarization
- **python-dotenv** — Environment variable management

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/jagriti777795-hub/NoteGenius-AI.git
cd NoteGenius-AI
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Your API Key

Create a `.env` file in the project folder and add your own Gemini API key:

```text
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own API key. Never upload your `.env` file to GitHub.

### 5. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

##  How to Use

1. Open NoteGenius AI.
2. Paste your study notes into the text area.
3. Click **Summarize Notes**.
4. Read the AI-generated summary.

##  Future Improvements

- PDF upload and summarization
- Download summaries as text files
- Multiple summary styles
- Key points and important-question generation
- Improved user interface

##  Author

**Jagriti Dubey**

GitHub: [jagriti777795-hub](https://github.com/jagriti777795-hub)

---

 If you find this project useful, consider giving the repository a star!