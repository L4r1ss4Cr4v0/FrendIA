import streamlit as st
import openai

def pageChatbot():
    
    openai.api_key = st.secrets['OPENAI_API_KEY']

    st.title(f'👋 Conversa com {st.session_state.nome[0]}')

    # Setando as variavéis
    if st.session_state.sex == "man":
        avatar = "👦🏻"
    else:
        avatar = "👧🏻"

    if "chat_model" not in st.session_state:
        st.session_state.chat_model = "gpt-4o-mini"

    # Inicializando o modelo do chat
    
    user_response = st.chat_input('Digite sua mensagem aqui')

    # Criando o historico
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Colocando a conversa na tela
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_response is not None or "":

        with st.chat_message("user"):
            st.markdown(user_response)
            
        st.session_state.chat_history.append({"role": "user", "content": user_response})

        # Criando a resposta 

        with st.chat_message(avatar):
            message_placeholder = st.empty()
            full_response = ""
            if "first_message" not in st.session_state:
                st.session_state.first_message = True            
                for response in openai.chat.completions.create(
                    model=st.session_state.chat_model,
                    messages=[
                        {"role": "developer", "content": f"You are a {st.session_state.sex} called {st.session_state.name}. You are also a {st.session_state.caract}. Answer all the messages in this character."},
                        {"role": message["role"], "content": message["content"]}
                        for message in st.session_state.chat_history
                    ],
                    stream=True,
                    max_completion_tokens=200,
                ):                    
                    full_response += response.choices[0].delta.get("content", "")
                    message_placeholder.markdown(full_response + " ")
                    message_placeholder.markdown(full_response)
            else:            
                for response in openai.chat.completions.create(
                    model=st.session_state.chat_model,
                    messages=[
                        {"role": message["role"], "content": message["content"]}
                        for message in st.session_state.chat_history
                    ],
                    stream=True,
                    max_completion_tokens=200,
                ):
                    full_response += response.choices[0].delta.get("content", "")
                    message_placeholder.markdown(full_response + " ")
                    message_placeholder.markdown(full_response)

            st.session_state.chat_history.append({"role": avatar, "content": full_response})



    