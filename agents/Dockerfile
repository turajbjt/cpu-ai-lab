FROM python:3.14-slim

WORKDIR /app

# Copy agent code and run_agents.py inside container
COPY agents/ ./agents/
COPY run_agents.py ./run_agents.py

# Create learning folder inside container if it doesn't exist
RUN mkdir -p ./learning && \
    echo "[]" > ./learning/lessons.json

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Start the multi-agent HTTP API
CMD ["python", "run_agents.py"]
