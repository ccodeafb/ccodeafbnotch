#!/usr/bin/env python
# coding: utf-8

# # Reto 1

# In[5]:


#Construye una función “calculadora()” que reciba como parámetros de entrada:

#Tipo de operación y Operadores (siempre 2 operadores para hacerlo más sencillo).

#Las operaciones permitidas son: suma (“sum”), resta (“subs”), multiplicación (“mult”) y división (“div”).

#Dependiendo del identificador de la operación, y los parámetros de entrada, la función debe decidir qué operación 
#  realizar y devolvernos un resultado válido.

def calculadora(operacion,a,b):
    
    if operacion == "suma": 
        return sum(a,b)
    elif operacion == "resta":
        return a-b
    elif operacion == "multiplicacion":
        return a * b
    elif operacion == "division":
        return a / b
    else: print("Operadores incorrectos")



# # Reto 2

# In[9]:


#Luego coloca el fichero en esta misma carpeta e importa y utiliza esas funciones
import random
import vectores

ejemplo_vector1 = vectores.crear_vector(3,385)
print(ejemplo_vector1)
ejemplo_vector2 = vectores.crear_vector(4,94)
print(ejemplo_vector2)
ejemplo_vector3 = vectores.crear_vector(4,40)
print(ejemplo_vector3)


vectores.mult_vector(ejemplo_vector1,ejemplo_vector2)
vectores.resta_vector(ejemplo_vector2,ejemplo_vector3)



# # Reto 3

# In[ ]:


#Use la función incorporada len() para encontrar la longitud de la siguiente cadena de texto: "¡Hola, mundo!".

cadena = "¡Hola, mundo!"
len(cadena)

#Cree una función llamada doblar() que toma un número y devuelve el doble de ese número. Luego use la función map() 
#para doblar todos los números en la siguiente lista: [1, 2, 3, 4, 5].

def doblar(n):
    return n*2
lista_numeros = [1, 2, 3, 4, 5]
resultado = list(map(doblar, lista_numeros))


#Cree una función llamada multiplicar() que toma dos números y devuelve su producto. Luego use la función reduce() 
#para multiplicar todos los números en la siguiente lista: [1, 2, 3, 4, 5].

from functools import reduce

def multiplicar(n,p):
    return n*p
lista_numeros2 = [1, 2, 3, 4, 5]
resultado = reduce(multiplicar, lista_numeros2)


# In[ ]:




