import requests
import subprocess

def run_python(code: str) -> str:
    try:
        result = subprocess.check_output(["python3", "-c", code], stderr=subprocess.STDOUT)
        return result.decode()
    except Exception as e:
        return str(e)

def trigger_n8n(data: str) -> str:
    r = requests.post("http://localhost:5678/webhook/ai", json={"input": data})
    return r.text
