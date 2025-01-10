import os
from ollama import Client, Options, Message, ResponseError
from typing import Dict, List
from domain.prompts import SYSTEM_PROMPT


OLLAMA_HOST_DEFAULT="http://localhost:11434"
OLLAMA_HOST = os.getenv("OLLAMA_HOST")
client = Client(host=OLLAMA_HOST)


def model_inference(
        user_prompt: str,
        model_name: str,
        max_output: int = 128,
        temperature: float = 0.7
) -> Dict[str, str]:
    try:
        # prime conversation with system prompt and few shot
        messages = [
            Message(role="system", content=SYSTEM_PROMPT),
            Message(role="user", content="a horse wearing a suit"),
            Message(role="assistant", content="emoji of horse in black suit and tie with flowing mane. a strong, confident stallion wearing formal attire for a special occasion. cute. 3D lighting. no cast shadows. enlarged head in cartoon style. head is turned towards viewer."),
            Message(role="user", content="flying pig"),
            Message(role="assistant", content="emoji of flying pink pig. enlarged head in cartoon style. cute. white wings. head is turned towards viewer. 3D lighting. no cast shadows."),
            Message(role="user", content=user_prompt)
        ]
        response = client.chat(
            model=model_name,
            messages=messages,
            options=Options(temperature=temperature, num_predict=max_output))

        return {"message": response.get("message").content}
    except ResponseError as e:
        if e.status_code == 404:
            return {"message": f"Model {model_name} not found"}
        return {"message": f"Error performing inference: {e.error}"}
    except Exception as e:
        return {"message": f"Error performing inference: {e}"}


def list_installed_llms() -> List[str]:
    models = client.list()

    return [
        {
            "model_name": model.get("model"),
            "family": model.get("details", {}).get("family"),
            "param_size": model.get("details", {}).get("parameter_size"),
        }
        for model in models.get("models")
    ]