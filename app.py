import streamlit as st
import gdown
from tensorflow.keras.models import load_model

st.title('Descargar y Cargar Pesos desde Google Drive')

# Enlace compartido de Google Drive al archivo HDF5 (reemplaza 'your_file_id')
enlace_google_drive = 'https://drive.google.com/uc?id=1NNw7-bCVLEYNKH4Q6rnwXCRkxa2IHAka'

# Botón para iniciar la descarga
if st.button('Descargar Pesos desde Google Drive'):
    with st.spinner('Descargando los pesos...'):
        # Descargar el archivo desde Google Drive
        output_file_path = 'pesos.hdf5'
        gdown.download(enlace_google_drive, output_file_path, quiet=False)

        st.success('Descarga completa. Puedes cargar los pesos ahora.')

# Cargar el modelo con los pesos descargados
if st.button('Cargar Modelo con Pesos'):
    try:
        # Cargar el modelo con los pesos
        modelo_cargado = load_model('pesos.hdf5')
        st.success('Modelo cargado exitosamente con los pesos descargados.')
        
        # Realizar acciones adicionales con el modelo cargado si es necesario
        # ...
    except Exception as e:
        st.error(f'Error al cargar el modelo: {e}')
