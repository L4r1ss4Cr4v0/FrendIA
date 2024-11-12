import streamlit as st
import os
from langchain_openai import ChatOpenAI
import pages.config as pgConfig
import pages.chatbot as pgChatbot

st.set_page_config(page_title='FriendIA')

page = "main"

name = []

st.markdown("""
    <style>
        .st-emotion-cache-13k62yr{
            text-align: center;
        }
        .stSidebar, .st-emotion-cache-1f3w014, st-emotion-cache-hzo1qh eczjsme5, .st-emotion-cache-1wqrzgl, .st-emotion-cache-hzo1qh, eczjsme18{
            display: none;
        }

    </style>
        """, 
    unsafe_allow_html=True)

if page == "main":
    st.title('Converse com seu FriendIA!')
    st.subheader('Crie o seu amigo virtual! Personalize-o do jeito que quiser')
    if st.button('Vamos começar!'):
        pgConfig.PageConfiguration(name)



