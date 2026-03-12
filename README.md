# CPU AI Lab 🖥️

**CPU AI Lab** is a fully containerized AI lab environment running entirely on CPU. It integrates:

* Ollama (LLMs)
* Open WebUI
* Flowise
* Qdrant
* n8n
* Multi-agent AI framework

It is **turn-key** — start everything with a single command and start experimenting immediately.


## 🖼 Quick Demo Screenshots

Open WebUI

(replace with your screenshot)

Flowise Flow Designer

(replace with your screenshot)

Ollama API / Multi-agent Logs

(replace with your screenshot)


## 🚀 First-Run Setup

Clone the repo:

```bash
git clone <repo-url> cpu-ai-lab
cd cpu-ai-lab
```

Start the lab (pulls Docker images and bootstraps Ollama models automatically):

```bash
./lab up
```

Stop the lab:

```bash
./lab down
```

✅ The lab script automatically removes any existing Ollama container to avoid conflicts.


## 🌐 Access URLs

| **Service**      | **URL** |
| ---------------- | ------- |
| Open WebUI       | http://localhost:3000 |
| Flowise          | http://localhost:3001 |
| Multi-agent API  | http://localhost:5000/api/goal |
| Ollama API       | http://localhost:11434 |
| Qdrant Dashboard | http://localhost:6333/dashboard |
| n8n              | http://localhost:5678 |


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


## 📝 Notes

First run may take a few minutes to pull images and models.

Re-running ./lab up is safe; models are not re-downloaded.

Ollama container is automatically cleaned up before startup to prevent conflicts.


## 🔄 Resetting the CPU AI Lab

The CPU AI Lab now includes an **enhanced reset** feature that lets you start completely fresh. This is useful if you want to:

* Remove all running containers
* Clear the Ollama container and its volume
* Reinitialize local learning data

**Usage**

Run the following command from the project root:

```bash
./lab reset
```

This will:

* Stop and remove all Docker containers associated with the lab.
* Remove the Ollama container if it exists.
* Delete the Ollama Docker volume to clear cached models.
* Reinitialize learning/lessons.json to an empty state.

**After Reset**

Once reset is complete, you can start the lab as usual:

``bash
./lab up
```

This will rebuild all containers, start Ollama with the CPU-friendly models, and ensure the lab environment is fully clean.


## 🛠 Troubleshooting

1. Container name conflict:

If you see:

``Conflict. The container name "/ollama" is already in use``

Run:

```bash
docker stop ollama
docker rm ollama
```

Then try:

```bash
./lab up
```

2. Ollama models missing:

Make sure Docker has enough disk space and network connectivity.


## 📄 License

This repo is provided under the MIT License.

