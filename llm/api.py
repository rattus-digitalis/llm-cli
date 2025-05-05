import subprocess

def ask_mistral(prompt: str) -> str:
    try:
        result = subprocess.run(["ollama", "run", "mistral"], input=prompt.encode(), capture_output=True, check=True)
        return result.stdout.decode().strip()
    except subprocess.CalledProcessError as e:
        return f"[Error] Ollama call failed: {e.stderr.decode().strip()}"
    except FileNotFoundError:
        return "[Error] Ollama is not installed or not in PATH."
