from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from agents.rag_memory import vectorstore

loader = DirectoryLoader("../docs")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

vectorstore.add_documents(chunks)

print("Documents indexed.")
