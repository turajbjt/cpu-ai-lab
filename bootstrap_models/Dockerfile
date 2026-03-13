# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy any requirements file if you have one
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Copy bootstrap scripts (if any)
COPY . .

# Expose ports if your bootstrap service has any HTTP endpoints
# Example: EXPOSE 8000
# EXPOSE 8000

# Default command (do nothing, placeholder)
CMD ["sleep", "infinity"]

