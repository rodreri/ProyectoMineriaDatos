from pandas.tseries.offsets import Hour
import streamlit as st
import pandas as pd
import numpy as np
from streamlit.elements.arrow import Data

st.title('Proyecto Final Mineria de Datos')

@st.cache
def load_data(nrows):
    data = pd.read_csv("inci.csv", index_col=0, encoding='latin-1', nrows=nrows)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
# maximo numero 217000
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

# st.subheader('Raw data')
# st.write(data)
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


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