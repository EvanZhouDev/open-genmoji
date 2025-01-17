import requests
import json
import os

def get_prompt_response(user_prompt: str, metaprompt: str) -> str:
    url = "http://localhost:1234/v1/chat/completions"
    headers = {"Content-Type": "application/json"}

    with open(f"{os.path.abspath(os.path.dirname(__file__))}/metaprompt/{metaprompt}.md", "r") as file:
        prompt_content = file.read()

    full_prompt = f'{prompt_content}\n\nUSER PROMPT: "{user_prompt}"'
    json_path = f"{os.path.abspath(os.path.dirname(__file__))}/metaprompt/{metaprompt}.json"

    try:
        with open(json_path, "r") as json_file:
            conversation_history = json.load(json_file)
    except FileNotFoundError:
        conversation_history = {"messages": []}

    conversation_history["messages"].append({"role": "user", "content": full_prompt})

    data = {
        "messages": conversation_history["messages"],
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].replace("```", "").replace("\n", "")
    else:
        raise Exception(f"Failed to get response: {response.status_code}, {response.text}")