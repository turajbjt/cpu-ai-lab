from langchain_community.llms import Ollama
from langchain.agents import initialize_agent, Tool
from langchain.memory import ConversationBufferMemory

from tools import run_python

llm = Ollama(model="mistral")

memory = ConversationBufferMemory()

tools = [

    Tool(
        name="Python",
        func=run_python,
        description="Run python code"
    )

]

agent = initialize_agent(
    tools,
    llm,
    memory=memory,
    verbose=True
)

while True:

    prompt = input("You: ")

    response = agent.run(prompt)

    print("Agent:", response)
