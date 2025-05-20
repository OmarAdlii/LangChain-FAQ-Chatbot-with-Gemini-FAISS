import os
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import GoogleGenerativeAI 
llm=GoogleGenerativeAI(google_api_key=os.environ['GOOGLE_API_KEY'],temperature=0.9, model="gemini-2.0-flash")
from langchain.document_loaders.csv_loader import CSVLoader

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
embeddings=HuggingFaceEmbeddings()

vectordb_file_path='faiss_index'
def create_vector_db():
	loader=CSVLoader(file_path='codebasics_faqs.csv',source_column='prompt', encoding='latin-1')
	data=loader.load()
	vectorDB=FAISS.from_documents(documents=data,embedding=embeddings) 
	vectorDB.save_local(vectordb_file_path)
def get_qa_chain():
	vectorDB=FAISS.load_local(vectordb_file_path,embeddings)
	retriever=vectorDB.as_retriever(score_threshold=0.7)
	prompt_template = """Given the following context and a question, generate an answer based on this context only.
In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

CONTEXT: {context}

QUESTION: {question}"""
	PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
	chain_type_kwargs = {"prompt": PROMPT}
	chain = RetrievalQA.from_chain_type(llm=llm,
                            chain_type="stuff",
                            retriever=retriever,
                            input_key="query",
                            return_source_documents=True,
                            chain_type_kwargs=chain_type_kwargs)
	return chain
if __name__=="__main__":
    create_vector_db()
    chain = get_qa_chain()
    print(chain("Do you have javascript course?"))