import streamlit as st
import os
# from langchain_openai import ChatOpenAI

def pageChatbot(name, caract):

    # os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
    # llm = ChatOpenAI(model='gpt-4o-mini')

    st.title(f'👋 Conversa com {name}')
    st.text_input('Digite sua mensagem aqui')