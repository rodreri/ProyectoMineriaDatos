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