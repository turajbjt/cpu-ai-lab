#!/bin/bash
set -e

echo "🟢 Starting CPU AI Lab..."

# 1️⃣ Pull Ollama Docker image
echo "Pulling Ollama Docker image..."
docker pull ollama/ollama:latest

# 2️⃣ Pull CPU-friendly Ollama models
echo "Pulling Ollama CPU models..."
docker run --rm ollama/ollama:latest ollama pull phi3
docker run --rm ollama/ollama:latest ollama pull mistral:Q4_K_M
docker run --rm ollama/ollama:latest ollama pull codellama
docker run --rm ollama/ollama:latest ollama pull nomic-embed-text

# 3️⃣ Ensure folders exist for volumes (learning folder)
mkdir -p learning
echo "[]" > learning/lessons.json

# 4️⃣ Build and start all Docker services
echo "Building and starting Docker containers..."
docker compose up --build -d

# 5️⃣ Finished
echo ""
echo "✅ CPU AI Lab is ready!"
echo ""
echo "Access URLs:"
echo "Multi-agent API   -> http://localhost:5000/api/goal"
echo "Web UI interface  -> http://localhost:3005"
echo "Ollama API        -> http://localhost:11434"
echo "Qdrant Dashboard  -> http://localhost:6333/dashboard"
echo "Open WebUI        -> http://localhost:3000"
echo "Flowise           -> http://localhost:3001"
echo "n8n               -> http://localhost:5678"
