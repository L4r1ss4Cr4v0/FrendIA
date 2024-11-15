import streamlit as st
import os
import pages.config as pgConfig
import pages.chatbot as pgChat

st.set_page_config(page_title='FriendIA')

if 'sexo_escolhido' not in st.session_state:
    st.session_state.sexo_escolhido = "NDA"
if 'inicio' not in st.session_state:
    st.session_state.inicio = False

st.markdown("""
    <style>
        .st-emotion-cache-13k62yr {
            text-align: center;
        }
        .stSidebar, .st-emotion-cache-1f3w014, st-emotion-cache-hzo1qh eczjsme5, 
        .st-emotion-cache-1wqrzgl, .st-emotion-cache-hzo1qh, eczjsme18 {
            display: none;
        }
    </style>
    
    """, 
    unsafe_allow_html=True)

placeholder = st.empty()

if not st.session_state.inicio:
    with placeholder.container():
        st.title('Converse com seu FriendIA!')
        st.subheader('Crie o seu amigo virtual! Personalize-o do jeito que quiser')
        if st.button('Vamos começar!'):
            st.session_state.inicio = True  
            placeholder.empty()  

if st.session_state.inicio:
   pgConfig.PageConfiguration()


