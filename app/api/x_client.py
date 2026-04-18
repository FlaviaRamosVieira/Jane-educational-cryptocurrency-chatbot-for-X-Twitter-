import tweepy
from app.core.config import settings

class XClient:
    """
    Classe responsável por gerenciar a conexão com a API do X (Twitter).
    """
    def __init__(self):
        try:
            # Autenticação usando Tweepy Client (API v2)
            self.client = tweepy.Client(
                bearer_token=settings.X_BEARER_TOKEN,
                consumer_key=settings.X_API_KEY,
                consumer_secret=settings.X_API_SECRET,
                access_token=settings.X_ACCESS_TOKEN,
                access_token_secret=settings.X_ACCESS_SECRET
            )
            print("✅ Conexão com a API do X estabelecida com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao conectar com a API do X: {e}")
            raise e

    def get_client(self):
        return self.client
