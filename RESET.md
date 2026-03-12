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

```bash
./lab up
```

This will rebuild all containers, start Ollama with the CPU-friendly models, and ensure the lab environment is fully clean.

