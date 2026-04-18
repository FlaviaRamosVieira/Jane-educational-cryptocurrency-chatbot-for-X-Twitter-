from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):

    PROJECT_ID: str
    LOCATION: str = "us-central1"
    GEMINI_TUNED_MODEL_ID: str
    
    MODEL_ARMOR_FILTER_ID: Optional[str] = None

    X_API_KEY: str
    X_API_SECRET: str
    X_ACCESS_TOKEN: str
    X_ACCESS_SECRET: str
    X_BEARER_TOKEN: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
