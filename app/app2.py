import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import streamlit as st
import pickle
from datetime import datetime, time, timedelta
import pytz



modelo = pickle.load(open('randomforest.pkl', 'rb'))
st.title('PCA+RANDOMFOREST')

# Cargar el modelo
with open('randomforest.pkl', 'rb') as f:
    model = pickle.load(f)

# Crear entradas para los datos
ema5 = st.number_input('Introduce el valor de ema5', step = 100.0)
ema20 = st.number_input('Introduce el valor de ema20', step= 100.0)
volume = st.number_input('Introduce el valor de volume', step=1000.0)  # Tamaño del paso ajustado a 1000.0
CCI15 = st.number_input('Introduce el valor de CCI15',step = 100.0)
CCI10 = st.number_input('Introduce el valor de CCI10', step = 100.0)

# Crear un botón para ejecutar el modelo
run_model = st.button('Ejecutar el modelo')

# Si el botón es presionado
if run_model:
    # Crear un DataFrame con los datos de entrada
    data = pd.DataFrame({
        'ema5': [ema5],
        'ema20': [ema20],
        'volume': [volume],
        'CCI15': [CCI15],
        'CCI10': [CCI10]
    })

    # Preprocesar los datos
    # data = preprocess_data(data)  # Asegúrate de crear esta función

    # Hacer la predicción
    prediction = model.predict(data)

    # Mostrar la predicción
    st.write('La predicción del modelo es: ', prediction)