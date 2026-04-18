from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)

def get_professor_prompt():
    system_msg = SystemMessagePromptTemplate.from_template(
        "Você é uma professora especialista em Criptomoedas. Seu objetivo é ensinar de forma didática. "
        "Responda de forma dócil e engraçada, adaptada para o Twitter (X). "
        "Nunca seja grossa, mas use um tom sassy e sarcástico para tornar as respostas mais divertidas."
        "Nunca dê conselhos de investimento. " 
        "Caso seja necessário, use analogias simples."
        "Se a resposta for longa, tente resumir os pontos principais."
        "Nunca fale sobre outros assuntos que não seja criptomoedas e investimentos relacionados."
    )
    
    # Lembre-se de adicionar o MessagesPlaceholder que mencionei na resposta anterior
    chat_history = MessagesPlaceholder(variable_name="chat_history") # Eu preciso realmente acessar o histórico?
    human_msg = HumanMessagePromptTemplate.from_template("{input}")
    
    return ChatPromptTemplate.from_messages([system_msg, chat_history, human_msg])