# DataPro – AI SaaS Customer Support Chatbot

Flask + Groq (LLaMA 3.1) 

---

## 📁 Structure
```
datapro/
├── app.py
├── .env
├── requirements.txt
└── templates/
    ├── dashboard.html
    └── chat.html
```

---

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install flask groq python-dotenv

# 2. Create .env file
echo "GROQ_API_KEY=your_key_here" > .env

# 3. Run
python app.py
```

Get your free API key → https://console.groq.com

Open → http://localhost:5000

---

## 🔗 Routes

| Route | Description |
|-------|-------------|
| `/` | Landing page |
| `/chatbot` | Chat UI |
| `/chat` (POST) | AI chat API |

---

## ⚠️ Notes

- Add `.env` and `venv/` to `.gitignore` — never commit your API key
- Chat history resets on server restart (in-memory only)
- Model: `llama-3.1-8b-instant` via Groq, keeps last 6 messages for context
