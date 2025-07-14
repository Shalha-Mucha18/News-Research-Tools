import os
import streamlit as st
import pickle
import validators
from dotenv import load_dotenv

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import UnstructuredURLLoader, PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Constants
EMBEDDING_MODEL = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
LLM_MODEL = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=GEMINI_API_KEY)
VECTORSTORE_PATH = "vectorstore.pkl"
TEMP_PDF_PATH = "temp.pdf"

# Page setup
st.set_page_config(page_title="News & Paper Assistant", layout="wide")
st.title("News & Research QA")
st.sidebar.subheader("Paste article or PDF URLs ▸ build embeddings ▸ ask questions ▸ get sources.")

# Input: URLs
urls = []
for i in range(2):
    url = st.sidebar.text_input(f"URL {i+1}")
    if url and not validators.url(url):
        st.sidebar.warning(f"Invalid URL: {url}")
    elif validators.url(url):
        urls.append(url)

# Input: PDF
uploaded_pdf = st.sidebar.file_uploader("Upload PDF", type=["pdf"])
append_mode = st.sidebar.checkbox("Append to existing index", value=False)
build_index = st.sidebar.button("Build / Update Index")

# Helper: Build or update vectorstore
def build_vectorstore(docs, append=False):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    if append and os.path.exists(VECTORSTORE_PATH):
        with open(VECTORSTORE_PATH, "rb") as f:
            vs = pickle.load(f)
        vs.add_documents(chunks)
    else:
        vs = FAISS.from_documents(chunks, EMBEDDING_MODEL)

    with open(VECTORSTORE_PATH, "wb") as f:
        pickle.dump(vs, f)

    return vs

# Load documents
docs_loaded = []

if build_index:
    with st.spinner("Loading content & building vector index..."):
        try:
            if urls:
                loader = UnstructuredURLLoader(urls=urls)
                loaded = loader.load()
                if not loaded:
                    st.warning("No content could be loaded from the provided URLs.")
                docs_loaded.extend(loaded)

            if uploaded_pdf:
                with open(TEMP_PDF_PATH, "wb") as f:
                    f.write(uploaded_pdf.read())
                pdf_loader = PyMuPDFLoader(TEMP_PDF_PATH)
                docs_loaded.extend(pdf_loader.load())
                os.remove(TEMP_PDF_PATH)

            if docs_loaded:
                build_vectorstore(docs_loaded, append=append_mode)
                st.success("Index built successfully! You can now ask questions.")
            else:
                st.warning("No valid content found. Please check your inputs.")

        except Exception as e:
            st.error(f"Error during indexing: {e}")

# QA Chain Setup
def get_qa_chain(vs):
    return RetrievalQA.from_chain_type(
        llm=LLM_MODEL,
        chain_type="stuff",
        retriever=vs.as_retriever(),
        return_source_documents=True
    )

# Input: Query
st.divider()
query = st.text_input("Ask a question about the loaded content…")

if query:
    if not os.path.exists(VECTORSTORE_PATH):
        st.error("Please build the index first (from the sidebar).")
    else:
        with open(VECTORSTORE_PATH, "rb") as f:
            vectorstore = pickle.load(f)

        qa = get_qa_chain(vectorstore)

        with st.spinner("Thinking..."):
            result = qa(query)

        # Display Answer
        st.markdown("### Answer")
        st.write(result["result"])

        # Display Source Documents
        if result.get("source_documents"):
            st.markdown("#### 📚 Sources")
            for i, doc in enumerate(result["source_documents"], 1):
                src = doc.metadata.get("source", "Unknown source")
                st.markdown(f"**Source {i}:** {src}")
                st.write(doc.page_content[:300] + "...")
