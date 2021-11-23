from pandas.tseries.offsets import Hour
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit.elements.arrow import Data

# Datos Generales
st.title('Proyecto Final Mineria de Datos')
st.markdown('**Alumno:** Erick Rodrigo Minero Pineda')
st.markdown('**Correo:** rodreri@gmail.com')

st.markdown('En este proyecto si integra en una interfaz grafica la compilacion de las practica realizadas a lo largo del semestre')
st.markdown('Se va a utilizar como datos de entrada, datos abiertos que la CDMX publica, con fecha del 20 de noviembre del 2021. Estos datos contienen un conjunto de datos con los incidentes viales reportados por el Centro de Comando, Control, Cómputo, Comunicaciones y Contacto Ciudadano de la Ciudad de México (C5) desde 2014 y actualizado mensualmente')
st.text('Liga: https://datos.cdmx.gob.mx/dataset/incidentes-viales-c5')

st.markdown('## Análisis exploratorio de datos')
@st.cache
def load_data(nrows):
    data = pd.read_csv("inci.csv", index_col=0, encoding='latin-1', nrows=nrows)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Cargando datos...')
# Load 10,000 rows of data into the dataframe.
# maximo numero 217000
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Datos leidos con exito!")

# st.subheader('Raw data')
# st.write(data)
if st.checkbox('Ver datos'):
    st.subheader('Datos...')
    st.write(data)

st.markdown('### Descripcion de la estructura de los datos')
st.markdown('La matriz de datos que se cargo tiene la siguiente forma, cabe mencionar que streamlit no permite cargar mas de 50 MB de datos, po lo que solo se eligen 10000 registros de forma aleatoria')
st.write(data.shape)

st.markdown('El tipo de dato que se tiene por columna')
# st.write(data.dtypes) Pendiente error

st.markdown('### Identifcación de datos faltantes')
st.write(data.isnull().sum())
st.markdown('De acuerdo con lo anterior **no se cuentan con datos nulos**')

st.markdown('### Deteccion de valores atipicos')
st.write(data.describe())



















# Convertimos a hora la columna
Matriz = np.array(data[['latitud', 'longitud', 'hora_creacion']])
MatrizPD = pd.DataFrame(Matriz, columns=['lat','lon', 'hora_creacion'])
MatrizPD['hora_creacion'] = pd.to_datetime(MatrizPD['hora_creacion'], format='%H:%M:%S')

# Mapa de accidentes por hora
st.subheader('Mapa de accidentes')
# st.map(MatrizPD)
hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = MatrizPD[MatrizPD['hora_creacion'].dt.hour == hour_to_filter]
st.subheader(f'Accidentes a las {hour_to_filter}:00')
# st.write(filtered_data)
st.map(filtered_data)

# Grafica de accidentes por hora
hist_values = np.histogram(
    MatrizPD['hora_creacion'].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)