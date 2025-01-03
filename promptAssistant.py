import requests
import json
import os


def get_prompt_response(user_prompt: str, metaprompt: str) -> str:
    # The URL where the local server is running
    url = "http://localhost:1234/v1/chat/completions"

    # The headers to indicate that we are sending JSON data
    headers = {"Content-Type": "application/json"}

    # The JSON data payload
    # Read the content from METAPROMPT.md
    with open(
        f"{os.path.abspath(os.path.dirname(__file__))}/metaprompt/{metaprompt}.md", "r"
    ) as file:
        prompt_content = file.read()

    # Append the user prompt
    full_prompt = prompt_content + f'\n\nUSER PROMPT: "{user_prompt}"'

    # get the (pre-made) conversation history and append the current full prompt
    json_path = f"{os.path.abspath(os.path.dirname(__file__))}/metaprompt/{metaprompt}.json"

    try:
        with open(json_path, "r") as json_file:
            conversation_history = json.load(json_file)
            print("Using pre-existing conversation history")
    except FileNotFoundError:
        print("No pre existing conversation history")
        conversation_history = {"messages": []}

    conversation_history["messages"].append({"role": "user", "content": full_prompt})

    data = {
        "messages": conversation_history["messages"],
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False,
    }

    # Making the POST request to the local server
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Checking if the request was successful
    if response.status_code == 200:
        # Returning the response content
        return (
            response.json()
            .get("choices")[0]
            .get("message")
            .get("content")
            .replace("```", "")
            .replace("\n", "")
        )
    else:
        raise Exception(
            f"Failed to get response: {response.status_code}, {response.text}"
        )
