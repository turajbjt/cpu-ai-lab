from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="codellama")

def write_code(task: str) -> str:
    prompt = f"""
You are a code-generation AI.

Write Python code for the following task:

{task}
"""
    return llm.invoke(prompt)
