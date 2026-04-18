import tweepy
from app.core.config import settings

class XClient:
    def __init__(self):
        try:
            self.client = tweepy.Client(
                bearer_token=settings.X_BEARER_TOKEN,
                consumer_key=settings.X_API_KEY,
                consumer_secret=settings.X_API_SECRET,
                access_token=settings.X_ACCESS_TOKEN,
                access_token_secret=settings.X_ACCESS_SECRET
            )
            print("✅ Connected API!")
        except Exception as e:
            print(f"❌ ERROR API: {e}")
            raise e

    def get_client(self):
        return self.client
