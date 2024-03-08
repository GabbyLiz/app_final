import streamlit as st
import gdown
import requests
import os 
from tensorflow.keras.models import load_model
from PIL import Image

st.title('Descargar y Cargar Pesos desde Google Drive')

# Enlace compartido de Google Drive al archivo HDF5 (reemplaza 'your_file_id')
enlace_google_drive = 'https://drive.google.com/uc?id=1FMoVJX2X-pgYV7noOXny6Xnq5lPjJetb'

# Variable de sesión para realizar un seguimiento del estado de la descarga
descarga_realizada = st.session_state.get('descarga_realizada', False)

# Obtener el tamaño original del archivo en bytes
with st.spinner('Obteniendo información del archivo...'):
    response = requests.head(enlace_google_drive)
    file_size_original = int(response.headers['Content-Length'])

# Crear una sección para cargar una imagen de fondo
background_image = 'logo2.png'  # Ruta de la imagen de fondo
st.markdown(
    f"""
    <style>
        .reportview-container {{
            background: url({background_image}) no-repeat center center fixed;
            background-size: cover;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Crear una sección para cargar una imagen
st.header('Cargar Imagen')

# Añadir un botón para cargar la imagen
imagen_cargada = st.file_uploader('Selecciona una imagen', type=['jpg', 'jpeg', 'png'])

# Mostrar la imagen cargada si existe
if imagen_cargada is not None:
    st.image(imagen_cargada, caption='Imagen cargada', use_column_width=True)

# Crear una barra lateral para las opciones de descarga
st.sidebar.subheader('Opciones de Descarga')
opcion_descarga = st.sidebar.selectbox('Seleccione una opción de descarga:', ['Seleccione', 'Opción 1', 'Opción 2', 'Opción 3'])

# Botón para iniciar la descarga solo si se selecciona una opción válida y la descarga aún no se ha realizado
if opcion_descarga != 'Seleccione' and not descarga_realizada:
    if st.sidebar.button(f'Descargar Pesos para {opcion_descarga} desde Google Drive'):
        with st.spinner('Descargando los pesos...'):
            # Descargar el archivo desde Google Drive
            output_file_path = f'pesos_{opcion_descarga.lower()}.hdf5'
            gdown.download(enlace_google_drive, output_file_path, quiet=False)
            
            # Obtener el tamaño del archivo después de la descarga
            file_size_downloaded = os.path.getsize(output_file_path)

            st.success(f'Descarga completa para {opcion_descarga}. Puedes cargar los pesos ahora.')
            st.info(f'Tamaño original del archivo: {file_size_original / (1024 ** 2):.2f} MB')
            st.info(f'Tamaño del archivo descargado: {file_size_downloaded / (1024 ** 2):.2f} MB')

            # Actualizar la variable de sesión para indicar que la descarga se ha realizado
            st.session_state.descarga_realizada = True

# Cargar el modelo con los pesos descargados solo si la descarga se ha realizado
if descarga_realizada and st.sidebar.button('Cargar Modelo con Pesos'):
    try:
        # Cargar el modelo con los pesos
        modelo_cargado = load_model(f'pesos_{opcion_descarga.lower()}.hdf5')
        st.success('Modelo cargado exitosamente con los pesos descargados.')
        
        # Realizar acciones adicionales con el modelo cargado si es necesario
        # ...
    except Exception as e:
        st.error(f'Error al cargar el modelo: {e}')
