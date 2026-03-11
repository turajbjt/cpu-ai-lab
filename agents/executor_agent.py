import subprocess
import tempfile

def execute(code: str) -> str:
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as f:
        f.write(code.encode())
        path = f.name

    try:
        result = subprocess.check_output(["python3", path], stderr=subprocess.STDOUT)
        return result.decode()
    except Exception as e:
        return str(e)
