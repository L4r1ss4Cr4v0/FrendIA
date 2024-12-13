import streamlit as st
import os
# from langchain_openai import ChatOpenAI

def pageChatbot():

    # os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
    # llm = ChatOpenAI(model='gpt-4o-mini')

    st.title(f'👋 Conversa com {st.session_state.nome[0]}')
    st.text_input('Digite sua mensagem aqui')