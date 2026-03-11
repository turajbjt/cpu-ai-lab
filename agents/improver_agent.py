from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral")

def improve(feedback: str) -> str:
    prompt = f"""
You are an AI improvement system.

Feedback:
{feedback}

Extract actionable lessons that future agents should follow.
"""
    return llm.invoke(prompt)
