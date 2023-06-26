import pandas as pd
import streamlit as st

# DEFINIR NOTAS

TONES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def generate_scale(tone, intervals):
    notes = TONES * 2
    start = notes.index(tone)
    end = start + len(intervals)
    scale = [notes[start]]
    for i in intervals:
        start += i
        scale.append(notes[start])
    return scale


def show_scale_page():
    st.write("# Generador de Escalas")

    SCALE_FORMULAS = {
        "Mayor": [2, 2, 1, 2, 2, 2, 1],
        "Menor": [2, 1, 2, 2, 1, 2, 2],
        "Menor armónica": [2, 1, 2, 2, 1, 3, 1],
        "Menor melódica (ascendente)": [2, 1, 2, 2, 2, 2, 1],
        "Menor natural": [2, 1, 2, 2, 1, 2, 2],
        "Dórica": [2, 1, 2, 2, 2, 1, 2],
        "Frigia": [1, 2, 2, 2, 1, 2, 2],
        "Lydian": [2, 2, 2, 1, 2, 2, 1],
        "Mixolidia": [2, 2, 1, 2, 2, 1, 2],
        "Locria": [1, 2, 2, 1, 2, 2, 2],
        "Pentatonica mayor": [2, 2, 3, 2, 3],
        "Pentatonica menor": [3, 2, 2, 3, 2],
        "Blues": [3, 2, 1, 1, 3, 2],
        "Disminuida (M-T)": [1, 2, 1, 2, 1, 2, 1, 2],
        "Disminuida (T-M)": [2, 1, 2, 1, 2, 1, 2, 1],
        "de tonos enteros": [2, 2, 2, 2, 2, 2],
        "Augmentada": [3, 1, 3, 1, 3, 1],
        "Armónica doble": [1, 3, 1, 2, 1, 3, 1],
        "Napolitana menor": [1, 2, 2, 2, 1, 3, 1],
        "Napolitana mayor": [1, 2, 2, 2, 2, 2, 1],
        "Mayor armónica": [2, 2, 1, 2, 1, 3, 1],
        "Alterada": [1, 2, 1, 2, 2, 2, 2]
    }

    ADDITIONAL_SCALE_FORMULAS = {
        "Gitana Húngara": [2, 1, 3, 1, 1, 2, 2],
        "Persa": [1, 3, 1, 1, 2, 3, 1],
        "Árabe": [2, 2, 1, 1, 2, 2, 2],
        "Japonesa": [1, 4, 2, 1, 4],
        "Enigmática": [1, 3, 2, 2, 2, 1, 1],
        "Española 8 Tonos": [1, 2, 1, 1, 1, 2, 2, 2],
        "Bebop Dominante": [2, 2, 1, 2, 2, 1, 1, 1],
        "Bebop Mayor": [2, 2, 1, 2, 1, 1, 2, 1],
        "Bebop Menor": [2, 1, 2, 2, 1, 1, 2, 1],
        "Pentatonica Dominante": [2, 2, 3, 3, 2],
        "Blues b5": [3, 2, 1, 1, 1, 2, 2],
        "Blues": [3, 2, 1, 1, 1, 3, 1],
        "Pentatónica mayor b6": [2, 2, 3, 1, 4],
        "Pentatónica menor mayor": [3, 2, 2, 1, 4],
        "Menor armónica b6": [2, 1, 2, 2, 1, 2, 2],
        "Dórica b2": [1, 2, 2, 2, 1, 2, 2],
        "Lidia Aumentada": [2, 2, 2, 2, 1, 2, 1],
        "Lidia b7": [2, 2, 2, 1, 2, 1, 2],
        "Mixolidia b13": [2, 2, 1, 2, 1, 2, 2],
        "Locria natural 2": [2, 1, 2, 1, 2, 2, 2],
        "Super Locria": [1, 2, 1, 2, 2, 2, 2],
        "Hindú": [2, 2, 1, 2, 1, 2, 2],
        "Jónica Aumentada": [2, 2, 2, 1, 2, 2, 1],
        "Dórica #4": [2, 1, 3, 1, 2, 2, 1]
    }

    escalas = list(SCALE_FORMULAS.keys()) + list(ADDITIONAL_SCALE_FORMULAS.keys())

    tone = st.sidebar.selectbox("Elige un tono", TONES)
    scale_type = st.sidebar.selectbox("Elige un tipo de escala", escalas)

    if scale_type in SCALE_FORMULAS:
        scale_formula = SCALE_FORMULAS[scale_type]
    else:
        scale_formula = ADDITIONAL_SCALE_FORMULAS[scale_type]

    scale = generate_scale(tone, scale_formula)
    scale_text = ", ".join(scale)
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(f"La escala {scale_type} de {tone} es:")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.markdown(f"<p style='font-size:28px;line-height:1.5;'><strong>{scale_text}</strong></p>", unsafe_allow_html=True)

...

if __name__ == "__main__":
    page = st.sidebar.selectbox("Elige una página", ["Progresiones modales", "Funcionalidad 2", "Generador de Escalas"])
    if page == "Progresiones modales":
        show_modal_chord_page()
    elif page == "Funcionalidad 2":
        pass
    elif page == "Generador de Escalas":
        show_scale_page()
