# News & Research QA Assistant

**News & Research QA Assistant** is an AI-powered web application that empowers users to effortlessly extract insights, summaries, and answers from long-form articles and academic documents using natural language questions.

Instead of spending time manually reading and scanning through lengthy texts, users can:

- **Paste URLs of news articles or blog posts** to analyze key points, arguments, and perspectives
- **Upload academic PDFs**, such as research papers or reports, to explore methodologies, results, or conclusions
- **Ask specific questions** in plain English ,like *"What is the author’s main argument?"* or *"What methods were used in the study?"*
- **Receive instant, AI-generated answers** that are contextually accurate and based on the actual content of the uploaded documents
- **View source snippets** to verify facts, trace statements, or explore further

This assistant is ideal for students, researchers, journalists, analysts, and even casual readers who want to quickly understand complex content without reading every word. By combining the power of semantic search with generative AI, it transforms passive reading into an interactive and intelligent experience.

Whether you're preparing for an exam, writing a report, fact-checking a claim, or just trying to understand a dense article, this tool saves time, enhances comprehension, and keeps you focused on insights that matter.


---

##  Features

- Load content from **article URLs**
- Upload and process **PDF research papers**
- Build semantic **vector indexes** using `FAISS`
- Ask questions using **Google Gemini Pro**
- Get answers with **source document context**
- Optional: Append new documents to the existing vectorstore

---

## 🛠Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Shalha-Mucha18/News-Research-Tools.git
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
## 🧑‍💻 Usage Guide

1. Go to the **sidebar** and:
   - Paste up to **2 URLs** of articles  
   - **Or** upload a **PDF research paper**  
   - Click **"Build Index"** to generate embeddings

2. Ask a question in the main input field.

3. View the AI-generated answer and document sources.


## 📸 Demo

<img width="1907" height="813" alt="R A" src="https://github.com/user-attachments/assets/30f91a13-1076-44bf-bfae-03b65e3bc379" />





