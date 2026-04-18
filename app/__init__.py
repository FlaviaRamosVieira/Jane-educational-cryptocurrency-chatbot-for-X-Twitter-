# app/__init__.py

"""
Este arquivo transforma a pasta 'app' em um pacote Python e atua como uma Fachada (Facade).
Ele expõe as principais funcionalidades de api, core e engine para simplificar os imports
no arquivo principal (main.py).
"""

# 1. Importações do módulo API (Comunicação com o X)
from .api import XBotHandler

# 2. Importações do módulo CORE (Configurações e Segurança Técnica)
from .core.config import settings
from .core.security import validate_api_keys, sanitize_input

# 3. Importações do módulo ENGINE (Cérebro, Memória e Segurança Semântica)
from .engine import run_bot_with_security

# Definimos o __all__ para controlar o que é exportado ao fazer "from app import *"
__all__ = [
    "XBotHandler", 
    "settings", 
    "validate_api_keys", 
    "sanitize_input", 
    "run_bot_with_security"
]