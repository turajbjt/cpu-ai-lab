from qdrant_client import QdrantClient
from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings import OllamaEmbeddings

client = QdrantClient("localhost", port=6333)

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectorstore = Qdrant(
    client,
    collection_name="documents",
    embeddings=embeddings
)
