# Note que agora importamos TUDO diretamente de 'app', sem precisar de 'app.api' ou 'app.core'
from app import XBotHandler, validate_api_keys, settings

def main():
    print("--- INICIANDO CHATBOT JANE PROF CRIPTO ---")
    
    try:
        # Valida as chaves do .env
        validate_api_keys()
        print("✅ Configurações validadas!")
        
        # Inicia o Handler do X
        bot = XBotHandler()
        
        # Começa a rodar o bot (checa menções a cada 60 segundos)
        bot.start_polling(interval=60)
        
    except Exception as e:
        print(f"❌ Falha crítica na inicialização: {e}")

if __name__ == "__main__":
    main()