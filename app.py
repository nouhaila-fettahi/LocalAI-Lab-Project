
import time
import requests

URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:3b"

prompt = "Explain recursion in Python in two sentences."

start = time.perf_counter()

try:
    response = requests.post(
        URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "keep_alive": "10m",
            "think": False,
            "options": {
                "num_predict": 80,
                "temperature": 0.2
            }
        },
        timeout=(10, 180)
    )

    response.raise_for_status()
    result = response.json()

    print("Model:", result.get("model", MODEL))
    print("\nResponse:\n", result.get("response", ""))
    print("\nTotal time:", round(time.perf_counter() - start, 2), "seconds")
    print("Load time:", round(result.get("load_duration", 0) / 1e9, 2), "seconds")
    print("Generation time:", round(result.get("eval_duration", 0) / 1e9, 2), "seconds")
    print("Tokens generated:", result.get("eval_count", 0))
    print("Tokens/second:", round(
        result.get("eval_count", 0) /
        max(result.get("eval_duration", 0) / 1e9, 1e-9), 2
    ))

except requests.exceptions.RequestException as error:
    print("Ollama error:", error)
