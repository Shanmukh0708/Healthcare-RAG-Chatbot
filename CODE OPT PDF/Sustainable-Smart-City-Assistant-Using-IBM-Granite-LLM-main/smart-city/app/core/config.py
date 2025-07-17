from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    huggingface_api_key: str = os.getenv("HUGGINGFACE_API_KEY")
    model_id: str = os.getenv("MODEL_ID")

settings = Settings()
