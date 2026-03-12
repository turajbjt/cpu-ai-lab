## 🩺 CPU AI Lab Health Checks

CPU AI Lab includes automated health checks in the ./lab startup script to ensure all services are fully operational before use. This file explains how they work and what they check.

1️⃣ **Overview**

The health checks verify:

| **Service**   | **Check Method**           | **Port / Endpoint**          |
| --------- | ---------------------- | ------------------------ |
| OpenWebUI | HTTP GET               | `http://localhost:5000`  |
| Flowise   | HTTP GET               | `http://localhost:3000`  |
| N8N       | HTTP GET               | `http://localhost:5678`  |
| Ollama    | API GET `/v1/models`   | `http://localhost:11434` |
| Qdrant    | API GET `/collections` | `http://localhost:6333`  |

If any service fails to respond, the startup script waits and retries until the service is available.


2️⃣ **How Health Checks Work**

1. Web Services (OpenWebUI, Flowise, N8N):

* The script sends an HTTP request to the service URL.
* If it responds successfully, the service is marked as ready.

2. Ollama Model Server:

* Sends a GET request to http://localhost:11434/v1/models.
* Waits until the model server responds, ensuring the AI models are loaded.

3. Qdrant Vector Database:

* Sends a GET request to http://localhost:6333/collections.
* Waits until the service responds, ensuring the database is operational.


3️⃣ **Flags Affecting Health Checks**

| **Flag**           | **Effect on Health Checks**                                                               |
| -------------- | ------------------------------------------------------------------------------------- |
| `--fast-start` | Skips all health checks. Containers are started, but services may not be fully ready. |
| `--no-logs`    | Logs are hidden, but health checks still run unless `--fast-start` is used.           |

**Example:** Full startup with health checks and logs

./lab up

**Example:** Skip health checks but start containers

./lab up --fast-start


4️⃣ **Troubleshooting Health Check Failures**

*Service does not respond:*

* Check that the container is running:

```bash
docker ps | grep <service_name>
```

* If the container is not running, restart the lab with:

```bash
./lab up --no-logs
```

**Port conflicts:**

* Make sure the required ports are not in use by other applications.

✅ Health checks ensure that CPU AI Lab is fully ready before you start using the environment, saving time and avoiding partial service failures.

