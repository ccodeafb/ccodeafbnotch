# Importar Streamlit
import streamlit as st

def main():
    st.title('Ejemplo de Layouts en Streamlit')

    # Sidebar
    st.sidebar.header('Barra Lateral')
    opcion = st.sidebar.selectbox('Elige una opción', ['A', 'B', 'C'])
    st.sidebar.write('Has seleccionado:', opcion)

    # Columnas
    col1, col2 = st.columns(2)

    with col1:
        st.header('Columna 1')
        st.write('Contenido de la columna 1.')
        st.radio("Opción Radio en Col1", ('1', '2', '3'))

    with col2:
        st.header('Columna 2')
        st.write('Contenido de la columna 2.')
        if st.button('Botón en Col2'):
            st.write('¡Botón en la columna 2 presionado!')

    # Expander
    with st.expander('Haz clic para expandir'):
        st.write('Contenido detallado que se mostrará al expandir.')
        st.slider('Deslizador dentro del expander', 0, 10, 5)

    # Espacio vacío (será llenado más tarde)
    espacio = st.empty()

    # Contenedor
    with st.container():
        st.text('Este es el inicio del contenedor.')
        st.text_input('Escribe algo en el contenedor:')
        st.text('Este es el final del contenedor.')

    # Rellenar el espacio vacío creado anteriormente
    espacio.text('Este texto llena el espacio previamente vacío.')

if __name__ == '__main__':
    main()
