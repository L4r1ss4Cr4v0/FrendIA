import streamlit as st
import pages.chatbot as pgChat

def PageConfiguration():

    placeholder = st.empty()

    if 'check' in st.session_state:
        placeholder.empty()
        pgChat.pageChatbot()

    else:
        with placeholder.container(border=True):
            st.subheader('Escolha o sexo')
            col1, col2 = st.columns(2)
            with col1:
                if st.button('🧑', key='homem'):
                    st.session_state.sex = 'homem'
            with col2:
                if st.button('👩', key='mulher'):
                    st.session_state.sex = 'mulher'
            if st.session_state.sex != "NDA":
                st.text(f"Sexo escolhido: {st.session_state.sex}")

            st.session_state.name = st.text_input('Digite o nome do seu FriendIA').split()

            st.session_state.caract = st.text_area('Como você quer que ele/ela seja?', placeholder='Ex.: Ele é um bombeiro dedicado com 1.80m de altura...')

            if st.session_state.sex != 'NDA' and st.session_state.name != "" and st.session_state.caract != "":

                if st.button("Passar (clique 2x)"):
                    st.session_state.check = True
