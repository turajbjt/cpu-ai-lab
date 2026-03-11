from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral")

def critique(goal: str, output: str) -> str:
    prompt = f"""
You are an AI critic.

Goal:
{goal}

Output:
{output}

Evaluate:
1. correctness
2. quality
3. improvements

Return feedback.
"""
    return llm.invoke(prompt)
