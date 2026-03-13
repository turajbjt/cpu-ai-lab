## 🖥 CPU AI Lab – Quick Start 

1️⃣ Clone the repository

```bash
git clone <repo-url> cpu-ai-lab
cd cpu-ai-lab
```

2️⃣ Run the lab (full startup - pulls Docker images and bootstraps Ollama models automatically):

```bash
./lab up
```

Stop the lab:

```bash
./lab down
```

✅ The lab script automatically removes any existing Ollama container to avoid conflicts.

**What happens:**

* Cleans up old containers, volumes, and networks
* Pulls/builds Docker images: Ollama, Flowise, WebUI, Agents, Qdrant, N8N
* Starts all containers in the correct order
* Streams real-time logs for each container
* Performs health checks to ensure all services are responsive

**Output example (colors):**

* ℹ️ Blue → Info / progress
* ⚠️ Yellow → Warnings
* ✅ Green → Success / ready
* ❌ Red → Errors


3️⃣ Fast start options

| **Command** | **Description** |
| ----------- | --------------- |
| ./lab up --no-logs | Startup without real-time logs, but still runs health checks |
| ./lab up --fast-start | Quick start, skips health checks, shows logs |
| ./lab up --no-logs --fast-start | Fastest startup, no logs, no health checks |

4️⃣ One-line reset and start (recommended for new installs)

```bash
./lab up --no-logs && echo -e "\n✅ CPU AI Lab environment has been reset and started successfully!"
```

**Benefits:**

* Fully resets containers, volumes, and network
* Builds/pulls required images
* Starts all services automatically
* Clean output for scripts or automated deployments

5️⃣ Accessing services

## 🌐 Access URLs

| **Service**      | **URL** |
| ---------------- | ------- |
| Open WebUI       | http://localhost:3000 |
| Flowise          | http://localhost:3001 |
| Browser UI       | http://localhost:3005 |
| Ollama API       | http://localhost:11434 |
| Multi-Agent API  | http://localhost:5000/api/goal |
| Qdrant Dashboard | http://localhost:6333/dashboard |
| n8n              | http://localhost:5678 |

6️⃣ Notes

* Ensure Docker ≥ 24 and Docker Compose ≥ 2 are installed.
* Make sure your system has enough space (~400 MB for Ollama image).
* Press Ctrl+C to exit log streams — containers continue running in the background.
* To check logs later for a specific container:

```bash
docker logs -f ollama
```

## 📝 Notes

First run may take a few minutes to pull images and models.

Re-running ./lab up is safe; models are not re-downloaded.

Ollama container is automatically cleaned up before startup to prevent conflicts.
