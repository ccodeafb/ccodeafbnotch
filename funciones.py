import pandas as pd
import numpy as np 
import sys
import importlib
import funciones
import os
from datetime import datetime

def impago(dataframe):
    Producto = dataframe['Producto']
    impago_medio = {'Alta nueva + fibra Neba': 94.94840504015147, 
                    'Alta nueva + fibra Pro': 80.37161142857143, 
                    'Alta nueva + fibra Smart 1GB': 71.7065685980186, 
                    'Alta nueva + fibra Smart 500Mb': 51.67519289221416, 
                    'Alta nueva movil': 50.111616378520594, 
                    'Error': 27.47175824175824, 
                    'Fibra Neba': 80.34984520632314, 
                    'Fibra Pro': 70.28586389220536, 
                    'Fibra_Smart_1GB': 60.0659261792639, 
                    'Fibra_Smart_500Mb': 44.44962351632047, 
                    'Port + fibra Neba': 87.37978578229134, 
                    'Port + fibra Pro': 89.1276091954023,
                    'Port + fibra Smart 1GB': 75.71050396962374, 
                    'Port + fibra Smart 500Mb': 57.13898073836276, 
                    'Portabilidad movil': 62.34373610439826,
                    'Fibra Smart': 55.404119622787746}
    def apply_impago(Producto):
        for productos,impago in impago_medio.items():
            if Producto in productos: 
                return impago            
    dataframe['Estimacion_impago_bruto'] = dataframe.apply(lambda row: apply_impago(row['Producto']), axis=1)
    
def get_past_date(str_days_ago):
    import datetime
    from dateutil.relativedelta import relativedelta
    TODAY = datetime.date.today()
    splitted = str_days_ago.split()
    if len(splitted) == 1 and splitted[0].lower() == 'today':
        return str(TODAY.isoformat())
    elif len(splitted) == 1 and splitted[0].lower() == 'yesterday':
        date = TODAY - relativedelta(days=1)
        return str(date.isoformat())
    elif splitted[1].lower() in ['hour', 'hours', 'hr', 'hrs', 'h']:
        date = datetime.datetime.now() - relativedelta(hours=int(splitted[0]))
        return str(date.date().isoformat())
    elif splitted[1].lower() in ['day', 'days', 'd']:
        date = TODAY - relativedelta(days=int(splitted[0]))
        return str(date.isoformat())
    elif splitted[1].lower() in ['wk', 'wks', 'week', 'weeks', 'w']:
        date = TODAY - relativedelta(weeks=int(splitted[0]))
        return str(date.isoformat())
    elif splitted[1].lower() in ['mon', 'mons', 'month', 'months', 'm']:
        date = TODAY - relativedelta(months=int(splitted[0]))
        return str(date.isoformat())
    elif splitted[1].lower() in ['yrs', 'yr', 'years', 'year', 'y']:
        date = TODAY - relativedelta(years=int(splitted[0]))
        return str(date.isoformat())
    else:
        return "Wrong Argument format"

def calcular_scoring_ML(dataframe):
    nuevo_pesos=pd.read_excel('//diginas/40_Gestion_de_la_Informacion/INFORMES_GI/Scoring/Perfilado/Pesos/Pesos_scoring_ML.xlsx',sheet_name='Coeficientes')
    def calculo_apply_log(externa,interna,edad,canal,tipo_documento,provincia,huella,nacionalidad):
        df_deuda_ext=nuevo_pesos[nuevo_pesos['Campo']=='deuda_externa']
        df_deuda_int=nuevo_pesos[nuevo_pesos['Campo']=='CUANTIA_TOTAL']
        df_edad=nuevo_pesos[nuevo_pesos['Campo']=='EDAD']
        df_canal=nuevo_pesos[nuevo_pesos['Campo']=='CANAL']
        df_tipo_doc=nuevo_pesos[nuevo_pesos['Campo']=='tipo_documento']
        df_provincia=nuevo_pesos[nuevo_pesos['Campo']=='provincia']
        df_huella=nuevo_pesos[nuevo_pesos['Campo']=='HUELLA']
        df_nacionalidad=nuevo_pesos[nuevo_pesos['Campo']=='nacionalidad']
        
        if len(df_deuda_ext[df_deuda_ext['Resultado']==externa])>=1:
            filtro_df_deuda_ext=df_deuda_ext[df_deuda_ext['Resultado']==externa]
            coef_deuda_externa=filtro_df_deuda_ext['Coeficiente'].iloc[0]
        else:
            coef_deuda_externa=0
        try:
            interna2=int(interna)
            if len(df_deuda_int[df_deuda_int['Resultado']<=interna2])>=1:
                filtro_df_deuda_int=df_deuda_int[df_deuda_int['Resultado']<=interna2]
                coef_deuda_interna=filtro_df_deuda_int['Coeficiente'].iloc[0]
            else:
                coef_deuda_interna=0        
        except:
            coef_deuda_interna=0        
        coef_edad_inter=df_edad['Coeficiente'].iloc[0]
        coef_edad=coef_edad_inter*edad
        
        if len(df_canal[df_canal['Resultado']==canal])>=1:
            filtro_df_canal=df_canal[df_canal['Resultado']==canal]
            coef_canal=filtro_df_canal['Coeficiente'].iloc[0]
        else:
            coef_canal=0  
            
        if len(df_tipo_doc[df_tipo_doc['Resultado']==tipo_documento])>=1:
            filtro_df_doc=df_tipo_doc[df_tipo_doc['Resultado']==tipo_documento]
            coef_doc=filtro_df_doc['Coeficiente'].iloc[0]
        else:
            coef_doc=0  
            
        if len(df_provincia[df_provincia['Resultado']==provincia])>=1:
            filtro_df_provincia=df_provincia[df_provincia['Resultado']==provincia]
            coef_provincia=filtro_df_provincia['Coeficiente'].iloc[0]
        else:
            coef_provincia=0
        
        if len(df_huella[df_huella['Resultado']==huella])>=1:
            filtro_df_huella=df_huella[df_huella['Resultado']==huella]
            coef_huella=filtro_df_huella['Coeficiente'].iloc[0]
        else:
            coef_huella=0
            
        if len(df_nacionalidad[df_nacionalidad['Resultado']==nacionalidad])>=1:
            filtro_df_nacionalidad=df_nacionalidad[df_nacionalidad['Resultado']==nacionalidad]
            coef_nacionalidad=filtro_df_nacionalidad['Coeficiente'].iloc[0]
        else:
            filtro_df_nacionalidad=df_nacionalidad[df_nacionalidad['Resultado']=='OTHER']
            coef_nacionalidad=filtro_df_nacionalidad['Coeficiente'].iloc[0]
        
        filtro_df_indepe=nuevo_pesos[nuevo_pesos['Campo']=='Intercepto']
        indepe=filtro_df_indepe['Coeficiente'].iloc[0]
        resultado=indepe+coef_deuda_externa+coef_deuda_interna+coef_edad+coef_canal+coef_doc+coef_provincia+coef_huella+coef_nacionalidad
        
        return 1 / (1 + np.exp(-resultado))
    dataframe['SCORE_FINAL_ML_LOGISTICA'] = dataframe.apply(lambda row: calculo_apply_log(row['deuda_externa'],row['CUANTIA_TOTAL'],row['EDAD'],row['CANAL'],row['tipo_documento'],row['provincia'],row['HUELLA'],row['nacionalidad']), axis=1)


def DECISION_SCORE_ML_LOGISTICA(dataframe):    
    nuevo_resultados_logis = pd.read_excel('//diginas/40_Gestion_de_la_Informacion/INFORMES_GI/Scoring/Perfilado/Pesos/Pesos_scoring_ML.xlsx',sheet_name='Decision_logistica')
    minimo_aceptado = nuevo_resultados_logis[nuevo_resultados_logis['Resolucion']=='ACEPTADO']['Resultado'][0]
    minimo_revision = nuevo_resultados_logis[nuevo_resultados_logis['Resolucion']=='REVISION']['Resultado'][1]
    minimo_denegado = nuevo_resultados_logis[nuevo_resultados_logis['Resolucion']=='DENEGADO']['Resultado'][2]
    def DECISION_SCORE_ML_LOG(score,facturas_impagadas):
        if facturas_impagadas >= 2:
            return 'DENEGADO'
        elif facturas_impagadas > 0 and minimo_denegado < score:
            return 'DENEGADO'
        elif facturas_impagadas > 0:
            return 'REVISION'
        else:
            if (score > minimo_revision) & (score < minimo_denegado):
                return 'REVISION'
            elif minimo_denegado < score:
                return 'DENEGADO'
            else:
                return 'ACEPTADO'
    dataframe['DECISION_SCORE_ML_LOGISTICA'] = dataframe.apply(lambda row: DECISION_SCORE_ML_LOG(row['SCORE_FINAL_ML_LOGISTICA'],row['FACTURAS_TOTAL']), axis=1)

def comprobacion(archivo):
    try:
        def comprobar_tamaño(archivo):
            limite = 40
            directory, filename = os.path.split(archivo)
            if os.path.exists(archivo):
                tamaño = os.path.getsize(archivo)                
                if tamaño > 0:
                    print(f"OK, El archivo {filename[:limite]} se ha encontrado y su tamaño es mayor que 0KB.")
                else: 
                    print(f"KO Error, {filename[:limite]} son 0KB.")
                input("Cerrar el mensaje")
            else:
                print(f"KO Error, {filename[:limite]} no se ha guardado el archivo.")
                input("Cerrar el mensaje")
        comprobar_tamaño(archivo)
    except:
        print(f"KO Error, {filename[:15]} no se ha guardado el archivo.")
        input("Cerrar el mensaje")

def paquetes(entrada1,entrada2,entrada3):
    if entrada1==0:
        if entrada2==0:
            if entrada3==0:
                return '00_NADA'
            else:
                return '06_FIJO'
        else:
            if entrada3==0:
                return '04_FIBRA'
            else:
                return '05_FIBRA+FIJO'
    else:
        if entrada2==0:
            if entrada3==0:
                return '01_MOVIL'
            else:
                return '07_MOV+FIJO'
        else:
            if entrada3==0:
                return '02_MOV+FIBRA'
            else:
                return '03_MOV+FIJO+FIBRA'

def encontrar_huella(portabilidad,alta_nueva,tipo_fibra):
    if portabilidad==0 and alta_nueva>0 and (tipo_fibra=='NEO WIFI' or tipo_fibra=='Promo' or tipo_fibra=='0'):
        return 'Alta_nueva'
    elif portabilidad>0 and (tipo_fibra=='NEO WIFI' or tipo_fibra=='Promo' or tipo_fibra=='0'):
        return 'Portabilidad'
    elif portabilidad==0 and alta_nueva>0 and (tipo_fibra=='Fibra 1Gb' or tipo_fibra=='Fibra 300Mb' or tipo_fibra=='Fibra DIGI'):
        return 'Alta_nueva_+_Neba'
    elif portabilidad>0 and (tipo_fibra=='Fibra 1Gb' or tipo_fibra=='Fibra 300Mb' or tipo_fibra=='Fibra DIGI'):
        return 'Portabilidad_+_Neba'
    elif portabilidad==0 and alta_nueva>0 and (tipo_fibra=='Fibra PRO-DIGI 10 Gb' or tipo_fibra=='Fibra SMART 1Gb' or tipo_fibra=='Fibra SMART 500Mb'):
        return 'Alta_nueva_+_Propia'
    elif portabilidad>0 and (tipo_fibra=='Fibra PRO-DIGI 10 Gb' or tipo_fibra=='Fibra SMART 1Gb' or tipo_fibra=='Fibra SMART 500Mb'):
        return 'Portabilidad_+_Propia'
    elif portabilidad==0 and alta_nueva==0 and (tipo_fibra=='Fibra PRO-DIGI 10 Gb' or tipo_fibra=='Fibra SMART 1Gb' or tipo_fibra=='Fibra SMART 500Mb'):
        return 'Propia'
    elif portabilidad==0 and alta_nueva==0 and (tipo_fibra=='Fibra 1Gb' or tipo_fibra=='Fibra 300Mb' or tipo_fibra=='Fibra DIGI'):
        return 'Neba'
    else:
        return 'Huella_por_determinar'

def encontrar_huella2(portabilidad, alta_nueva, NEBA, PRO_DIGI, SMART, Not_Specified):
    if portabilidad == 0 and alta_nueva > 0:
        if NEBA == 1:
            return 'Alta_nueva_+_Neba'
        elif PRO_DIGI == 1:
            return 'Alta_nueva_+_Propia'
        elif SMART == 1:
            return 'Alta_nueva_+_Propia'
        elif Not_Specified == 1:
            return 'Alta_nueva'
    elif portabilidad > 0:
        if NEBA == 1:
            return 'Portabilidad_+_Neba'
        elif PRO_DIGI == 1:
            return 'Portabilidad_+_Propia'
        elif SMART == 1:
            return 'Portabilidad_+_Propia'
        elif Not_Specified == 1:
            return 'Portabilidad'
    elif portabilidad == 0 and alta_nueva == 0:
        if NEBA == 1:
            return 'Neba'
        elif PRO_DIGI == 1:
            return 'Propia'
        elif SMART == 1:
            return 'Propia'
    else:
        return 'Huella_por_determinar'
    
        
# archivo = '//diginas/45_ANALISIS_DE_OPERACIONES/01_Scoring/10_FOTO DEUDA/Deuda Ventas/Deuda_ventas_.xlsx'
# comprobacion(archivo)

## Conexion SQL

def conexionsoop(base):   
    import mysql.connector
    import random
    cuenta = random.choice(['sergio','adri'])
    if cuenta == 'sergio':
        user_digi='sergio.osma'
        password_digi='1935Ser1935+'
    elif cuenta == 'adri':
        user_digi='adrian.fernandezb'
        password_digi='9ServidorQL7'

    host_digi='digi-com-4478'
    db_digi='soop'
    db_digi2='soop_prueba'
    tabla_PRDNI='prdni'
    nombre_test='test_nombre'
    correo_test='test_correo'
    dni_test='test_dni'
    idclient_test='test_idclient'
    if base == 1:   
        miConexion = mysql.connector.connect( host = host_digi, user = user_digi, password=password_digi, db = db_digi)
        return miConexion
    elif base == 2:
        miConexion2 = mysql.connector.connect( host = host_digi, user = user_digi, password=password_digi, db = db_digi2)
        return miConexion2
    else: print('Especificar base 1 o 2')


## Altas moviles

def agrupar_altas0(dataframe):
    dataframe['altas'] = dataframe['alta_movil'].apply(
        lambda x: 2 if x == 2 else
        (3 if x == 3 else
         (4 if x == 4 else 
          (5 if x == 5 else
          (6 if x == 6 else
           (1 if x == 1 else 0))))))

def agrupar_altas(dataframe):

    dataframe['alta_movil'] = dataframe['alta_movil'].astype(int)
    dataframe['port_movil'] = dataframe['port_movil'].astype(int)
    dataframe['total_movil'] = dataframe['alta_movil'] + dataframe['port_movil']


## Tipos de paq

def agrupar_connection(dataframe,separar_smart):
    if separar_smart == True:
        dataframe['Connection_Type'] = dataframe['TIPO_PAQ_FIBRA'].apply(
            lambda x: 'Fibra_Neba' if x in ['Fibra 300Mb  y Prueba 6 meses','Fibra 100Mb','Fibra 30Mb y Prueba 6 meses','Fibra 50Mb','Fibra 1Gb', 'Fibra 300Mb','Fibra 500Mb','Fibra 30Mb'] else
            ('Fibra_Pro' if x in ['Fibra PRO-DIGI 10 Gb','Fibra DIGI 300Mb', 'DIGI Fibra 500Mb','Fibra DIGI','DIGI Fibra 100Mb'] else
             ('Fibra_Smart_1GB' if x == 'Fibra SMART 1Gb' else
              ('Fibra_Smart_500Mb' if x =='Fibra SMART 500Mb' else
             ('Movil' if x in ['0',0] else None)))))
    else:
        dataframe['Connection_Type'] = dataframe['TIPO_PAQ_FIBRA'].apply(
            lambda x: 'Fibra_Neba' if x in ['Fibra 300Mb  y Prueba 6 meses','Fibra 100Mb','Fibra 30Mb y Prueba 6 meses','Fibra 50Mb','Fibra 1Gb', 'Fibra 300Mb','Fibra 500Mb','Fibra 30Mb'] else
            ('Fibra_Pro' if x in ['Fibra PRO-DIGI 10 Gb','Fibra DIGI 300Mb', 'DIGI Fibra 500Mb','Fibra DIGI','DIGI Fibra 100Mb'] else
             ('Fibra_Smart' if x in ['Fibra SMART 1Gb', 'Fibra SMART 500Mb'] else
             ('Movil' if x in ['0',0] else None))))


## Costes por num lineas,provincia, producto, y canal

def estimacion_costes(dataframe):
    coste_sim = 1
    coste_sim_nopresencial = 5
    coste_fibra_pro = 60
    coste_fibra_neba = 15
    coste_smart1gb = 15
    coste_smart500mb = 15
    coste_smart = 15
    coste_instalacion = 20
    coste_neba_telf = 5        # suplemento telefonica
    
    connection = dataframe['Connection_Type']
    provincia = dataframe['provincia']
    alta_movil = dataframe['alta_movil']
    canal = dataframe['canal']
    alta_fijo = dataframe['paq_fijo']
    producto = dataframe['Producto']
    def actualizar_altas_moviles(producto,alta_movil):
        if producto in ['Alta nueva movil','Portabilidad movil'] and alta_movil < 1:
            return 1
        else: return alta_movil
            
    dataframe['alta_movil'] = dataframe.apply(lambda row: actualizar_altas_moviles(row['Producto'],row['alta_movil']), axis=1)
       
    
    def costes(connection, alta_movil, canal, alta_fijo):
        if canal in ['03_STAND', '06_D2D', '07_TIENDA_DIGI','01_DC']:
            coste_sim_0 = alta_movil * coste_sim
            if connection == 'Fibra_Neba':
                return coste_fibra_neba + coste_sim_0 + coste_neba_telf * alta_fijo + coste_instalacion
            elif connection == 'Fibra_Pro':
                return coste_fibra_pro + coste_sim_0 + coste_instalacion  
            elif connection in ['Fibra_Smart_1GB']:
                return coste_smart1gb + coste_sim_0 + coste_instalacion
            elif connection in ['Fibra_Smart_500Mb']:
                return coste_smart500mb + coste_sim_0 + coste_instalacion
            elif connection in ['Fibra_Smart']:
                return coste_smart + coste_sim_0 + coste_instalacion
            else:
                return  coste_sim_0
        else:
            coste_sim_0 = alta_movil * coste_sim + alta_movil * coste_sim_nopresencial
            if connection == 'Fibra_Neba':
                return coste_fibra_neba + coste_sim_0 + coste_neba_telf * alta_fijo + coste_instalacion
            elif connection == 'Fibra_Pro':
                return coste_fibra_pro + coste_sim_0 + coste_instalacion
            elif connection in ['Fibra_Smart_1GB']:
                return coste_smart1gb + coste_sim_0 + coste_instalacion
            elif connection in ['Fibra_Smart_500Mb']:
                return coste_smart500mb + coste_sim_0 + coste_instalacion
            elif connection in ['Fibra_Smart']:
                return coste_smart + coste_sim_0 + coste_instalacion
            else:
                return  coste_sim_0

    dataframe['Coste'] = dataframe.apply(lambda row: costes(row['Connection_Type'], row['alta_movil'], row['canal'], row['paq_fijo']), axis=1)
    coste = dataframe['Coste']
    def costes_añadidos(provincia, coste):
        if provincia in ['Palmas, Las' , 'Santa Cruz de Tenerife']:    
            return coste * 1.07
        else:
            return coste * 1.21
    dataframe['Coste'] = dataframe.apply(lambda row: costes_añadidos(row['provincia'], row['Coste']), axis=1)    


## DNI o NIE

def identidad(numero):
    # Los DNI comienzan con un número, mientras que los NIE comienzan con una letra
    if numero[0].isdigit():
        return 'DNI'
    else:
        return 'NIE'
        

## Agrupacion portabilidad + lineas + producto

def agrupar_productos(dataframe):
    connection = dataframe['Connection_Type']
    dataframe['total_movil'] = dataframe['total_movil'].astype(int)
    dataframe['port_movil'] = dataframe['port_movil'].astype(int)
    port_movil = dataframe['port_movil']
    total_movil = dataframe['total_movil']
    def agrupar_plus(connection, port_movil, total_movil):
        if total_movil < 1:    
            if connection == 'Fibra_Neba':
                return 'Fibra Neba'
            elif connection == 'Fibra_Pro':
                return 'Fibra Pro'
            elif connection == 'Fibra_Smart':
                return 'Fibra Smart'
            elif connection == 'Fibra_Smart_1GB':
                return 'Fibra_Smart_1GB'
            elif connection == 'Fibra_Smart_500Mb':
                return 'Fibra_Smart_500Mb'
            else:
                return 'Error'
        else:    
            if connection == 'Fibra_Neba' and port_movil < 1:
                return 'Alta nueva + fibra Neba'
            elif connection  =='Fibra_Neba':
                return 'Port + fibra Neba'
                
            elif connection  =='Movil' and port_movil < 1:
                return 'Alta nueva movil'
            elif connection  =='Movil':
                return 'Portabilidad movil'
                
            elif connection  =='Fibra_Pro' and port_movil >= 1:
                return 'Port + fibra Pro'
            elif connection  =='Fibra_Pro':
                return 'Alta nueva + fibra Pro'
                
            elif connection  =='Fibra_Smart' and port_movil < 1:
                return 'Alta nueva + fibra Smart'
            elif connection =='Fibra_Smart':
                return 'Port + fibra Smart'
                
            elif connection =='Fibra_Smart_1GB' and port_movil < 1:
                return 'Alta nueva + fibra Smart 1GB'
            elif connection =='Fibra_Smart_1GB':
                return 'Port + fibra Smart 1GB'
                
            elif connection =='Fibra_Smart_500Mb' and port_movil < 1:
                return 'Alta nueva + fibra Smart 500Mb'
            elif connection =='Fibra_Smart_500Mb':
                return 'Port + fibra Smart 500Mb'
            else:
                return 'Error'
    dataframe['Producto'] = dataframe.apply(lambda row: agrupar_plus(row['Connection_Type'], row['port_movil'], row['total_movil']), axis=1)

# Actualizador canales

def canales_act(dataframe):
    dataframe['canal'] = dataframe['canal_venta'].apply(
        lambda x: '01_DC' if x == 'DEALER' else
        ('03_STAND' if x == 'STAND' else
         ('04_TELEVENTA' if x == 'TELEVENTA' else
         ('05_C2C' if x == 'C2C' else 
          ('06_D2D' if x == 'D2D' else 
          ('07_TIENDA_DIGI' if x == 'DIGI STORE' else 
           ('02_WEB' if x == 'WEB' else '00_Otros')))))))


# Actualizador operadores donantes

def agrupar_operador(dataframe):
    dataframe['grupo_donante'] = dataframe['operador_donante'].apply(
        lambda x: 'Movistar' if x in ['Telefonica Tech AIoT','Movistar YYY','TELEFÓNICA','MOVISTAR',
                                      'TELEFÓNICA DE ESPAÑA, S.A.U', 'TELEFÃ?NICA DE ESPAÃ?A, S.A.U',
                                      'Movistar XXXXX','Movistar XXXXXXXXXX', 'movistar', 'telefonica', 'telefónica', 'Telefónica',
                                      'Movistar','11888 Servicio Consulta Telefonica S.A.','Movistar XXXXXXXXXX'] else
        ('Orange' if x in ['Orange Business Spain','Orange','France Telecom España',
                           'France Telecom EspaÃ±a','ORANGE B4B TECHNOLOGY','Amena'] else
         ('Vodafone' if x in ['Vodafone España','Vodafone ES','Vodafone','Vodafone EspaÃ±a S.A.U',
                              'vodafone','Vodafone ONO','Vodafone España S.A.U',
                              'Vodafone Roaming Services','Vodafone Es','ONO','Vodafone Enabler'] else 
          ('Pepephone' if x in ['PepePhone 3.0','PepePhone','Pepephone','pepephone'] else 
          ('MasMovil' if x in ['Virgin Telco', 'R Cable y Telecomunicaciones GALICIA S.A.', 'LCR Movil_ON movil','Happy móvil', 'IBERCOM', 
                               'THE TELECOM BOUTIQUE','Republica Movil','Mas Movil','MasMovil','Másmóvil','Xtra Telecom S.A.','Telecable Movil',
                               'OPEN CABLE', 'Cable Móvil', 'FreedomPop/ Parlem', 'Euskaltel','Hits Mobile'] else 
          ('Alta' if x in ['0'] else 
           ('Lowi' if x in ['Lowi','Vodafone Enabler'] else 
          ('Jazztel' if x in ['Jazztel Móvil','Jazztel','Jazztel MÃ³vil'] else
          ('Simyo' if x in ['Simyo'] else 
          ('Adamo' if x in ['Adamo'] else 
          ('Euskatel' if x in ['euskatel, Euskaltel S.A.', 'Euskaltel'] else 
          ('Yoigo' if x in ['Xfera Moviles S.A.','Yoigo', 'yoigo'] else 'Otros'))))))))))))


# Asignar Scoring

def asignar_scoring(dataframe):
    dataframe['DECISION_SCORE'] = dataframe['DECISION_SCORE'].apply(lambda x: 'DENEGADO' if x == 'DENEGADO' 
                                                                    else ('ACEPTADO' if x == 'ACEPTADO' else 'REVISION'))
    values = {"CUANTIA_TOTAL": 0}
    dataframe.fillna(value=values, inplace=True)

    def asignar_sco1(row):
        if row['CUANTIA_TOTAL'] > 0 and row['estado_actualizado'] == 'Cancelled':
            return 'Cancelado_1'
        elif row['deuda_externa'] in [1,'1','1.0'] and row['estado_actualizado'] == 'Cancelled':
            return 'Cancelado_1'
        elif row['estado_actualizado'] in ['Validated','Delivered']:
            return 'Aceptado_1'
        else:
            return 'Revision_1'
    def asignar_sco2(row):
        if str(row['DECISION_SCORE']) == 'DENEGADO':
            return 'Cancelado_2'
        elif str(row['DECISION_SCORE']) not in ['ACEPTADO','DENEGADO'] and row['estado_actualizado']=='Cancelled':
            return 'Cancelado_2' 
        elif str(row['DECISION_SCORE']) not in ['ACEPTADO','DENEGADO'] and row['deuda_externa']==1:
            return 'Cancelado_2'         
        elif str(row['DECISION_SCORE']) != 'DENEGADO' and row['estado_actualizado']=='Validated':
            return 'Aceptado_2' 
        else:
            return 'Revision_2' 

    dataframe['Scoring_1'] = dataframe.apply(asignar_sco1, axis=1)
    dataframe['Scoring_2'] = dataframe.apply(asignar_sco2, axis=1)


# Antiguo asignar scoring

def asignar_scoring_antiguo(dataframe):
    def asignar_sco1(row):
        if row['Decisión comercial'] == 'Permitir' and str(row['estado']) in ('Cancelled'):
            return 'Cancelado_1'
        elif row['Decisión comercial'] == 'Permitir' and str(row['estado']) in ('Validated'):
            return 'No_cancelado_1'        
        else:
            return 'Revision_1'
    def asignar_sco2(row):
        if str(row['DECISION_SCORE']) == 'DENEGADO':
            return 'Cancelado_2'
        elif row['DECISION_SCORE']=='REVISIÓN' and row['estado_actualizado']=='Cancelled':
            return 'Cancelado_2' 
        
        else:
            return 'Revision_2' 
    dataframe['Scoring_1_ANT'] = dataframe.apply(asignar_sco1, axis=1)
    dataframe['Scoring_1_ACT'] = dataframe.apply(asignar_sco1_ACT, axis=1)
    dataframe['Scoring_2'] = dataframe.apply(asignar_sco2, axis=1)



