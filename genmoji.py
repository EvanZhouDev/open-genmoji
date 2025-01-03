import sys
from promptAssistant import get_prompt_response
from generateImage import generate_image
from PIL import Image
import os
import argparse
import json


def get_unique_path(base_path):
    directory = os.path.dirname(base_path)
    filename = os.path.basename(base_path)
    name, ext = os.path.splitext(filename)

    # Remove any existing numbers from name
    base_name = name.split("-")[0]

    counter = 1
    while True:
        new_path = os.path.join(directory, f"{base_name}-{counter:03d}{ext}")
        if not os.path.exists(new_path):
            return new_path
        counter += 1


def main(
    user_prompt: str,
    direct: bool,
    height: int,
    width: int,
    upscale_factor: int,
    output_path: str = "output/genmoji.png",
    lora: str = "flux-dev",
):
    with open("./lora/info.json", "r") as f:
        models = json.load(f)
        metaprompt = "open-genmoji"
        found = False
        for model in models:
            if model["name"] == lora:
                found = True
                metaprompt = model["metaprompt"]
                break

        if not found:
            print(
                f"Error: LoRA {lora} does not exist. Run 'python download.py' to view and download available LoRAs."
            )
            sys.exit(1)

        # Check if the lora file exists
        lora_path = f"lora/{lora}.safetensors"
        if not os.path.exists(lora_path):
            print(
                f"Error: LoRA {lora} is not downloaded. Please run 'python download.py' to download it."
            )
            sys.exit(1)
        if not direct:
            # Get the response from the prompt assistant
            prompt_response = get_prompt_response(user_prompt, metaprompt)
            print("Prompt Created: " + prompt_response)
        elif direct:
            prompt_response = user_prompt
            print("Original prompt used: " + prompt_response)

    # Generate the image using the response from the prompt assistant
    image = generate_image(prompt_response, lora, width, height)

    output_width, output_height = image.size
    new_img = image.resize((output_width * upscale_factor, output_height * upscale_factor), Image.LANCZOS)

    output_path = get_unique_path(output_path)
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    new_img.save(output_path)


if __name__ == "__main__":
    # When function is called it creates an object that looks like this:
    # Namespace(user_prompt='a squirrel holding an iphone', assist=True, lora='flux-dev',
    # width=160, height=160, upscale=5)
    # the args object can then be passed into different functions
    # and its values can be accessed, for example, like this:
    # `args.height` --> returns `160` (as an int)

    parser = argparse.ArgumentParser()
    parser.add_argument("user_prompt", type=str, help="Your prompt")
    parser.add_argument("-d", "--direct",
                        action="store_true", help="Do not use prompt assistant")
    parser.add_argument("-l", "--lora",
                        nargs="?", default="flux-dev",
                        type=str, help="The LoRA to use")
    parser.add_argument("-iw", "--width",
                        nargs="?", default=160,
                        type=int, help="Image width")
    parser.add_argument("-ih", "--height",
                        nargs="?", default=160,
                        type=int, help="Image height")
    parser.add_argument("-u", "--upscale",
                        nargs="?", default=5,
                        type=int, help="Upscale factor")
    args = parser.parse_args()
    user_prompt = args.user_prompt
    lora = args.lora
    direct = args.direct
    height = args.height
    width = args.width
    upscale_factor = args.upscale

    main(
        user_prompt=user_prompt,
        lora=lora,
        direct=direct,
        height=height,
        width=width,
        upscale_factor=upscale_factor
    )
