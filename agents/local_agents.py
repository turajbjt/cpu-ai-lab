#!/usr/bin/python3

# NEEDS: pip install langchain langchain-community qdrant-client ollama tiktoken flask

from langchain_community.llms import Ollama
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory

llm = Ollama(model="mistral")

memory = ConversationBufferMemory()

def search_docs(query):
    return f"Searching internal docs for: {query}"

tools = [
    Tool(
        name="Document Search",
        func=search_docs,
        description="Search internal knowledge"
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

while True:
    prompt = input("You: ")
    response = agent.run(prompt)
    print("Agent:", response)

