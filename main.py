import streamlit as st
import os
import pages.config as pgConfig
import pages.chatbot as pgChat

st.set_page_config(page_title="FriendIA")

if 'sexo_escolhido' not in st.session_state:
    st.session_state.sexo_escolhido = "NDA"
    st.session_state.nome = ""
    st.session_state.caract = ""

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
        .st-emotion-cache-mptgkq, .exotz4b0{
            width: 100%;
        }
        .st-emotion-cache-janbn0{
            padding: 15px !important;
            text-align: start;
        }
        h1{
            margin-bottom: 30px;
        }
        .stChatMessage{
            background-color: #5555;    
        }
        .st-emotion-cache-4oy321{
            flex-direction: row-reverse;  
            text-align: end; 
        }
        .st-emotion-cache-18qnold{
            margin-right: 15px;    
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


