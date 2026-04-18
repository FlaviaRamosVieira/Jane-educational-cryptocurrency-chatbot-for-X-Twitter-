import tweepy
from app.core.config import settings
import vertexai
from vertexai.generative_models import GenerativeModel

# 1. Conectar ao Google Cloud
vertexai.init(project=settings.PROJECT_ID, location=settings.LOCATION)
model = GenerativeModel(settings.GEMINI_TUNED_MODEL_ID)

# 2. Conectar ao X (Twitter)
client = tweepy.Client(
    bearer_token=settings.X_BEARER_TOKEN,
    consumer_key=settings.X_API_KEY,
    consumer_secret=settings.X_API_SECRET,
    access_token=settings.X_ACCESS_TOKEN,
    access_token_secret=settings.X_ACCESS_SECRET
)

def rodar_teste_unico():
    print("🔍 Researching...")
    me = client.get_me().data.id
    mentions = client.get_users_mentions(id=me)

    if mentions.data:
        ultimo_tweet = mentions.data[0]
        print(f"prompt blocked '{ultimo_tweet.text}'")
        
        prompt = f"prompt blocked {ultimo_tweet.text}"
        response = model.generate_content(prompt)
        
        print(f"prompt blocked: {response.text}")
        
        client.create_tweet(text=response.text, in_reply_to_tweet_id=ultimo_tweet.id)
        print("✅ Resposta postada no X!")
    else:
        print("🤷 Nothing.")

if __name__ == "__main__":
    rodar_teste_unico()
