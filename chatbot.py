from langchain_community.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv("/home/akrizik/chatbot/.env")

def setup_vectorstore():
    loader = UnstructuredFileLoader("my_documents/AK Raw Text.txt")
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)
    embedding = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embedding)
    vectorstore.save_local("vectorstore")

def get_qa_bot():
    embedding = OpenAIEmbeddings()
    vectorstore_path = "/home/akrizik/chatbot/vectorstore"
    vectorstore = FAISS.load_local(vectorstore_path, embedding, allow_dangerous_deserialization=True)
    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model="gpt-4o-mini"),
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    return qa