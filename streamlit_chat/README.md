# 🦙 TinyLlama Terminal Chatbot (via Ollama API)

This project provides an interactive terminal-based chatbot powered by [TinyLlama](https://ollama.com/library/tinyllama), running locally using [Ollama](https://ollama.com) and accessed through Python's HTTP API.

---

## 📁 Repository Structure

GitHub repository: [nbhaskar76/genai_sample](https://github.com/nbhaskar76/genai_sample)

**Folder structure:**

```
genai_sample/
└── terminal_chatbot/
    ├── streamlit.py
    ├── chat.py
    ├── requirements.txt
    └── README.md
```

## ✅ Requirements
- Python 3.7 or higher
- Ollama installed and running
- Visual Studio Code
- Python extension for VS Code
- requests Python package

## ⚙️ Setup Instructions

1. Clone the Repository
   
```
    git clone https://github.com/nbhaskar76/genai_sample.git
    cd genai_sample/terminal_chatbot
```
2. Create a Python Virtual Environment

```
    python -m venv .venv
```

3. Activate the Virtual Environment

- Windows CMD:
```
    .venv\Scripts\activate
```
- On Windows (PowerShell)

```
    .\.venv\Scripts\Activate.ps1
```
- On macOS / Linux
```
    source .venv/bin/activate
```
4. Select the Python Interpreter in VS Code
- Open VS Code.
- Press Ctrl+Shift+P (or Cmd+Shift+P on macOS).
- Choose Python: Select Interpreter.
- Select the .venv environment from the list.

5. Install Dependencies
- Install required Python packages using:
```
    pip install -r requirements.txt
```

## 🤖 Download the Model with Ollama
Make sure Ollama is installed and running. Then pull the TinyLlama model: The model can be changed as per our need.
```
    ollama pull tinyllama
```
## ▶️ Run the Chatbot

- Run the chatbot :
```
    streamlit run streamlit_app.py
```