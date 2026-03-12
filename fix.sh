#!/usr/bin/sh

echo "Steps to fully clean up the conflicting Ollama container"

echo " "
echo "1️⃣ Check for 'ghost' container names"
docker ps -a --filter "name=ollama"

#If this returns nothing, Docker doesn’t see it, which explains the No such container error.

echo " "
echo "2️⃣ Check Docker volumes and networks"

echo " "
echo "-> Sometimes the conflict comes from a volume or network left over from a previous run:"
docker volume ls | grep ollama
docker network ls | grep cpu-ai-lab

echo " "
echo "-> Remove the Ollama volume if it exists:"
docker volume rm cpu-ai-lab_ollama

echo " "
echo "-> Remove the lab network if needed:"
docker network rm cpu-ai-lab_default

echo "3️⃣ Prune unused Docker resources (safe clean-up)"
echo " "
echo "-> #This removes all stopped containers, unused networks, and dangling images:"
docker system prune -a --volumes

echo " "
echo "⚠️ Warning: This deletes all unused containers, networks, images, and volumes on your system, not just lab-related ones."

echo " "
echo "4️⃣ Retry the lab"
./lab up

echo "=> It should now start fresh without detecting the conflicting container."
echo " "
