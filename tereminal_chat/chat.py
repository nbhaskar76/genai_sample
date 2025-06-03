import requests
import json

MODEL = "mistral"
OLLAMA_URL = "http://localhost:11434/api/chat"

def chat_with_llm(prompt, history=None):
    history = history or []
    history.append({"role": "user", "content": prompt})

    payload = {
        "model": MODEL,
        "messages": history,
        "stream": True  # Set to False if you don't want streaming
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, stream=True)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"❌ API error: {e}", history

    assistant_reply = ""

    try:
        for line in response.iter_lines():
            if line:
                try:
                    chunk = json.loads(line.decode("utf-8"))
                    content = chunk.get("message", {}).get("content", "")
                    assistant_reply += content
                except json.JSONDecodeError:
                    continue
    except Exception as e:
        return f"❌ Error reading response: {e}", history

    history.append({"role": "assistant", "content": assistant_reply})
    return assistant_reply, history

# CLI entry point
if __name__ == "__main__":
    print(f"💬 Chat with {MODEL}! Type 'exit' to quit.\n")
    history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            break
        reply, history = chat_with_llm(user_input, history)
        print(f"{MODEL}: {reply}")
