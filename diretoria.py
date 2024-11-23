import streamlit as st
import json

def carregar_atualizacoes():
    try:
        with open('atualizacoes.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"presencas": [], "jogo_confirmado": False}

def salvar_atualizacoes(atualizacoes):
    with open('atualizacoes.json', 'w') as f:
        json.dump(atualizacoes, f)

def show():
    st.title("Diretoria")
    
    atualizacoes = carregar_atualizacoes()

    # Disparar lista de presença
    if st.button("Disparar Lista de Presença"):
        st.info("Lista de presença enviada via WhatsApp!")  # Placeholder para integração futura

    # Registro de presença
    st.header("Registro de Presença")
    jogador = st.text_input("Nome do Jogador")
    if st.button("Confirmar Presença"):
        atualizacoes["presencas"].append(jogador)
        salvar_atualizacoes(atualizacoes)
        st.success(f"Presença de {jogador} confirmada!")
    
    # Confirmar jogo
    if st.button("Confirmar Jogo"):
        atualizacoes["jogo_confirmado"] = True
        salvar_atualizacoes(atualizacoes)
        st.success("Jogo confirmado!")

    st.write("Jogadores confirmados:", atualizacoes["presencas"])
    st.write("Jogo confirmado:", atualizacoes["jogo_confirmado"])