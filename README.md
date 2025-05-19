# LangChain-FAQ-Chatbot-with-Gemini-FAISS
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

├── .env # Stores the Google API key
├── base.py # LangChain setup: LLM, embeddings, vector store, and QA chain
├── main.py # Streamlit app for user interaction
├── test_notebook.ipynb # Jupyter notebook to test the core functionality
├── requirements.txt # Python dependencies

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/OmarAdlii/langchain-faq-chatbot.git
cd langchain-faq-chatbot

2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Setup your .env file
Create a .env file in the project root and add your API key:

ini
Copy
Edit
GOOGLE_API_KEY=your_google_genai_api_key_here
🔑 You can get your API key from MakerSuite.

4. Prepare the vector database
Run the following to create your FAISS index from the CSV:

bash
Copy
Edit
python base.py
5. Run the Streamlit app
bash
Copy
Edit
streamlit run main.py
🧪 Testing in Jupyter
Use test_notebook.ipynb to experiment with the retrieval pipeline interactively.

📦 Requirements
Main libraries used:

langchain

langchain_google_genai

huggingface_hub

faiss-cpu

python-dotenv

streamlit

See requirements.txt for the full list.

📝 Notes
The CSV file codebasics_faqs.csv must contain a prompt column with questions and a corresponding response column with answers.

Responses are constrained to existing content — hallucination is discouraged by prompt design.

🤝 Acknowledgments
LangChain

Google Generative AI

Hugging Face

Codebasics Dataset

📬 Contact
Created by Omar Adli — feel free to connect or open an issue for feedback!

yaml
Copy
Edit

---

Let me know if you want to include a screenshot of the app, add a demo video, or use GitHub badges (e.g., stars, forks, license).







