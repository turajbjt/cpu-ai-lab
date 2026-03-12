## 🛠 Troubleshooting

1️⃣ Container name conflicts

**Problem:**

If you see:

``Conflict. The container name "/ollama" is already in use``

**Solution:**

Run this:

```bash
docker stop ollama
docker rm ollama
```

OR

Run the full reset one-liner:
```bash
./lab up --no-logs && echo "✅ CPU AI Lab environment has been reset and started successfully!"``
```

Then try:

```bash
./lab up
```

2️⃣ Docker volume leftovers

**Problem:**

You get errors related to volumes, e.g., ``Volume cpu-ai-lab_ollama already exists.``

**Solution:**

Remove the specific volume manually:

```bash
docker volume rm cpu-ai-lab_ollama
```

Or use the reset script which handles all volumes automatically.


3️⃣ Port conflicts

**Problem:**

Some services fail to start because ports like 5000, 3000, 5678, 11434, or 6333 are already in use.

**Solution:**

Check which process is using the port:

```bash
sudo lsof -i :5000
```

4️⃣ Ollama or Qdrant not responding

**Problem:**

Containers are running, but API requests fail.

**Solution:**

Make sure the container is fully started:

```bash
docker ps | grep ollama
docker ps | grep qdrant
```

Use the health-check endpoints manually:

```bash
curl http://localhost:11434/v1/models  # Ollama
curl http://localhost:6333/collections # Qdrant
```

If unresponsive, reset containers:

```bash
./lab up --no-logs
```

5️⃣ Pull/build failures

**Problem:**

``docker pull`` or ``docker build`` fails due to network or image errors.

**Solution:**

Check internet connection

Retry:

```bash
docker-compose build --no-cache
```

Make sure Docker Hub or custom images are accessible.


6️⃣ Logs too verbose

**Problem:**

Real-time logs make it hard to read output during startup.

**Solution:**

Use the ``--no-logs` flag:

```bash
./lab up --no-logs
```

7. Ollama models missing:

Make sure Docker has enough disk space and network connectivity.

✅ These steps cover all common setup issues and ensure a smooth start.

