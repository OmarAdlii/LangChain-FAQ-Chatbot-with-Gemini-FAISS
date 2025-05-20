
# LangChain FAQ Chatbot with Gemini + FAISS

This project is a **Streamlit-based FAQ assistant** powered by **LangChain**, **Google's Gemini LLM**, and **FAISS vector search**. It allows users to query a dataset (`codebasics_faqs.csv`) using natural language and get accurate responses grounded in the source data.

---

## 🧠 Features

- 🔍 Context-aware question answering using `RetrievalQA`
- 🤖 LLM backend powered by **Gemini 2.0 Flash** via `langchain_google_genai`
- 🧾 Semantic search using **FAISS** and **HuggingFace Embeddings**
- 📄 Document ingestion from a CSV source
- 💡 Streamlit frontend for interactive chat
- 🔐 API key handling via `.env`

---

## 🗂️ Project Structure

.env # Stores the Google API key

base.py # LangChain setup: LLM, embeddings, vector store, and QA chain

main.py # Streamlit app for user interaction

test_notebook.ipynb # Jupyter notebook to test the core functionality

requirements.txt # Python dependencies



