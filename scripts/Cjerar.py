from pandas.tseries.offsets import Hour
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit.elements.arrow import Data

def write():
    st.title("Cluster Jerarquico")
    def load_data(nrows):
        # data = pd.read_csv("incid.csv", index_col=0, encoding='latin-1', nrows=nrows)
        data = pd.read_csv("datas/Hipoteca.csv")
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

    from sklearn.preprocessing import StandardScaler, MinMaxScaler  
    estandarizar = StandardScaler()                               # Se instancia el objeto StandardScaler o MinMaxScaler 
    MEstandarizada = estandarizar.fit_transform(data)   # Se calculan la media y desviación y se escalan los datos

    st.markdown("""
      Al trabajar con el agoritmo que permite hacer clustering, dado que son algoritmos basados en distancias, es fundamental escalar los
      datos para que cada una de las variables contribuyan por igual en el análisis.
    """)
    st.write(pd.DataFrame(MEstandarizada))

    

    #Se importan las bibliotecas de clustering jerárquico para crear el árbol
    import scipy.cluster.hierarchy as shc
    from sklearn.cluster import AgglomerativeClustering
    
    plt.figure(figsize=(10, 7))
    plt.title("Casos de hipoteca")
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    # Arbol = shc.dendrogram(shc.linkage(MEstandarizada, method='complete', metric='euclidean'))
    
    # st.pyplot(fig)
    #plt.axhline(y=5.4, color='orange', linestyle='--')
    #Probar con otras medciones de distancia (euclidean, chebyshev, cityblock)

    #Se crean las etiquetas de los elementos en los clústeres
    MJerarquico = AgglomerativeClustering(n_clusters=7, linkage='complete', affinity='euclidean')
    MJerarquico.fit_predict(MEstandarizada)
    st.write(MJerarquico.labels_)
