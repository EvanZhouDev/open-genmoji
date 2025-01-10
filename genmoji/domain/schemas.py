from pydantic import BaseModel
from typing import Optional


class DownloadModelRequest(BaseModel):
    huggingface_repo: str
    model_name: str


class GenerationRequest(BaseModel):
    prompt: str
    lora: Optional[str] = "flux-dev"
    llm_model: Optional[str] = "llama3.1:latest"
    direct: Optional[bool] = False
    height: Optional[int] = 160
    width: Optional[int] = 160
    upscale_factor: Optional[int] = 5