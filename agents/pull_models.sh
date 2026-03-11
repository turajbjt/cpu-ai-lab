#!/bin/bash
docker run --rm ollama/ollama:latest ollama pull phi3
docker run --rm ollama/ollama:latest ollama pull mistral:Q4_K_M
docker run --rm ollama/ollama:latest ollama pull codellama
docker run --rm ollama/ollama:latest ollama pull nomic-embed-text
