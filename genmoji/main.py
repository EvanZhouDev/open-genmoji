import io
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from huggingface_hub import hf_hub_download, login
from PIL import Image
from domain.schemas import DownloadModelRequest, GenerationRequest
from utils.generate_image import generate_image
from utils.llm_utils import list_installed_llms, model_inference
from utils.logger import logger

load_dotenv()

app = FastAPI()
login(token=os.getenv("HF_TOKEN"))


@app.post("/download_model")
async def download_model(input_data: DownloadModelRequest) -> JSONResponse:
    """
    Downloads model from huggingface
    """
    try:
        filename = f"{input_data.model_name}.safetensors"
        hf_hub_download(
            repo_id=input_data.huggingface_repo, filename=filename, local_dir="./lora"
        )
        return JSONResponse(content={"response": f"Download {input_data.model_name} complete"})
    except Exception as e:
        logger.error(f"Error downloading model: {e}")
        logger.exception(e)
        return JSONResponse(content={"response": f"Error downloading model: {e}"}, status_code=500)


@app.get("/installed_img_genmodels")
async def get_installed_img_gen_models() -> JSONResponse:
    """
    Get the list of installed image gen models
    """
    try:
        models = os.listdir("lora/")
        models = [model.replace(".safetensors", "") for model in models if not model.startswith(".") and "safetensors" in model]
        return JSONResponse(content={"models": models})
    except Exception as e:
        logger.error(f"Error listing models: {e}")
        logger.exception(e)
        return JSONResponse(content=f"Error listing models: {e}", status_code=500)


@app.get("/installed_llms")
async def get_installed_llms() -> JSONResponse:
    """
    Get the list of installed llms from ollama
    """
    try:
        return JSONResponse(content={"models": list_installed_llms()})
    except Exception as e:
        logger.error(f"Error listing models: {e}")
        logger.exception(e)
        return JSONResponse(content=f"Error listing models: {e}", status_code=500)


@app.post("/inference")
async def inference(input_data: GenerationRequest) -> StreamingResponse:
    """
    Perform model inference to generate an emoji. Uses Ollama to handle LLM inference for lora prompt generation
    """
    # Check if the lora file exists
    lora_path = f"lora/{input_data.lora}.safetensors"
    if not os.path.exists(lora_path):
        raise HTTPException(
            status_code=404,
            detail=f"Error: LoRA {input_data.lora} is not downloaded. Please run use the /download_model endpoint to download it.")
    
    if input_data.direct:
        user_prompt = input_data.prompt
    else:
        # Get the response from the prompt assistant
        user_prompt = model_inference(
            user_prompt=input_data.prompt,
            model_name=input_data.llm_model
        ).get("message")
        if "i cannot" in user_prompt.lower() or "i can't" in user_prompt.lower():
            logger.warning("Refusal detected from LLM prompt enhancement. Using raw prompt input, generation may be lacking.")
            user_prompt = input_data.prompt
        else:
            logger.info("Prompt Created: " + user_prompt)

    # Generate the image using the response from the prompt assistant
    image = generate_image(user_prompt, input_data.lora, input_data.width, input_data.height)

    output_width, output_height = image.size
    resized_image = image.resize(
        (
            output_width * input_data.upscale_factor,
            output_height * input_data.upscale_factor
        ),
        Image.LANCZOS)

    img_io = io.BytesIO()
    resized_image.save(img_io, 'PNG')
    img_io.seek(0)

    return StreamingResponse(img_io, media_type="image/png")