import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import altair as alt


#Leemos y adaptamos el dataframe para trabajar con el
ma = pd.read_csv("modelo_atribucion.tsv", sep = "\t")
ma.set_index("NOMBRES CAMPAÑA", drop=True, append=False, inplace=True, verify_integrity=False)
ma.dropna(inplace = True)


#Creamos columnas para nuestro analisis

ma['modalidad']=('WEB','DATA','WEB','WEB','WEB','WEB','WEB','WEB','WEB','WEB', None,None,None, 'DATA','DATA','DATA','DATA','DATA','DATA','DATA','DATA')

ma['cte_clic'] = ma.apply(lambda row: row.COSTE / row.CLICS, axis=1)

ma['cte_lead'] = ma.apply(lambda row: row.COSTE / row.NLEADS, axis=1)

ma['%costes'] = ma.apply(lambda row: row.COSTE / np.sum(np.array(ma['COSTE'])) * 100, axis=1)

ma['lead_clic'] = ma.apply(lambda row: row.NLEADS / row.CLICS, axis=1)


#Clasificamos por destino de marketing, meta o google
ma_meta = ma[ma.FUENTE == 'META']
ma_google = ma[ma.FUENTE == 'GOOGLE ADS']

#Guardamos en listas los datos
lista_cte_lead_meta = ma_meta['cte_lead']
lista_cte_lead_google = ma_google['cte_lead']

lista_cte_clic_meta = ma_meta['cte_clic']
lista_cte_clic_google = ma_google['cte_clic']

lista_n_lead_meta = ma_meta['NLEADS']
lista_n_lead_google = ma_google['NLEADS']

lista_coste_meta = ma_meta['COSTE']
lista_coste_google = ma_google['COSTE']

#calculamos medias y totales
media_cte_lead_meta = np.mean(np.array(ma_meta['cte_lead']))
media_cte_lead_google = np.mean(np.array(ma_google['cte_lead']))

media_cte_clic_meta = np.mean(np.array(ma_meta['cte_clic']))
media_cte_clic_google = np.mean(np.array(ma_google['cte_clic']))

media_n_lead_meta = np.mean(np.array(ma_meta['NLEADS']))
media_n_lead_google = np.mean(np.array(ma_google['NLEADS']))

media_coste_meta = np.mean(np.array(ma_meta['COSTE']))
media_coste_google = np.mean(np.array(ma_google['COSTE']))

total_coste_meta = np.sum(np.array(ma_meta['COSTE']))
total_coste_google = np.sum(np.array(ma_google['COSTE']))

num_campañas_meta = np.count_nonzero(np.array(ma_meta['COSTE']))
num_campañas_google = np.count_nonzero(np.array(ma_google['COSTE']))


#Representamos la informacion obtenida

st.title("Estudio de los costes de marketing de Codenotch")
image = Image.open("captura.jpg")
st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


col1, col2 = st.columns(2)

with col1:
    st.metric('Campañas con google', num_campañas_google)
    st.caption('Google es el proveedor mayoritario, 90% del total')
    image = Image.open("google.jpg")
    st.image(image, caption=None, width=122, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

with col2:
    st.metric('Campañas con meta', num_campañas_meta)
    st.caption('Meta es con quien menos trabaja Codenotch')
    image = Image.open("meta.jpg")
    st.image(image, caption=None, width=138, use_column_width=None, clamp=False, channels="RGB", output_format="auto")



st.title("Coste total de las campañas")
opcion = st.selectbox('Elige un proveedor', ['Todos', 'Meta','Google'])
opcion1 = st.selectbox('Elige una modalidad de bootcamp', ['Todos', 'DATA','WEB'])
if opcion == 'Google': 
    if opcion1 == 'WEB':
        x = ma[(ma.FUENTE == 'GOOGLE ADS') & (ma.modalidad == 'WEB')]['COSTE']
    elif opcion1 == 'DATA':
        x = ma[(ma.FUENTE == 'GOOGLE ADS') & (ma.modalidad == 'DATA')]['COSTE']
    elif opcion1 == 'Todos':
        x = ma[ma.FUENTE == 'GOOGLE ADS']['COSTE']    
elif opcion == 'Meta':
    if opcion1 == 'WEB':
        x = ma[(ma.FUENTE == 'META') & (ma.modalidad == 'WEB')]['COSTE']
    elif opcion1 == 'DATA':
        x = ma[(ma.FUENTE == 'META') & (ma.modalidad == 'DATA')]['COSTE']
    elif opcion1 == 'Todos':
        x = ma[ma.FUENTE == 'META']['COSTE']
elif opcion == 'Todos':
    if opcion1 == 'WEB':
        x = ma[ma.modalidad == 'WEB']['COSTE']
    elif opcion1 == 'DATA':
        x = ma[ma.modalidad == 'DATA']['COSTE']
    elif opcion1 == 'Todos':
        x = ma['COSTE']  

st.bar_chart(x)
st.markdown('Las campañas mas :red[costosas] :thermometer: hasta ahora han sido:')
st.caption('   -DATA_Bootcamp ')
st.caption('   -DATA_CURSO ')
st.caption('   -ES_PRO_WEB ')
st.caption('   -WEB_Bootcamp ')

st.title("Costes unitarios")
options = st.multiselect('',['Clics', 'Leads'], placeholder ='Elige unos costes')
if options == ['Clics']:
    st.line_chart(ma['cte_clic'])
elif options == ['Leads']:
    st.line_chart(ma['cte_lead'])
elif options == ['Clics', 'Leads']:
    ma['cte_lead + cte_clic'] = ma.apply(lambda row: row.cte_lead + row.cte_clic, axis=1)
    st.line_chart(ma['cte_lead + cte_clic'])
elif options == ['Leads', 'Clics']:
    ma['cte_lead + cte_clic'] = ma.apply(lambda row: row.cte_lead + row.cte_clic, axis=1)
    st.line_chart(ma['cte_lead + cte_clic'])

t1 = ('media lead',media_cte_lead_meta, media_cte_lead_google)
t2 = ('media clic',media_cte_clic_meta, media_cte_clic_google)
t3 = ('media total',media_coste_meta, media_coste_google)

lista8  = [t1, t2, t3]
cs = pd.DataFrame(lista8, columns=("Cte","Meta", "Google"))
cs.set_index("Cte", inplace=True)
st.title("Coste Meta VS Google")
st.dataframe(cs.style.highlight_max(axis=1, color='blue'), width=570)
st.markdown('Google es mas caro en las variables estudiadas, sin embargo en media total lo es Meta, lo que invita a pensar que faltan variables por explicar')

st.title("Resultados Meta VS Google")




col1, col2, col3 = st.columns(3)

t10 = ('Meta',num_campañas_meta, np.sum(np.array(ma_meta['NLEADS'])))
t20 = ('Google',num_campañas_google, np.sum(np.array(ma_google['NLEADS'])))
lista5  = [t10, t20]
df = pd.DataFrame(lista5, columns=("Proveedor","Campañas", "Leads"))
df.set_index("Proveedor", inplace=True)
df['Lead/Camp'] = df.apply(lambda row: row.Leads / row.Campañas, axis=1)

with col1:
    st.bar_chart(df['Campañas'])

with col2:
    st.bar_chart(df['Leads'])

with col3:
    st.bar_chart(df['Lead/Camp'])

st.line_chart(ma['lead_clic'].sort_values())

st.markdown('Google es el que mas leads ha aportado, debido a que ha sido el proveedor mas habitual. Codenotch ha conseguido mas leads en cada campaña en Meta')





