import streamlit as st
import pandas as pd
from pandas.tseries.offsets import Hour
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit.elements.arrow import Data
import awesome_streamlit as ast

def write():
    st.title('Analisis de componentes principales')
    def load_data(nrows):
        data = pd.read_csv("incid.csv", index_col=0, encoding='latin-1', nrows=nrows)
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

    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA

    data = data.drop(['fecha_creacion', 'hora_creacion', 'dia_semana', 'delegacion_inicio', 'codigo_cierre'], axis=1)
    normalizar = StandardScaler()                  # Se instancia el objeto StandardScaler 
    normalizar.fit(data)                           # Se calcula la media y desviación para cada variable
    MNormalizada = normalizar.transform(data)      # Se normalizan los dato
    
    pca = PCA(n_components=None)             # Se instancia el objeto PCA    #pca=PCA(n_components=None), pca=PCA(.85)
    pca.fit(MNormalizada)                  # Se obtiene los componentes
    st.write(pca.components_)

    Varianza = pca.explained_variance_ratio_
    print('Porporción de varianza:', Varianza)
    print('Varianza acumulada:', sum(Varianza[0:6]))   
    #Con 6 componentes se tiene el 89% de varianza acumulada y con 7 el 93%