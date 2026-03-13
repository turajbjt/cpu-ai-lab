# CPU AI Lab 🖥️

**CPU AI Lab** is a fully containerized AI lab environment running entirely on CPU. It integrates:

* Ollama (LLMs)
* Open WebUI
* Flowise
* Qdrant
* n8n
* Multi-agent AI framework

It is **turn-key** — start everything with a single command and start experimenting immediately.

For setup instructions, see [Quick Start](QUICK_START.md)  
For full AI reset, see [Reset](RESET.md)  
For troubleshooting, see [Troubleshooting](TROUBLESHOOTING.md)  
For validating services, see [Health Check](HEALTHCHECK.md)  
For CLI flag reference, see [Flags](FLAGS.md)  
For What It Can Do, see [What It Can Do](WHAT_CAN_DO.md)

## 🚀 First-Run Setup (Quick Run)

# Super quick reset and start

Clone the repository

```bash
git clone https://github.com/turajbjt/cpu-ai-lab.git
cd cpu-ai-lab
```

Start CPU AI Lab (super quick one-liner)

```bash
./lab up --no-logs --fast-start && echo -e "\n✅ CPU AI Lab environment is up and running!"
```

🔹 What this does:

* Removes old containers, volumes, and network
* Pulls/builds Docker images (Ollama, Flowise, OpenWebUI, Agents, Qdrant, N8N)
* Starts all containers in the correct order
* Skips logs and health checks for maximum speed

**Notes:**

* Containers are running in the background — services may not be fully ready until a few seconds after startup.
* You can check logs later if needed:  ``docker logs -f ollama``
* If you want full startup with health checks and logs, just run: ``./lab up``


## ✨ Features

* CPU-friendly Ollama models: phi3, mistral, codellama, nomic-embed-text
* Multi-agent system for AI workflows
* Web UI for interacting with agents
* Flowise orchestration flows
* Qdrant vector database for embeddings/search
* n8n workflow automation
* Automatic Ollama model bootstrap
* Persistent volumes for all services
* Conflict-free startup (old Ollama containers are removed automatically)
* Auto-removal of stale/conflicting Ollama containers


## 💾 Volumes & Persistence

| **Volume** | **Purpose** |
| ---------- | ----------- |
| ollama     | Ollama models and configs |
| openwebui  | WebUI data |
| flowise    | Flowise flows |
| qdrant     | Qdrant vector storage |
| n8n        | n8n workflows |


## ⚙️ Requirements

* Docker ≥ 24
* Docker Compose ≥ 2
* Linux, macOS, or Windows with WSL2



## 📄 License

This repo is provided under the MIT License.

