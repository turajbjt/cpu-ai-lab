from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI(title="CPU AI Lab WebUI")

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>CPU AI Lab WebUI</title>
        </head>
        <body>
            <h1>✅ CPU AI Lab is running!</h1>
            <p>Multi-agent lab, Qdrant, and WebUI are up and ready.</p>
        </body>
    </html>
    """

# Optional: healthcheck endpoint for scripts
@app.get("/health")
async def health():
    return {"status": "ok"}

