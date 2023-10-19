# Importar Streamlit
import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.title('Ejemplo de Widgets en Streamlit')

    # 1. Cajas de texto
    texto_usuario = st.text_input('Escribe algo aquí:')
    if texto_usuario:
        st.write(f"Escribiste: {texto_usuario}")

    # 2. Deslizadores
    rango_numero = st.slider('Selecciona un número del rango', 0, 100, 50)
    st.write(f"Seleccionaste: {rango_numero}")

    # 3. Cajas de selección
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['temperatura',
                 'humedad',
                 'precipitaciones'
                ]
    )
    
    opcion = st.selectbox('Elige una fruta', ['temperatura', 'humedad', 'precipitaciones'])
    st.line_chart(chart_data[opcion])

    # 4. Botones
    if st.button('Púlsame'):
        st.write('¡Botón pulsado!')

    # 5. Casillas de verificación
    mostrar_info = st.checkbox('Mostrar información extra')
    if mostrar_info:
        st.write('Aquí tienes información adicional.')
    
    # 6. Botones de opción
    mascota = st.radio("¿Cuál es tu mascota preferida?", ('Perro', 'Gato', 'Pájaro'))
    st.write(f"Tu mascota preferida es: {mascota}")

    # 7. Cargadores de archivos
    archivo = st.file_uploader('Carga un archivo')
    if archivo:
        st.write('¡Archivo cargado exitosamente!')

    # 8. Fecha y selección de tiempo
    fecha = st.date_input('Selecciona una fecha')
    st.write(f"Seleccionaste la fecha: {fecha}")

    tiempo = st.time_input('Selecciona una hora')
    st.write(f"Seleccionaste la hora: {tiempo}")

if __name__ == '__main__':
    main()
