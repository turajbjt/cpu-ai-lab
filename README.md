# CPU AI Lab

A fully containerized, CPU-friendly **multi-agent AI lab** with Ollama LLMs, vector memory, and browser-based goal submission.

---

## Overview

The CPU AI Lab allows you to:

- Run **multi-agent AI workflows** (Planner → Researcher → Coder → Executor → Critic → Improver → Memory).  
- Use **Ollama LLMs** (`phi3`, `mistral:Q4_K_M`, `codellama`, `nomic-embed-text`) on CPU.  
- Store persistent lessons in `learning/lessons.json`.  
- Automate workflows with **Flowise** and **n8n**.  
- Submit goals via a **browser UI** or HTTP API.  
- Fully containerized with **Docker Compose** — zero-touch startup.

---

## Features

| Feature | Description |
|---------|-------------|
| Multi-Agent API | Flask HTTP API (`/api/goal`) |
| Browser UI | Submit goals and view results (`http://localhost:3005`) |
| Ollama CPU Models | `phi3`, `mistral`, `codellama`, `nomic-embed-text` |
| Persistent Learning | Lessons stored in `learning/lessons.json` |
| Vector Memory | Qdrant vector database |
| Automation | Flowise + n8n |
| Containerized | All services run in Docker |

---

## Folder Structure

1️⃣ start_lab.sh

Pulls Ollama image and CPU models.

Creates learning/lessons.json.

Builds and starts all Docker containers.

2️⃣ requirements.txt

Includes Flask, langchain, langchain-ollama, Ollama client, Qdrant client, and other Python dependencies.

3️⃣ run_agents.py

Starts Flask multi-agent API (/api/goal).

4️⃣ docker-compose.yml

Core services: Ollama, Qdrant, n8n, Flowise, Open WebUI.

5️⃣ docker-compose.override.yml

Multi-agent API container (agents) + Web UI.

Only mounts directories (agents/, learning/) to avoid Docker mount errors.

6️⃣ agents/

Contains all agent Python code: Planner, Researcher, Coder, Executor, Critic, Improver, Memory, and helper tools (tools.py, rag_memory.py).

7️⃣ webui/

Simple browser UI with index.html, script.js, and Dockerfile.

8️⃣ learning/

Stores lessons.json (ignored by Git) for persistent learning.

9️⃣ ingestion/

Optional document ingestion scripts for vector memory.

---

## Prerequisites

- Docker ≥ 20.10  
- Docker Compose ≥ 2.0  
- CPU-only machine (no GPU required)  
- Optional: Python 3.14 for local testing

---

## Installation / Startup

1. Make the startup script executable:

```bash
chmod +x start_lab.sh
    2. Run the script:
./start_lab.sh
What it does:
    • Pulls Ollama Docker image
    • Pulls CPU-friendly Ollama models
    • Creates learning/lessons.json
    • Builds and starts all Docker containers

Access URLs
Service	URL
Multi-Agent API	http://localhost:5000/api/goal
Web UI	http://localhost:3005
Ollama API	http://localhost:11434
Qdrant Dashboard	http://localhost:6333/dashboard
Open WebUI	http://localhost:3000
Flowise	http://localhost:3001
n8n	http://localhost:5678

Usage
Multi-Agent API
Submit a goal:
curl -X POST http://localhost:5000/api/goal \
    -H "Content-Type: application/json" \
    -d '{"goal": "Write a Python script that downloads a webpage"}'
Web UI
    • Open browser at http://localhost:3005
    • Enter goal → Click “Submit Goal” → Result appears below

Self-Improvement
    • Lessons are automatically saved in:
learning/lessons.json
    • Agents use Critic → Improver → Memory to improve performance over time.
    • Vector embeddings stored in Qdrant allow retrieval-based reasoning.

Updating Ollama Models
docker run --rm ollama/ollama:latest ollama pull <model_name>
Available models: phi3, mistral:Q4_K_M, codellama, nomic-embed-text.

Troubleshooting
Error	Solution
missing a mount target	Remove file mounts; only mount directories (agents, learning).
API not responding	Check container logs: docker logs -f multi_agent_lab.
Lessons not saved	Ensure learning/lessons.json exists (startup script creates it).
Web UI not loading	Check logs for multi_agent_webui and port mapping (3005).

Scaling & Extending
    • Add new agents in agents/ folder
    • Add new tools in agents/tools.py
    • Extend Flask API in run_agents.py
    • Automate workflows with Flowise or n8n

License
MIT License
