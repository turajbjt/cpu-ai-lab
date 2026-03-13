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


## 🚀 Features

* Run local LLMs using Ollama
* Manage embeddings and vector storage with Qdrant
* CPU-friendly setup; no GPU required
* Web interface for experiments
* Modular architecture with Docker for easy deployment


## ⚙️ Requirements

🛠  Prerequisites

Make sure the following are installed:

* Docker ≥ 24.x
* Docker Compose ≥ 2.18.x
* CPU supporting AVX instructions (required by some LLMs)
* Optional: Python 3.11+ (if running scripts outside Docker)
* Linux, macOS, or Windows with WSL2


📂 Repository Structure

``
cpu-ai-lab/
├─ docker-compose.yml       # Docker Compose setup
├─ requirements.txt         # Python dependencies
├─ .env.example             # Example environment variables
├─ lab_up                   # Start all containers
├─ lab_down                 # Stop all containers
├─ QUICK_START.md           # Quick start guide
├─ TROUBLESHOOTING.md       # Known issues & fixes
└─ WHAT_CAN_DO.md           # Capabilities of the lab
``

## ⚡ First-Run Setup (Quick Run)

# Super quick reset and start

1. Clone the repository

```bash
git clone https://github.com/turajbjt/cpu-ai-lab.git
cd cpu-ai-lab
```

2. Copy environment variables

```bash
cp .env.example .env
```

Edit .env if needed (ports, API keys, or memory limits).

3. Start Docker Containers

```bash
./lab up
```

This will start:

* LLM service (Ollama)
* Vector database (Qdrant)
* Web UI/API services

4. Access the lab

* Web interface: http://localhost:3000 (or port defined in .env)
* Qdrant UI: http://localhost:6333

5. Stop containers

```bash
./lab_down
```


# 📦 Dependencies

``requirements.txt`` (pinned versions recommended):

``bash
langchain==0.3.1
qdrant-client==1.2.2
requests==2.31.0
Flask==2.3.2
```

⚠  *Avoid latest tags for Docker images; pin to a stable version to prevent breaking changes.*


# 🩺 Health Checks

* Ollama: curl http://localhost:11434/v1/models
* Qdrant: curl http://localhost:6333/collections

Docker containers include optional healthcheck entries to monitor availability.


# 📝 Environment Variables

Example ``.env`` variables:

```bash
WEB_PORT=3000
QDRANT_PORT=6333
OLLAMA_MODEL=llama2
```


# 🐞 Troubleshooting

* CPU not supported: Some LLMs require AVX instructions → check lscpu | grep avx
* Docker Compose fails: Ensure Docker ≥ 24.x and Compose ≥ 2.18.x
* Port conflicts: Update .env with available ports

Full troubleshooting: see TROUBLESHOOTING.md


# 🌟 Recommended Improvements

* Add GitHub Actions for CI/testing
* Provide example datasets for experiments
* Include screenshots of Web UI for clarity


# 📜 License

MIT License


