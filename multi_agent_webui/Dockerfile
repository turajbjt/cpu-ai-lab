# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy web UI code
COPY . .

# Expose port 80 for WebUI
EXPOSE 80

# Default command to start WebUI
CMD ["python", "app.py"]

