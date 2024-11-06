import streamlit as st 

MENSAGENS_EXEMPLO = [
    ('user', 'Olá'),
    ('Padilha', 'Tudo bem?'),
    ('user', 'Tudo não'),
]

def pagina_chat(): 
    st.header('🔮 Bem-vindo ao Oráculo de Padilha', divider=True)
    
    mensagens = st.session_state.get('mensagens', MENSAGENS_EXEMPLO)
    for mensangem in mensagens:
        chat = st.chat_message(mensangem[0])
        chat.markdown(mensangem[1])
        
    input_usuario = st.chat_input('Fale com Maria Padilha')
    if input_usuario:
        mensagens.append(('user', input_usuario))
        
        st.session_state['mensagens'] = mensagens
        st.rerun()
        

def sidebar():
    tabs = st.tabs(['Adicione Arquivos','Escolha um modelo de Padilha'])        
        
        
def main():
    pagina_chat()
    with st.sidebar:
        sidebar()


if __name__ == '__main__':
    main()