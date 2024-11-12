import streamlit as st
from langchain_openai import ChatOpenAI
import pages.chatbot as pgChatbot

def PageConfiguration(name):

    with st.container(border=True):
        st.subheader('Escolha o sexo')
        col1, col2 = st.columns(2)
        with col1:
            st.button('🧑', key='homem')
        with col2:
            st.button('👩', key='mulher')

    with st.form(key='dados'):
        name = st.text_input('Digite o nome do seu FriendIA').split()
        caract = st.text_area('Como você quer que ele/ela seja?', placeholder='Ex.: Ele é um bombeiro dedicado com 1.80m de altura...')
        
        if st.form_submit_button('Tudo OK!'):
            pgChatbot.pageChatbot(name)