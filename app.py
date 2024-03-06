import streamlit as st
import gdown
import requests  # Asegúrate de agregar esta línea
from tensorflow.keras.models import load_model

st.title('Descargar y Cargar Pesos desde Google Drive')

# Enlace compartido de Google Drive al archivo HDF5 (reemplaza 'your_file_id')
enlace_google_drive = 'https://drive.google.com/uc?id=1NNw7-bCVLEYNKH4Q6rnwXCRkxa2IHAka'

# Obtener el tamaño original del archivo en bytes
with st.spinner('Obteniendo información del archivo...'):
    response = requests.head(enlace_google_drive)
    file_size_original = int(response.headers['Content-Length'])

# Botón para iniciar la descarga
if st.button('Descargar Pesos desde Google Drive'):
    with st.spinner('Descargando los pesos...'):
        # Descargar el archivo desde Google Drive
        output_file_path = 'pesos.hdf5'
        gdown.download(enlace_google_drive, output_file_path, quiet=False)
        
        # Obtener el tamaño del archivo después de la descarga
        file_size_downloaded = os.path.getsize(output_file_path)

        st.success(f'Descarga completa. Puedes cargar los pesos ahora.')
        st.info(f'Tamaño original del archivo: {file_size_original / (1024 ** 2):.2f} MB')
        st.info(f'Tamaño del archivo descargado: {file_size_downloaded / (1024 ** 2):.2f} MB')


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
