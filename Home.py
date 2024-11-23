import streamlit as st
import jogo
import ranking
import jogadores
import diretoria
import membros  # Certifique-se de importar o módulo membros

# Configuração da página
st.set_page_config(page_title="App de Futebol", page_icon="⚽", layout="wide")

# Título do aplicativo
st.title("App de Futebol ⚽")

# Menu de navegação
menu = st.sidebar.selectbox("Escolha uma opção", ["Home", "Jogo", "Ranking", "Jogadores", "Diretoria", "Membros"])

# Lógica de navegação
if menu == "Home":
    st.write("Bem-vindo ao App de Futebol!")
    st.write("Use o menu lateral para navegar entre as opções.")
elif menu == "Jogo":
    jogo.show()
elif menu == "Ranking":
    ranking.show()
elif menu == "Jogadores":
    jogadores.show()
elif menu == "Diretoria":
    diretoria.show()
elif menu == "Membros":
    membros.show()  # Certifique-se de que não há erros de indentação ou de sintaxe