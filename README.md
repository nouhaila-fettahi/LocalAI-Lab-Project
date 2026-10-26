# local_ai_lab
Minimal Python client for a local Ollama server.
Run: `python app.py`
## 1. Project Overview

This project implements a local AI assistant using Ollama, Python, Flask, and Retrieval-Augmented Generation (RAG). It answers questions about course materials stored in local text documents and runs without relying on a cloud-based LLM API.

## 2. Main Features

- Runs a language model locally using Ollama.
- Provides a web interface for asking questions.
- Retrieves relevant information from local documents using RAG.
- Supports structured JSON responses.
- Maintains conversation history in the web application.
- Displays response time, token statistics, and document sources.
- Includes local image analysis using a vision-capable model.
- Compares local models through performance benchmarks.

## 3. Technologies Used

- **Python** — application logic and backend.
- **Ollama** — local model execution and REST API.
- **Flask** — web application.
- **Requests** — HTTP communication.
- **Pandas** — benchmark data analysis.
- **Matplotlib** — performance visualization.
- **psutil** — system memory monitoring.

## 4. Project Structure

```text
LocalAI_Lab/
├── report.pdf
├── README.md
├── source/
│   ├── app.py
│   ├── chatbot.py
│   ├── rag.py
│   ├── benchmark.py
│   └── templates/
├── documents/
│   ├── ai.txt
│   ├── ml.txt
│   ├── rl.txt
│   └── other course documents
└── screenshots/
    ├── 01_installation.png
    ├── 02_model.png
    ├── 03_chatbot.png
    ├── 04_python.png
    ├── 05_rag.png
    └── 06_webapp.png
```

## 5. Requirements

- Python 3.10 or later
- Ollama installed and running
- At least one compatible local language model
- Python packages listed in `requirements.txt` or the project's dependency list

## 6. Installation

### Step 1 — Start Ollama

Install Ollama and start the local service.

### Step 2 — Download a model

For example:

```bash
ollama pull gemma3
```

Ensure the model name matches the configuration used by the application.

### Step 3 — Install Python dependencies

Open a terminal in the project directory and run:

```bash
pip install -r requirements.txt
```

If the dependency file is not included in `LocalAI_Lab/`, copy it there or install the required packages manually.

## 7. Running the Application

Open a terminal and navigate to the source directory:

```bash
cd LocalAI_Lab/source
python app.py
```

Open the local address displayed by Flask in your browser. Depending on the application configuration, it may be `http://127.0.0.1:5000`.

Keep Ollama running while using the application.

## 8. Performance Benchmark

The benchmark compares local models using the same prompt. It measures:

- Model disk size
- Loaded model size
- VRAM usage
- Model loading time
- Total response time
- Number of generated tokens
- Tokens generated per second
- System RAM usage

In the recorded experiment, `gemma3:latest` generated responses faster than `qwen3.5:latest` on the test computer. These results depend on the hardware, model configuration, and prompt used.

## 9. Security Considerations

The application is intended for local use. Avoid exposing the Ollama API or Flask development server directly to an untrusted network. Use appropriate network restrictions, authentication, and HTTPS/TLS when remote access is required.

## 11. Limitations

Response quality and speed depend on the selected model and available hardware. The RAG component can only retrieve information present in the available documents, and the model may still generate incorrect answers. Benchmark quality scores were not quantitatively evaluated in the recorded experiment.
