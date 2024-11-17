import streamlit as st
import pages.chatbot as pgChat

# def colorido():
#     st.markdown("""
#         <style>
#             button{
#                 background-color: red !important;    
#             }
#         </style>
#         """, 
#         unsafe_allow_html=True)

def PageConfiguration():
    with st.empty().container(border=True):
        st.subheader('Escolha o sexo')
        col1, col2 = st.columns(2)
        with col1:
            if st.button('🧑', key='homem'):
                st.session_state.sexo_escolhido = 'Masculino'
                # colorido()
        with col2:
            if st.button('👩', key='mulher'):
                st.session_state.sexo_escolhido = 'Feminino'
                # colorido()
        name = st.text_input('Digite o nome do seu FriendIA').split()
        caract = st.text_area('Como você quer que ele/ela seja?', placeholder='Ex.: Ele é um bombeiro dedicado com 1.80m de altura...')
        if st.session_state.sexo_escolhido != 'NDA' and name != "" and caract != "":
            if st.button("Passar"):
                st.empty().empty()
                pgChat.pageChatbot(name, caract)