import json
from huggingface_hub import hf_hub_download

# Read info.json
with open("./lora/info.json", "r") as f:
    models = json.load(f)

# Print menu
print("Available models:")
for i, model in enumerate(models):
    print(
        f"[{i}] {model['name']} ({model['model'].split('/')[1]})\n> {model['description']}"
    )

# Get user choice
choice = int(input("\nSelect a model (enter number): "))

if 0 <= choice < len(models):
    selected = models[choice]
    filename = f"{selected['name']}.safetensors"

    print(f"\nDownloading {selected['name']}...")
    print(
        "Downloaded weights to: "
        + hf_hub_download(
            repo_id=selected["huggingface"], filename=filename, local_dir="./lora"
        )
    )
else:
    print("Invalid selection")
