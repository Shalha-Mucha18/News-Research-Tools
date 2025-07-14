# 📚 News & Research QA Assistant

A Streamlit-powered app that allows users to extract insights from online articles and academic PDFs using Google Gemini, LangChain, and FAISS vector search.

> 💡 Paste URLs or upload PDFs → Generate embeddings → Ask questions → Get AI-powered answers with sources.

---

## 🚀 Features

- 🔗 Load content from **article URLs**
- 📄 Upload and process **PDF research papers**
- 🧠 Build semantic **vector indexes** using `FAISS`
- 🤖 Ask questions using **Google Gemini Pro**
- 📌 Get answers with **source document context**
- 💾 Optional: Append new documents to the existing vectorstore

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|---------|
| [Streamlit](https://streamlit.io/) | Web UI |
| [LangChain](https://python.langchain.com/) | Document QA pipeline |
| [Google Gemini (via `langchain-google-genai`)](https://github.com/langchain-ai/langchain-google-genai) | LLM for answering questions |
| [FAISS](https://github.com/facebookresearch/faiss) | Vector search |
| [Hugging Face Transformers](https://huggingface.co/) | Text embeddings (`all-MiniLM-L6-v2`) |
| [Unstructured](https://github.com/Unstructured-IO/unstructured) | URL content extraction |
| [PyMuPDF](https://pymupdf.readthedocs.io/) | PDF loading |
| `dotenv`, `validators`, `pickle` | Utilities |

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/news-research-qa.git
cd news-research-qa
```

### 2. Install Dependencies
Ensure Python 3.8+ is installed. Then:
```bash
pip install -r requirements.txt
```
### 3. Configure Environment Variables
```bash
GEMINI_API_KEY=your_gemini_api_key_here
```
### 4.  Run the App
```bash
streamlit run app.py
```
## 📸 Demo


