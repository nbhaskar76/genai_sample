import requests

model = "tinyllama" # Specify the model you want to use

def chat_with_llm(prompt, history=None):
    url = "http://localhost:11434/api/chat"
    messages = history if history else []
    messages.append({"role": "user", "content": prompt})

    payload = {
        "model": model,
        "messages": messages,
        "stream": True  # Enable streaming if supported
    }

    response = requests.post(url, json=payload, stream=True)

    assistant_reply = ""
    if response.status_code != 200:
        print(f"API returned status {response.status_code}")
        print("Response content:", response.text)
        return f"Error: API returned status {response.status_code}", messages

    try:
        # Read response line by line
        for line in response.iter_lines():
            if line:
                # Decode JSON per line
                data = line.decode('utf-8')
                json_data = None
                try:
                    import json
                    json_data = json.loads(data)
                except Exception:
                    print("Skipping non-JSON line:", data)
                    continue

                if 'message' in json_data and 'content' in json_data['message']:
                    assistant_reply += json_data['message']['content']

        messages.append({"role": "assistant", "content": assistant_reply})

    except Exception as e:
        print("Error processing streamed response:", e)
        return "Error processing response", messages

    return assistant_reply, messages


if __name__ == "__main__":
    history = []
    print(f"""Chat with {model}! Type 'exit' to quit.\n""")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        reply, history = chat_with_llm(user_input, history)
        print(f"""{model}:""", reply)
