import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from PIL import Image
import requests
import pickle
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from streamlit_option_menu import option_menu

#[theme]
#backgroundColor="#0E117"   <- de la web en ejecucion arriba a la derecha en settings --> theme


st.markdown(
    """
    <style>
    body {
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

marcas = ['Opel', 'Tesla', 'SsangYong', 'KIA', 'Lexus', 'Mitsubishi',
       'Nissan', 'Renault', 'SEAT', 'Skoda', 'Jeep', 'Abarth', 'Volvo',
       'Maserati', 'Dacia', 'Infiniti', 'Toyota', 'Land Rover', 'Jaguar',
       'Iveco', 'Citroen', 'Audi', 'Alfa Romeo', 'DS', 'BMW', 'Alpine',
       'Peugeot', 'Bentley', 'CUPRA', 'Honda', 'Hyundai', 'Mercedes-Benz',
       'Fiat', 'Ford', 'Volkswagen', 'Porsche', 'Mazda', 'Subaru',
       'Suzuki', 'Aston Martin', 'MG', 'Cadillac', 'Mahindra', 'Dodge',
       'KTM', 'Ferrari', 'Lamborghini', 'Rover', 'MINI', 'Saab',
       'Renault Trucks', 'Hummer', 'Tata', 'Galloper', 'Lancia',
       'Daihatsu', 'Daewoo', 'Chevrolet', 'Chrysler', 'Corvette',
       'McLaren', 'Lada', 'Isuzu', 'Santana', 'VAZ', 'Lotus']

#Representamos la informacion obtenida


with st.sidebar:
    selected = option_menu("Navegador", ['Estimador', 'Estudio de mercado'], 
        icons=['car-front-fill', 'bar-chart-fill'], menu_icon="cast", default_index=0)  

if selected == 'Estimador':

    st.title('Estimador de precios')
    st.subheader('¿Por cuánto puedes anunciar tu vehículo?')

    st.markdown('Con nuestra aplicacion puedes saber el precio óptimo para vender tu coche')
    

    with st.sidebar:
        st.markdown('**¡Introduce los datos!** :car:')
        marca = st.selectbox('Elige una marca', marcas)
        km = st.slider('¿Cuántos kms tiene?', 10000, 350000, 100000)
        edad = st.slider('¿Cuántos años tiene?', 0, 20, 5)
        fuel = st.selectbox('Tipo de combustible', ['Gasolina', 'Diésel', 'Eléctrico', 'Otros'])
        shift0 = st.selectbox('Tipo de cambio', ['Manual', 'Automático'])
        cambio = {'manual':'Manual', 'automatic':'Automático'}    
        shift = [key for key, value in cambio.items() if value == shift0][0]
        

    image = Image.open('C:/Users/Usuario/Desktop/proyecto/app/coches.jpeg')
    st.image(image, caption=None, width=510, output_format="JPEG")

    

    x_test = {"make": marca, "fuel": fuel, "kms": km, "shift":shift,  "antiguedad": edad}

    x_test = pd.DataFrame([x_test])

    #LOAD MODEL

    from utils.auxiliar import obtener_clase

    mi_instancia = obtener_clase()

    prediccion = mi_instancia.predict(x_test)

    #st.text(f'Precio sugerido al que puedes anunciar tu coche')

    st.markdown(f'Vehículo elegido: {marca}, Kms: {km}, Antigüedad: {edad}, Combustible: {fuel}, Cambio: {shift0}' )

    st.markdown("*Pulsa para conocer el precio sugerido al que puedes anunciar tu* ***coche***.")

    #st.button("Reset", type="primary")
    if st.button('Calcular:'):

        #st.markdown(f'Estimación: {int(prediccion[0])} €')
        st.metric(label='**Estimación:**', value=(f'{int(prediccion[0])} €'), delta=None, delta_color="normal", help=None, label_visibility="visible")
        st.markdown('''¡Mucha suerte! :money_with_wings:''')

    else:
        st.write(' ')

#st.divider()

elif selected == 'Estudio de mercado':

    st.title('Radiografía del mercado en España')
    st.components.v1.html("""<iframe title="Report Section" width="850" height="1000" src="https://app.powerbi.com/view?r=eyJrIjoiOWRjNWVmOGYtMzMwMy00YzY5LTliNTItZmVjYTVmMTNhY2FjIiwidCI6ImJiYjEzOGJhLWZjMDYtNDM2ZS04ODhlLTAyYmVjMzFlYTIzYSIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>""", width=850, height=930, scrolling=False)
