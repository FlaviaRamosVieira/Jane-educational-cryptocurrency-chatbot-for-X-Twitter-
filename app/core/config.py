# Leitura do .env e configurações do Vertex AI


from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    # --- Configurações do Google Vertex AI ---
    PROJECT_ID: str
    LOCATION: str = "us-central1"
    GEMINI_TUNED_MODEL_ID: str
    
    # --- Configurações do Model Armor (Google Cloud) ---
    # Se você criou um filtro no Model Armor, coloque o ID dele aqui
    MODEL_ARMOR_FILTER_ID: Optional[str] = None

    # --- Configurações da API do X (Twitter) ---
    X_API_KEY: str
    X_API_SECRET: str
    X_ACCESS_TOKEN: str
    X_ACCESS_SECRET: str
    X_BEARER_TOKEN: str

    # Configuração para ler o arquivo .env
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# Instanciamos o settings para ser usado em todo o projeto
settings = Settings()