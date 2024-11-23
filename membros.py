import streamlit as st
import json

def carregar_membros():
    with open('membros.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def show():
    st.title("Gerenciamento de Membros")
    
    # Carregar dados de membros
    membros = carregar_membros()
    
    # Exibição da lista de membros
    st.header("Lista de Membros")
    for membro in membros:
        st.subheader(membro["NOME"])
        st.text(f"Telefone: {membro['TELEFONE']}")
        st.text(f"Apelido: {membro['APELIDO']}")
        st.text(f"Data de Nascimento: {membro['DATA_NASCIMENTO']}")
        st.text(f"Naturalidade: {membro['NATURALIDADE']}")
        st.text(f"Time do Coração: {membro['TIME_CORACAO']}")
        st.text(f"Posição no Jogo: {membro['POSICAO_JOGO']}")
        st.text(f"Data de Filiação: {membro['DATA_FILIACAO']}")
        st.text(f"Tipo de Usuário: {membro['TIPO_USUARIO']}")
        st.markdown("---")

    # Cadastro de Membros (exemplo simplificado)
    st.header("Cadastro de Membros")
    nome = st.text_input("Nome do Novo Membro")
    telefone = st.text_input("Telefone")
    apelido = st.text_input("Apelido")
    data_nascimento = st.text_input("Data de Nascimento")
    naturalidade = st.text_input("Naturalidade")
    time_coracao = st.text_input("Time do Coração")
    posicao_jogo = st.text_input("Posição no Jogo")
    data_filiacao = st.text_input("Data de Filiação")
    senha = st.text_input("Senha", type="password")
    tipo_usuario = st.selectbox("Tipo de Usuário", ["Presidente", "Membro"])

    if st.button("Cadastrar Membro"):
        novo_membro = {
            "Nº": len(membros) + 1,
            "NOME": nome,
            "TELEFONE": telefone,
            "APELIDO": apelido,
            "DATA_NASCIMENTO": data_nascimento,
            "NATURALIDADE": naturalidade,
            "TIME_CORACAO": time_coracao,
            "POSICAO_JOGO": posicao_jogo,
            "DATA_FILIACAO": data_filiacao,
            "SENHA": senha,
            "TIPO_USUARIO": tipo_usuario
        }
        membros.append(novo_membro)
        with open('membros.json', 'w', encoding='utf-8') as f:
            json.dump(membros, f, ensure_ascii=False, indent=4)
        st.success(f"Membro {nome} cadastrado com sucesso!")