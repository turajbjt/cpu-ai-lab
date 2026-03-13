#!/usr/bin/sh

# Run this code to ensure all 4 models (phi3, mistral, codellama, nomic-embed-text) are installed in your Ollama container.
# This avoids timing issues with the bootstrap script.

docker compose exec ollama /bin/sh -c "
for model in phi3 mistral codellama nomic-embed-text; do
  if ollama list | grep -q \$model; then
    echo \"✔ \$model already installed\";
  else
    echo \"⬇ Pulling \$model\";
    ollama pull \$model;
  fi;
done
"

# verify models are are installed:

docker compose exec ollama ollama list


# fix test:
# curl -X POST http://localhost:11434/v1/completions -H "Content-Type: application/json" -d '{"model": "phi3", "prompt": "Write a short poem about AI"}'
