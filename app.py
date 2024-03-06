import streamlit as st
from tensorflow.keras.models import load_model
import gdown
import requests
from io import BytesIO
import tempfile
import os

st.title('Mi Aplicación Streamlit con Modelo Preentrenado')

# Enlace compartido de Google Drive al archivo HDF5 (reemplaza 'your_file_id')
enlace_google_drive = 'https://drive.google.com/uc?id=1NNw7-bCVLEYNKH4Q6rnwXCRkxa2IHAka'

# Función para cargar el modelo desde Google Drive
def cargar_modelo_desde_drive(enlace):
    with st.spinner('Descargando el modelo...'):
        response = requests.get(enlace)
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(response.content)
        temp_file.close()
        modelo_cargado = load_model(temp_file.name)
        os.remove(temp_file.name)
    return modelo_cargado

# Cargar el modelo en tiempo real
modelo_cargado = cargar_modelo_desde_drive(enlace_google_drive)

# Hacer predicciones o cualquier otra cosa con el modelo cargado
# ...

# Mostrar información sobre el modelo
st.write("Modelo cargado exitosamente:", modelo_cargado.summary())
