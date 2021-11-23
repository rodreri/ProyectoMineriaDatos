import streamlit as st

import scripts.eda

PAGES = {
    "Análsis Exploratorio de Datos": scripts.eda
}

def main():
    """Main function of the App"""
    st.set_page_config(layout="wide")
    st.sidebar.title("Menú")
    selection = st.sidebar.radio("Ir a", list(PAGES.keys()))

    st.sidebar.title("Míneria de Datos")
    st.sidebar.info(
        """Proyecto Final 2021-2

Universidad Nacional Autónoma de México

Facultad de Ingeniería 
"""
    )
    st.sidebar.title("Alumno")
    st.sidebar.info(
        """
        Emanuel Flores Martínez
"""
    )

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)


if __name__ == "__main__":
    main()