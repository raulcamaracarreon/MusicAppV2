import streamlit as st
from blues_page import show_blues_page
from modal_chord_page import show_modal_chord_page
from scale_page import show_scale_page

# Definir las páginas en tu aplicación
paginas = {
    "Progresiones de blues": show_blues_page,
    "Progresiones modales de acordes": show_modal_chord_page,
    "Compendio de Escalas": show_scale_page
    # Aquí puedes agregar más páginas según lo necesites...
}

# Crear un menú de selección en la barra lateral
pagina_seleccionada = st.sidebar.radio("Selecciona una función: ", list(paginas.keys()))

# Mostrar la página seleccionada
paginas[pagina_seleccionada]()

# Añade varias líneas vacías
for _ in range(7):
        st.sidebar.write("")

    # Añade tu leyenda
st.sidebar.markdown('<p style="font-size: 10px;color:gray;"><b>Hipnonauta</b></p>', unsafe_allow_html=True)
