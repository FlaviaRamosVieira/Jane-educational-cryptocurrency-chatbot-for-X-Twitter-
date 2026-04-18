# chain.py
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from app.engine.model import get_llm, validate_input_security # Importamos a segurança aqui
from app.engine.prompts import get_professor_prompt

# Dicionário para armazenar o histórico (Lembre-se: em produção, use Redis/MongoDB)
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

def create_bot_chain():
    """
    Define a estrutura da Chain (LCEL).
    Esta função apenas 'monta' o motor do bot.
    """
    llm = get_llm()
    prompt = get_professor_prompt()

    # Base: Prompt -> LLM
    base_chain = prompt | llm

    # Adicionamos a gestão de histórico
    chain_with_history = RunnableWithMessageHistory(
        base_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
    )
    return chain_with_history

# --- ACRÉSCIMO PARA SEGURANÇA (MODEL ARMOR) ANTES DE RODAR A CHAIN ---

# Instanciamos a chain globalmente para não recriá-la a cada mensagem
bot_chain = create_bot_chain()

def run_bot_with_security(user_id: str, user_input: str):
    """
    Esta é a função principal que será chamada pelo seu integrador do X.
    Ela une Segurança -> Memória -> LLM.
    """
    # 1. Camada de Proteção (Jailbreak)
    is_safe, reason = validate_input_security(user_input)
    
    if not is_safe:
        print(f"⚠️ Segurança: {reason}")
        return "Sinto muito, mas não posso responder a esse tipo de solicitação."

    # 2. Execução da Chain com Histórico
    # O user_id do Twitter entra como session_id
    try:
        response = bot_chain.invoke(
            {"input": user_input}, 
            config={"configurable": {"session_id": user_id}}
        )
        return response.content
    except Exception as e:
        print(f"❌ Erro na Chain: {e}")
        return "Ops, tive um problema técnico. Pode repetir a pergunta? 🤖"