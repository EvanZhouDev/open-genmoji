# Open Genmoji LoRAs

## Downloading LoRAs

LoRA downloads are done through HuggingFace. Run the following Python script in the root `open-genmoji` directory to download a LoRA. The script will give you a list of available LoRAs, what models they use, and a brief description. Choose your favorite!

```bash
# If you're in the lora directory, cd out to root `open-genmoji` folder
cd ../

python3 ./download.py
```

## LoRA List

List of metadata for all Genmoji LoRAs.

| LoRA Name                                                                        | Model Trained | Emojis Used                         | More Info                         |
| -------------------------------------------------------------------------------- | ------------- | ----------------------------------- | --------------------------------- |
| `flux-dev.safetensors`                                                       | Flux.1 Dev    | No Skintone Apple Emoji List (1901) | [View](#flux-devsafetensors)      |
| [`diverse-emoji.safetensors`](https://huggingface.co/caspersimon/Diverse-Emoji/) | Flux.1 Dev    | Complete Apple Emoji list (3770)    | [View](#diverse-emojisafetensors) |

# Contributing a LoRA

Contributing is easy! Here's the simple steps:

1. First, create a LoRA. You can learn how in `README` in the `open-genmoji/finetuning` folder in the root directory.
2. Go ahead and name that LoRA, and submit a PR to the [Open Genmoji HuggingFace](https://huggingface.co/EvanZhouDev/open-genmoji), adding that file.
3. If you would like your model to use a custom metaprompt (for Prompt Assist), you should add that to the `metaprompt` folder. _You do not need a metaprompt. You can choose to use `metaprompt/open-genmoji`_
   
   <details>
     <summary><em>Optional: improving Prompt Assistant consistency by adding conversation history </em> </summary>
     To make outputs of your metaprompt more consistent across different LLM's, you can choose to add example combinations of input and output texts to a JSON file with the same name as your metaprompt.
     
     The file should be structured with a key `"messages"` which has a value containing a list of dictionaries as shown below. 

   **The `content` of the first message (with `"role": "user"`) should include:** 
     * The full metaprompt
     * Two new lines `\n\n`
     * `USER PROMPT: `
     * The user prompt. This can be any non-optimized prompt.
   
   **The `content` of the second message (with `"role": "assistant"`) should include:**
   * Only the optimized prompt.

    You can add multiple examples by repeating this. The file shown below has 2 example prompts and outputs.
    
    ```json
       {
         "messages": [
           { "role": "user", "content": "You are helping create a prompt for a Emoji generation image model. An emoji must be easily interpreted when small so details must be exaggerated to be clear. Your goal is to use descriptions to achieve this.\n\nYou will receive a user description, and you must rephrase it to consist of short phrases separated by periods, adding detail to everything the user provides.\n\nAdd describe the color of all parts or components of the emoji. Unless otherwise specified by the user, do not describe people. Do not describe the background of the image. Your output should be in the format:\n\n```\nemoji of {description}. {addon phrases}. 3D lighting. no cast shadows.\n```\n\nThe description should be a 1 sentence of your interpretation of the emoji.\nThen, you may choose to add addon phrases. You must use the following in the given scenarios:\n\n- \"cute.\": If generating anything that's not an object, and also not a human\n- \"enlarged head in cartoon style.\": ONLY animals\n- \"head is turned towards viewer.\": ONLY humans or animals\n- \"detailed texture.\": ONLY objects\n\nFurther addon phrases may be added to ensure the clarity of the emoji.\n\n\n USER PROMPT: a horse wearing a suit"},
           { "role": "assistant", "content": "emoji of horse in black suit and tie with flowing mane. a strong, confident stallion wearing formal attire for a special occasion. cute. 3D lighting. no cast shadows. enlarged head in cartoon style. head is turned towards viewer." },
           { "role": "user", "content": "You are helping create a prompt for a Emoji generation image model. An emoji must be easily interpreted when small so details must be exaggerated to be clear. Your goal is to use descriptions to achieve this.\n\nYou will receive a user description, and you must rephrase it to consist of short phrases separated by periods, adding detail to everything the user provides.\n\nAdd describe the color of all parts or components of the emoji. Unless otherwise specified by the user, do not describe people. Do not describe the background of the image. Your output should be in the format:\n\n```\nemoji of {description}. {addon phrases}. 3D lighting. no cast shadows.\n```\n\nThe description should be a 1 sentence of your interpretation of the emoji.\nThen, you may choose to add addon phrases. You must use the following in the given scenarios:\n\n- \"cute.\": If generating anything that's not an object, and also not a human\n- \"enlarged head in cartoon style.\": ONLY animals\n- \"head is turned towards viewer.\": ONLY humans or animals\n- \"detailed texture.\": ONLY objects\n\nFurther addon phrases may be added to ensure the clarity of the emoji.\n\n\n USER PROMPT: flying pig"},
           { "role": "assistant", "content": "emoji of flying pink pig. enlarged head in cartoon style. cute. white wings. head is turned towards viewer. 3D lighting. no cast shadows." }
         ]
       }
    ```
   
    **Why does this work?** <br>
    These messages are added to the conversation history with the chatbot. Then, when you submit a new prompt, it is likely to respond in a similar way it did before.
  </details>

4. Next, you'll need to update `info.json` in this directory. Add an entry like such underneath all the other models:

```json
{
	"model": "black-forest-labs/FLUX.1-dev", // HuggingFace path of base model
	"huggingface": "EvanZhouDev/open-genmoji", // Your own HuggingFace repo, optional
	"name": "flux-dev", // The name of your LoRA file
	"metaprompt": "open-genmoji", // The name of your metaprompt file
	"description": "Original Open Genmoji finetune. Trained on Apple Emojis w/o Skin Tone Variants." // Nice and short description of your model (< 100 characters)
}
```

5. Finally, update this file, to let people know what you trained on, how you trained it, etc. Start by adding a row with proper info in the [LoRA List](#lora-list). Then, add a new section below in [Detailed LoRA Description](#detailed-lora-description). The template for it can be found in `LORA_TEMPLATE.md` file in this directory.
6. With all that done, submit a PR to this repository. I'll get back to you as soon as possible.

Thank you for your contribution!

# Detailed LoRA Description

## `flux-dev.safetensors`

**Model Finetuned**: Flux.1 Dev
**Finished Finetuning**: December 25, 2024
**Finetuned By**: Evan Zhou ([@evanzhoudev](https://github.com/evanzhoudev))
**Finetuned On**: M4 Max MacBook Pro (64GB Unified Memory, 40 core GPU)
**Finetuned With**: [SimpleTuner](https://github.com/bghira/SimpleTuner)
**Finetuning Time**: ~10 hours
**Finetuning Steps**: 10,000
**Image Resolution**: 160x160
**Emoji Dataset**: All Apple Emojis as of December 25, 2024, with skin tone variants pruned to reduce training time.

## `diverse-emoji.safetensors`

**Model Finetuned**: Flux.1 Dev
**Finished Finetuning**: December 31, 2024
**Finetuned By**: Julius ([@caspersimon](https://github.com/caspersimon))
**Finetuned On**: M4 Max MacBook Pro (128GB Unified Memory, 40 core GPU)
**Finetuned With**: [SimpleTuner](https://github.com/bghira/SimpleTuner)
**Finetuning Time**: ~20 hours
**Finetuning Steps**: 20,000
**Image Resolution**: 160x160
**Emoji Dataset**: All Apple Emoji as of December 30, 2024.
**Huggingface Link**: [caspersimon/Diverse-Emoji](https://huggingface.co/caspersimon/Diverse-Emoji)
