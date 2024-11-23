import streamlit as st
import time

def show():
    st.title("Jogo")

    # Registro de presença
    st.header("Registro de Presença")
    jogador = st.text_input("Nome do Jogador")
    if st.button("Registrar Chegada"):
        st.success(f"Chegada de {jogador} registrada!")

    # Formação de time
    st.header("Formação de Time")
    time_azul = st.multiselect("Time Azul", ["Jogador 1", "Jogador 2", "Jogador 3", "Jogador 4", "Jogador 5"])
    time_amarelo = st.multiselect("Time Amarelo", ["Jogador 6", "Jogador 7", "Jogador 8", "Jogador 9", "Jogador 10"])

    # Início da partida
    st.header("Partida")
    if 'tempo_jogo' not in st.session_state:
        st.session_state.tempo_jogo = 0
        st.session_state.rodando = False
        st.session_state.placar_azul = 0
        st.session_state.placar_amarelo = 0

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Iniciar/Pausar"):
            st.session_state.rodando = not st.session_state.rodando

    with col2:
        if st.button("Finalizar"):
            st.session_state.rodando = False
            st.session_state.tempo_jogo = 0

    with col3:
        tempo = st.empty()

    # Placar
    col4, col5 = st.columns(2)
    with col4:
        st.subheader(f"Azul: {st.session_state.placar_azul}")
    with col5:
        st.subheader(f"Amarelo: {st.session_state.placar_amarelo}")

    # Registro de Gol
    time_gol = st.radio("Time que marcou o gol", ["Azul", "Amarelo"])
    jogador_gol = st.selectbox("Jogador que marcou o gol", time_azul + time_amarelo)
    teve_assistencia = st.checkbox("Teve assistência?")
    jogador_assistencia = st.selectbox("Jogador que fez a assistência", time_azul + time_amarelo) if teve_assistencia else None

    if st.button("Registrar Gol"):
        if time_gol == "Azul":
            st.session_state.placar_azul += 1
        else:
            st.session_state.placar_amarelo += 1
        st.success(f"Gol registrado para o time {time_gol}!")

    # Lógica do cronômetro
    while st.session_state.rodando:
        time.sleep(1)
        st.session_state.tempo_jogo += 1
        minutos = st.session_state.tempo_jogo // 60
        segundos = st.session_state.tempo_jogo % 60
        tempo.text(f"{minutos:02d}:{segundos:02d}")
        
        if st.session_state.tempo_jogo >= 900 and not st.session_state.rodando:  # 15 minutos
            st.warning("Tempo regulamentar encerrado. Contando acréscimos.")

    tempo.text(f"{st.session_state.tempo_jogo // 60:02d}:{st.session_state.tempo_jogo % 60:02d}")