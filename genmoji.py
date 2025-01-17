import sys
from promptAssistant import get_prompt_response
from generateImage import generate_image
from PIL import Image
import os
import argparse
import json

def get_unique_path(base_path):
    directory, filename = os.path.split(base_path)
    base_name, ext = os.path.splitext(filename)
    base_name = base_name.split("-")[0]
    counter = 1
    while True:
        new_path = os.path.join(directory, f"{base_name}-{counter:03d}{ext}")
        if not os.path.exists(new_path):
            return new_path
        counter += 1

def main(user_prompt, direct, height, width, upscale_factor, output_path="output/genmoji.png", lora="flux-dev"):
    try:
        with open("./lora/info.json", "r") as f:
            models = json.load(f)
    except FileNotFoundError:
        print("Error: info.json not found.")
        sys.exit(1)

    metaprompt = next((model["metaprompt"] for model in models if model["name"] == lora), None)
    if not metaprompt:
        print(f"Error: LoRA {lora} does not exist. Run 'python download.py' to view and download available LoRAs.")
        sys.exit(1)

    lora_path = f"lora/{lora}.safetensors"
    if not os.path.exists(lora_path):
        print(f"Error: LoRA {lora} is not downloaded. Please run 'python download.py' to download it.")
        sys.exit(1)

    prompt_response = user_prompt if direct else get_prompt_response(user_prompt, metaprompt)
    print(f"Prompt Created: {prompt_response}" if not direct else f"Original prompt used: {prompt_response}")

    image = generate_image(prompt_response, lora, width, height)
    new_img = image.resize((image.width * upscale_factor, image.height * upscale_factor), Image.LANCZOS)

    output_path = get_unique_path(output_path)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    new_img.save(output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("user_prompt", type=str, help="Your prompt")
    parser.add_argument("-d", "--direct", action="store_true", help="Do not use prompt assistant")
    parser.add_argument("-l", "--lora", default="flux-dev", type=str, help="The LoRA to use")
    parser.add_argument("-iw", "--width", default=160, type=int, help="Image width")
    parser.add_argument("-ih", "--height", default=160, type=int, help="Image height")
    parser.add_argument("-u", "--upscale", default=5, type=int, help="Upscale factor")
    args = parser.parse_args()

    main(args.user_prompt, args.direct, args.height, args.width, args.upscale, lora=args.lora)