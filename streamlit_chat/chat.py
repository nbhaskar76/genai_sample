import requests
import json

model = "mistral"  # Specify the model you want to use

def chat_with_llm(user_input, history):

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": model,
            "messages": history + [{"role": "user", "content": user_input}],
            "stream": False,
        }
    )

    data = response.json()

    # Just return the reply — do NOT append to history here
    reply = data.get("message", {}).get("content", "⚠️ No reply received.")
    return reply, history