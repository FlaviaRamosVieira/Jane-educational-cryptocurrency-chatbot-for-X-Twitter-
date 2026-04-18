from app import XBotHandler, validate_api_keys, settings

def main():
    print("--- STARTING ---")
    
    try:
        # Valida as chaves do .env
        validate_api_keys()
        print("✅ Validated Settings!")
        
        # Inicia o Handler do X
        bot = XBotHandler()
    
        bot.start_polling(interval=60)
        
    except Exception as e:
        print(f"❌ FAIL: {e}")

if __name__ == "__main__":
    main()
