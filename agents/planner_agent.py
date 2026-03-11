from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral")

def plan_task(goal: str) -> str:
    prompt = f"""
You are a planning AI.

Break the following goal into numbered steps.

Goal:
{goal}
"""
    return llm.invoke(prompt)
