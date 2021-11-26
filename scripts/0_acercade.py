from pandas.tseries.offsets import Hour
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit.elements.arrow import Data

def write():
    # Datos Generales
    st.title('Proyecto Final Mineria de Datos')
    st.markdown('**Alumno:** Erick Rodrigo Minero Pineda')
    st.markdown('**Correo:** rodreri@gmail.com')

    st.markdown('En este proyecto si integra en una interfaz grafica la compilacion de las practica realizadas a lo largo del semestre')
    st.markdown('Se va a utilizar como datos de entrada, datos abiertos que la CDMX publica, con fecha del 20 de noviembre del 2021. Estos datos contienen un conjunto de datos con los incidentes viales reportados por el Centro de Comando, Control, Cómputo, Comunicaciones y Contacto Ciudadano de la Ciudad de México (C5) desde 2014 y actualizado mensualmente')
    st.text('Liga: https://datos.cdmx.gob.mx/dataset/incidentes-viales-c5')