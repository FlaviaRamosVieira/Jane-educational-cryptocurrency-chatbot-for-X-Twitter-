from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)

def get_professor_prompt():
    system_msg = SystemMessagePromptTemplate.from_template("prompt blocked")
    
    chat_history = MessagesPlaceholder(variable_name="chat_history")
    human_msg = HumanMessagePromptTemplate.from_template("{input}")
    
    return ChatPromptTemplate.from_messages([system_msg, chat_history, human_msg])
