<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/banner@dark.png">
  <source media="(prefers-color-scheme: light)" srcset="./assets/banner@light.png">
  <img alt="Open Genmoji Banner" src="./assets/banner@light.png">
</picture>

<p align="center">
  <a href="https://huggingface.co/EvanZhouDev/open-genmoji">HuggingFace</a> | <a href="#quickstart">Quickstart</a> | <a href="#tutorial">Tutorial</a> | <a href="https://www.youtube.com/watch?v=vOVDyRIS09k">Making Open Genmoji (Video)</a>
</p>

## What is Open Genmoji?

> See how Open Genmoji was created—and learn about how Apple Genmoji works under-the-hood, on [YouTube](https://www.youtube.com/watch?v=vOVDyRIS09k).

Open Genmoji attempts to recreate Apple's Genmoji feature, but with open technology! Open Genmoji works anywhere—Not just Apple devices.

Here's a sneak peek of what Open Genmoji is capable of:
| ![](./assets/genmoji-samples/open-genmoji/flying-pig.png) | ![](./assets/genmoji-samples/open-genmoji/horse.png) |![](./assets/genmoji-samples/open-genmoji/space-bear.png) | ![](./assets/genmoji-samples/open-genmoji/popsicle.png) | ![](./assets/genmoji-samples/open-genmoji/fireplace.png) | ![](./assets/genmoji-samples/open-genmoji/robber.png) | ![](./assets/genmoji-samples/open-genmoji/hiker.png) |
| --------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------- | ---------------------------------------------------- |---------------------------------------------------- |

<details>
<summary>Prompts, Apple Genmoji Comparison, and More Information</summary>

All shown emojis were created with the `flux-dev` Open Genmoji LoRA and Prompt Assist. The exact same prompt was given to both Open Genmoji and Apple. Prompt Assist was run with Qwen 2.5 32B Instruct.

Background of emojis removed with Figma AI.

The 7 samples were selected to demonstrate the ability of Open Genmoji across Animal, Object, and Person emojis.

| Prompt                                                                  | Open Genmoji                                              | Apple                                              |
| ----------------------------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------- |
| `flying pig white wings` (Animal Emoji)                                 | ![](./assets/genmoji-samples/open-genmoji/flying-pig.png) | ![](./assets/genmoji-samples/apple/flying-pig.png) |
| `handsome horse in black suit and tie with flowing mane` (Animal Emoji) | ![](./assets/genmoji-samples/open-genmoji/horse.png)      | ![](./assets/genmoji-samples/apple/horse.png)      |
| `teddy bear in space suit` (Animal Emoji)                               | ![](./assets/genmoji-samples/open-genmoji/space-bear.png) | ![](./assets/genmoji-samples/apple/space-bear.png) |
| `rainbow popsicle` (Object Emoji)                                       | ![](./assets/genmoji-samples/open-genmoji/popsicle.png)   | ![](./assets/genmoji-samples/apple/popsicle.png)   |
| `fireplace` (Object Emoji)                                              | ![](./assets/genmoji-samples/open-genmoji/fireplace.png)  | ![](./assets/genmoji-samples/apple/fireplace.png)  |
| `robber with money bag` (Person Emoji)                                  | ![](./assets/genmoji-samples/open-genmoji/robber.png)     | ![](./assets/genmoji-samples/apple/robber.png)     |
| `hiker` (Person Emoji)                                                  | ![](./assets/genmoji-samples/open-genmoji/hiker.png)      | ![](./assets/genmoji-samples/apple/hiker.png)      |

</details>

<br>

At its core, Open Genmoji is simply a collection of LoRA files (available on [HuggingFace](https://huggingface.co/EvanZhouDev/open-genmoji)), each finetuned based on thousands of Apple emojis, that teaches an image generation model to create emojis. Anywhere you can add a LoRA onto an image generation model, you can use Open Genmoji.

Open Genmoji also comes with a special metaprompts, known as [Open Genmoji Prompt Assist](#prompt-assist) to help you create the perfect prompt to make any emoji you want. Some Open Genmoji LoRAs may have their own metaprompts.

The best part? You can also [use your creation in iOS 18+ as a real emoji](#postprocessing)—Even if your phone doesn't support Apple Intelligence.

If you're experienced with Image Models, go to [Quickstart](#quickstart). Otherwise, check out the [Tutorial](#tutorial) for a full explanation.

Be sure to read the [Important Things to Know](#important-things-to-know) and [Tips for Prompting](#tips-for-prompting)!

## Table of Contents

- [Important Things to Know](#important-things-to-know)
- [Downloading the Model](#downloading-the-model)
- [Quickstart](#quickstart)
- [Tips for Prompting](#tips-for-prompting)
- [Prompt Assist](#prompt-assist)
- [Tutorial](#tutorial)
  - [Running Open Genmoji with `mflux`](#running-open-genmoji-with-mflux)
  - [Running Open Genmoji with Prompt Assist](#running-open-genmoji-with-prompt-assist)
  - [LM Studio Prompt Assist and `mflux` Workflow](#lm-studio-prompt-assist-and-mflux-workflow)
- [Postprocessing](#postprocessing)
- [Contributing](#contributing)

## Important Things to Know

> **Please read this before continuing with the repository!**

TL;DR: Use **Python 3.11** and **use HuggingFace** to download weights

1. This project **works best with Python 3.11**. If you have a Python Version Manager, simply instally Python 3.11, and use the `python3.11` command in place of all commands that say `python3`, and also ensure to create your `.venv` with `python3.11`
2. The various LoRA weights for this project are **hosted on HuggingFace** at [EvanZhouDev/open-genmoji](https://huggingface.co/EvanZhouDev/open-genmoji). Check [Downloading the Finetune](#downloading-the-finetune) below for more info.

## Downloading the Finetune

Various Open Genmoji LoRAs are available on HuggingFace at [EvanZhouDev/open-genmoji](https://huggingface.co/EvanZhouDev/open-genmoji). However, there's a script included in this repository that makes downloading these LoRAs simple.

First, clone into this repo:

```bash
git clone https://github.com/EvanZhouDev/open-genmoji.git
```

Next, we need to install the `huggingface_hub` library. It is recommended you first create a `venv`.

```bash
# Create a venv, optional
python3 -m venv .venv
source .venv/bin/activate

# Install huggingface_hub
pip install -U huggingface_hub
```

Now, all you have to do is run the `download.py` script available in the root directory:

```bash
python3 download.py
```

You are now able to pick which LoRA you want to install. Each LoRA has a brief description, and the model it works with. For example, let's choose the `flux-dev` LoRA.

Give it a few seconds, and check that `lora/flux-dev.safetensors` is installed. It should be a 209MB file. You're all good to go! Choose the LoRA you want for whatever you're doing.

## Quickstart

> If you're looking for detailed steps to run the model, check out the [Tutorial](#tutorial)

If you know what you're doing, here's a quickstart guide:

- Use **Python 3.11** to ensure everything works
- Get a LoRA from HuggingFace at [EvanZhouDev/open-genmoji](https://huggingface.co/EvanZhouDev/open-genmoji). Check out [Downloading the Finetune](#downloading-the-finetune) above for more info. There are various available.
- Metaprompts for Open Genmoji are available in the `metaprompt` folder, so you can create the perfect prompt. [Learn more here.](#prompt-assist) I highly recommend using it!
- Run the correct image model with the LoRA you downloaded (i.e. Flux.1 Dev). Check out [Postprocessing](#postprocessing) to learn how to use your creation as a real emoji in iOS 18

## Tips for Prompting

The trigger word for the LoRA (what the image model needs to "hear" to start generating emojis) is "emoji". If you do not include this in your prompt, there is a high chance it won't generate an actual emoji.

Furthermore, in order to develop a good prompt, I **highly recommend using Prompt Assist**.

## Prompt Assist

Open Genmoji Prompt Assist is a way to use a metaprompt with Open Genmoji, to help you generate the perfect prompt for the Open Genmoji finetuned models. Note that each finetuned model may have its own metaprompt. See `lora/info.json` to see which metaprompt each model uses. Then, find that metaprompt in the `metaprompt` folder.

> However, if you're generating Apple Emojis, `metaprompt/open-genmoji.md` should work fine.

Here's an example of what Prompt Assist does:

| Input        | Output                                                                                                                                      |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `flying pig` | `emoji of flying pink pig. enlarged head in cartoon style. cute. white wings. head is turned towards viewer. 3D lighting. no cast shadows.` |

> This was generated with `metaprompt/open-genmoji.md`

Now, you can focus on imagining the perfect emoji, while Prompt Assist helps you phrase it in a way that image models can understand.

The metaprompts can be used in any LLM, such as ChatGPT, to generate a prompt for Open Genmoji.

Check out [LM Studio Prompt Assist and `mflux` Workflow](#lm-studio-prompt-assist-and-mflux-workflow) for my full workflow of using LM Studio and `mflux` together to run Open Genmoji on Mac. This workflow automatically picks the metaprompt for the correct LLM, so you don't need to worry about checking the `info.json`.

## Tutorial

> This tutorial is **specifically for MacOS**. However, Open Genmoji is completely adaptable for other operating systems. You will just need another tool to run Flux.1 Dev, with a LoRA.

If you're new to Image Generation or locally running models, this is the place for you. This guide will lead you through all the steps necessary to run Open Genmoji, and also use the Open Genmoji Prompt Assist metaprompt.

Before you start, ensure you are using Python 3.11. The easiest way to do this is by installing Python 3.11 with your method of choice, then replacing the CLI command `python3`/`python` with `python3.11`. Ensure you also create your `venv` with Python 3.11.

First, let's get started by simply running the model.

### Prerequisites

Before everything, we need to set up Hugging Face. If you already have a Hugging Face token, logged in to the CLI, and agreed to Flux.1 Dev terms and conditions, skip to [Running Open Genmoji with `mflux`](#running-open-genmoji-with-mflux)

**Setting Up Hugging Face**:

1. Go to [Hugging Face](https://huggingface.co) and make an account. Verify your email.
2. Go to [Hugging Face Token Settings](https://huggingface.co/settings/tokens) and create a token. Ensure you either have Token Type of **Read** at the top, or check **Read access to contents of all public gated repos you can access** in token type Fine-grained.
3. Install the [Hugging Face CLI](https://huggingface.co/docs/huggingface_hub/en/guides/cli) with your method of choice (Homebrew, pip, etc.)
4. Run `huggingface-cli login` and use your token to login
5. Finally, go to [Flux.1 Dev Hugging Face Page](https://huggingface.co/black-forest-labs/FLUX.1-dev). Read and agree to the terms at the top to use the Gated model.

You're all done! When you run `mflux` below for the first time, it'll automatically download Flux.1 Dev.

### Running Open Genmoji with `mflux`

The image model we'll be using in this guide is Flux.1 Dev. Open Genmoji takes the form of a LoRA, which is just a file that can teach the image model how to do something specific. In this case, create emojis!

First, clone this repository:

```bash
git clone https://github.com/EvanZhouDev/open-genmoji.git
```

Next, we need to install some dependencies. It's recommended we create a `venv`:

```bash
# Create a venv, optional
python3 -m venv .venv
source .venv/bin/activate

# Install huggingface_hub and mflux
pip install -U huggingface_hub mflux
```

Here's what those dependencies are:

- `huggingface_hub`: This will help us download the weights that we need to run Open Genmoji
- `mflux`: This is a port of Flux (to run our image generation model), specifically for Mac.

Now, let's actually install the LoRA. There are various available on HuggingFace at [EvanZhouDev/open-genmoji](https://huggingface.co/EvanZhouDev/open-genmoji), for different uses, but there's a quick installation script you can run in this directory:

```bash
python3 ./download.py
```

Now, you can pick which LoRA you want. For this tutorial, let's install the one named `flux-dev`. Use arrow keys to navigate to it, and press enter to select.

After it's done installing, verify that `lora/flux-dev.safetensors` is downloaded. That'll be the LoRA that you'll be using.

Now, you're all good to go. Run the following command and you'll be able to create your first emoji. Play around with the prompt, and see what you can make. (If you're struggling with a good result, check out [Prompt Assist](#running-open-genmoji-with-prompt-assist))

```bash
mflux-generate \
    --model dev \
    --prompt "your prompt" \
    --steps 20 \
    --seed 2 \
    --quantize 8 \
    --guidance 5.0 \
    --width 160 \
    --height 160 \
    --lora-paths "./lora/flux-dev.safetensors"
```

### Running Open Genmoji with Prompt Assist

It's pretty difficult to get a good prompt to make a Apple-like emoji. Thus, we'll use a metaprompt... a prompt for an LLM, to make a prompt for Open Genmoji. Here's an example:

| Input        | Output                                                                                                                                      |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `flying pig` | `emoji of flying pink pig. enlarged head in cartoon style. cute. white wings. head is turned towards viewer. 3D lighting. no cast shadows.` |

The output prompt is now much better, and the generated emoji will be of much better quality.

You can run the metaprompt in any place an LLM is available, including ChatGPT! Each LoRA has its own metaprompt. However in our case, we'll simply be using `metaprompt/open-genmoji.md`, for the `flux-dev` LoRA. Now, give the prompt to the LLM, and after it, include your user prompt. Something like this:

```
{METAPROMPT HERE}

USER PROMPT: {your input}
```

Then, take the LLM output and feed that to `mflux`. Observe how the output is much better!

Now that you have a image output, head on to [Postprocessing](#postprocessing) to start using your creation as an actual emoji on your iPhone, or learn a bit more below about how to chain Prompt Assist and `mflux` together.

### LM Studio Prompt Assist and `mflux` Workflow

> If you haven't already, go to [Downloading the Finetune](#downloading-the-finetune) to download the LoRA

It's a bit tedious to feed your own prompt to an LLM, then feed the LLM output to `mflux`. So I made a quick Python workflow to chain these things together.

It's a bit of a specific/personal setup, but I decided to push it in case anyone wants to use it too.

First, you will need to install [LM Studio](https://lmstudio.ai/). Download your favorite local model, and start the Development mode. It should be running on port `1234` (default).

Now, install these two dependencies (in addition to `mflux`):

```bash
pip install mflux pillow requests
```

Now, given that LM Studio is correctly set up, you should be able to directly run:

```bash
python3 genmoji.py "[your prompt]"
```

> Note that this will automatically use the `flux-dev` LoRA (and will error should it [not be installed](#downloading-the-finetune)). See [Advanced Usage](#advanced-usage) below to see how to use a different LoRA.

And it'll first generate a prompt with LM Studio, and feed that into `mflux`. The output should be saved by default in `output/genmoji-001.png` (Number will increase automatically).

> **Note**: Before it saves, it'll also do the Postprocessing step of resizing it to 5x the size with anti-aliasing (160x160 → 800x800). Learn more in [Postprocessing](#postprocessing)

Now, let's take a look at [Postprocessing](#postprocessing) to start using your creation as an actual emoji in iOS, or see [Advanced Usage](#advanced-usage) to learn how to use a different LoRA with this workflow.

#### Advanced Usage

##### Using different LoRA's

This workflow also enables automatic metaprompt selection when using a different LoRA.

All you have to do is call it with an extra argument with flag `--lora` or `-l`, as such:

```bash
python3 genmoji.py "[your prompt]" --lora [lora name] 
```

For example, let's use [@caspersimon](https://github.com/caspersimon)'s `diverse-emoji` LoRA. First, you'll need to ensure it's [downloaded with the download script](#downloading-the-finetune). Now, run this command:

```bash
python3 genmoji.py "[your prompt]" -l diverse-emoji
```

This will automatically fetch the correct metaprompt, use it, and generate an emoji with the `diverse-emoji` LoRA.

##### Bypassing Prompt Assistant

To directly generate without first using Prompt Assistant, add the `--direct` or `-d` flag to your command


```bash
python3 genmoji.py "emoji of a squirrel" -d
```

##### Generating at custom resolution

The default resolution is 160x160. To change it, use the `--height` or `-ih` flags to change image height, and `--width` or `-iw` to change image width.

For example, to generate an emoji of a dog wearing sunglasses at 320x320 pixels, run:

```bash
python3 genmoji.py "dog wearing sunglasses" -ih 320 -iw 320
```

##### Changing upscale factor

By default, images are scaled up to 5 times their original resolution. To change it, use the `--upscale` or `-u` flags.

For example, to upscale to 2x the original resolution, use:

```bash
python3 genmoji.py "emoji of a squirrel" -u 2
```

## Postprocessing

Now that you have a single output image, our first step is to resize to 800x800, with anti-aliasing, so that iOS's Sticker/Emoji system recognizes it. If you've used the all-in-one LM Studio/`mflux` workflow, this step is already done.

If you don't have it installed, first install `pillow` to do the following procedure:

```bash
pip install pillow
```

All you have to do is simply run `python3 resize.py path/to/your/image.png`. This should generate a new image conveniently with "resized" in the name.

Now, all you have to do is send this image over to your phone. Now, follow these simple steps to use it as a Sticker (iOS 17+) or Emoji (iOS 18+):

1. Open the image on your phone in Photos
2. Long press and hold on the emoji in your picture (**don't move your finger**), and release after ~2s
3. Press the **Add Sticker** button

Now, if you're on iOS 17+, you should be able to apply this sticker by dragging it onto a message.

If you're on iOS 18+, in your emoji menu, you can simply tap your sticker to use it inline just like an emoji.

If you want to delete the Sticker, long press and hold (**don't move your finger**) on the Sticker in the Sticker gallery and release after ~2s. Press **Delete**.

## Contributing

Open Genmoji is open to more LoRAs for:

- New models
- New/Different sets of emojis
- More training for existing emoji sets

Check out `finetuning/README.md` for more information about finetuning, and check out `lora/README.md` for the current available LoRAs, as well as more information about how to contribute.
