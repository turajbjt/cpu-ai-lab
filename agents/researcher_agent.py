from .rag_memory import vectorstore

def research(query: str) -> str:
    docs = vectorstore.similarity_search(query)
    return "\n".join([d.page_content for d in docs])
