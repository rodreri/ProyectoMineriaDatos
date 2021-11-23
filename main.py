from os import write
from awesome_streamlit.shared.components import write_page
import streamlit as st

import awesome_streamlit as ast
import scripts.acercade
import scripts.edam
import scripts.hola

PAGES = {
    "Acerca de": scripts.acercade,
    "Análsis Exploratorio de Datos": scripts.edam,
    "Hola": scripts.hola,
}

def main():
    """Index"""
    st.sidebar.title("Menú")
    selection = st.sidebar.radio("Ir a", list(PAGES.keys()))

    st.sidebar.title("Contacto")
    st.sidebar.success("""
        **Alumno:** Erick Rodrigo Minero Pineda
        **Correo:** rodreri@gmail.com
    """)

    page = PAGES[selection]

    with st.spinner(f"Cargando {selection} ..."):
        ast.shared.components.write_page(page)


if __name__ == "__main__":
    main()