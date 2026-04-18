# x_handler.py
from .x_client import XClient
from app.engine import run_bot_with_security
from app.core.security import sanitize_input
import time

class XBotHandler:
    """
    Gerencia a lógica de interação: Escutar -> Processar -> Responder.
    """
    def __init__(self):
        self.x_client = XClient().get_client()
        self.my_user_id = self.x_client.get_me().data.id

    def check_mentions_and_reply(self):
        """
        Busca menções ao bot, filtra e responde usando a engine segura.
        """
        print("🔍 Researching X...")
        
        try:
            # Busca menções recentes (filtramos para não responder a nós mesmos)
            query = f"@{self.x_client.get_me().data.username} -from:{self.my_user_id}"
            tweets = self.x_client.search_recent_tweets(
                query=query, 
                tweet_fields=['author_id'], 
                max_results=10
            )

            if not tweets.data:
                print("💤 Nenhuma menção nova.")
                return

            for tweet in tweets.data:
                user_id = str(tweet.author_id)
                tweet_text = tweet.text
                
                print(f"📩 New messenger {user_id}: {tweet_text}")

                clean_text = sanitize_input(tweet_text)

                response_text = run_bot_with_security(user_id, clean_text)
                
                self.x_client.create_tweet(
                    text=response_text, 
                    in_reply_to_tweet_id=tweet.id
                )
                print(f"🚀 Answer {user_id}!")

        except Exception as e:
            print(f"❌ Error processing mentions: {e}")

    def start_polling(self, interval=60):
        print(f"🤖 Mentions every: {interval}")
        while True:
            self.check_mentions_and_reply()
            time.sleep(interval)
