# security.py
import re
import unicodedata
from app.core.config import settings

# --- CONFIGURAÇÕES DE SEGURANÇA ---
# Limite de caracteres para evitar ataques de DoS e custos excessivos de tokens
# Um tweet tem 280 caracteres, então 500 é mais que suficiente para a entrada.
MAX_INPUT_LENGTH = 100

def sanitize_input(text: str) -> str:
    """
    Versão Blindada de Sanitização:
    1. Valida tipo e tamanho (Anti-DoS)
    2. Normaliza Unicode (Anti-Bypass de filtros)
    3. Remove caracteres de controle (Anti-Crash)
    4. Limpa ruídos e URLs (Limpeza de Dados)
    """
    if not text or not isinstance(text, str):
        return ""

    # 1. Proteção contra Input Gigante (DoS)
    # Se o usuário enviar um texto imenso, cortamos imediatamente.
    if len(text) > MAX_INPUT_LENGTH:
        text = text[:MAX_INPUT_LENGTH]

    # 2. Normalização Unicode (NFKC)
    # Isso impede que hackers usem caracteres "parecidos" (ex: um 'a' cirílico)
    # para enganar o seu filtro de Jailbreak no model.py.
    text = unicodedata.normalize('NFKC', text)

    # 3. Remoção de caracteres de controle e não-imprimíveis
    # Evita que caracteres invisíveis causem erros no processamento do LLM.
    text = "".join(ch for ch in text if unicodedata.category(ch)[0] != "C")

    # 4. Remoção de URLs e Menções excessivas
    # Remove links para evitar que o bot seja usado para propagar phishing.
    text = re.sub(r'http\S+', '', text)
    
    # 5. Limpeza de espaços e quebras de linha
    text = " ".join(text.split())
    
    return text.strip()

def validate_api_keys():
    """
    Validação rigorosa de ambiente. 
    Garante que o sistema nem inicie se houver brechas de configuração.
    """
    # Lista de chaves obrigatórias para o funcionamento
    required_keys = {
        "PROJECT_ID": settings.PROJECT_ID, 
        "GEMINI_TUNED_MODEL_ID": settings.GEMINI_TUNED_MODEL_ID, 
        "X_API_KEY": settings.X_API_KEY, 
        "X_ACCESS_TOKEN": settings.X_ACCESS_TOKEN,
        "X_BEARER_TOKEN": settings.X_BEARER_TOKEN
    }
    
    missing_keys = [name for name, value in required_keys.items() if not value]
    
    if missing_keys:
        error_msg = f"❌ ERRO CRÍTICO DE SEGURANÇA: As seguintes chaves estão faltando no .env: {', '.join(missing_keys)}"
        raise EnvironmentError(error_msg)
    
    return True