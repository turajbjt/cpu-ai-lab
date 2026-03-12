#!/usr/bin/sh

# Run manually, to trigger model bootstrap manually (for debugging):

docker run --rm --name bootstrap_models \
  --link ollama:ollama \
  ollama/ollama \
  /bin/sh -c "
  until curl -s http://ollama:11434/api/tags >/dev/null; do sleep 2; done;
  for model in phi3 mistral codellama nomic-embed-text; do
    if curl -s http://ollama:11434/api/tags | grep -q \$model; then
      echo '\$model already installed';
    else
      docker exec ollama ollama pull \$model;
    fi;
  done
"
