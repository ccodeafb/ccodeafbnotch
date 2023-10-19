#!/usr/bin/env python
# coding: utf-8

# # Retos 1.2

# In[161]:


#De la misma manera que en el ejemplo de esta unidad, crea la clase
#“Persona” de la manera más completa que se te ocurra.

import datetime
anyoactual = datetime.date.today().year

class Persona():
    def __init__(self,nombre,anyoNacimiento,peso,altura,aficiones):
        self.nombre=nombre
        self.anyoNacimiento=anyoNacimiento
        self.peso=peso
        self.altura=altura
        self.aficiones=aficiones
    def hablar(self):
        print("¡Hola!")
    def saltar(self):
        print("Saltó 0.5 metros")
        
#Reto 2
#Utilizando la clase “Persona” definida en el punto anterior, haz que se pueda
#calcular el IMC (índice de mas corporal) de cualquier persona que se haya creado como un objeto de la clase.

    def IMC(self):
        return self.peso / self.altura
    
#Reto 3
#Añadir el atributo anyoNacimiento a la clase ”Persona” e implementar el
#método edad que tome como parámetro el año actual y calcule la edad de la persona

    def edad(self):
        return anyoactual-self.anyoNacimiento
    
#Reto 4
#Añadir un método que se denomine mostrarTodos que muestre por consola cada una de los atributos de la clase “Persona” 
#seguido por “:” y el valor del atributo.
    
    def mostrarTodos(self):
        print(f"Nombre: {self.nombre}, Año de nacimiento: {self.anyoNacimiento}, Peso: {self.peso}, Altura: {self.altura}")

        
##Reto 5
#Añadir el atributo aficiones a la clase “Persona”, que es un array de strings, y
#crear un método denominado mostrarAficiones, que muestre por consola las aficiones de la persona.

    def mostrarAficiones(self):
        print("Las aficiones son: " + ", ".join(a.capitalize() for a in self.aficiones))     
                
#Reto 6
#• Crear una clase que se llame ”Agenda” que tenga un atributo que sea una lista de objetos de la clase “Persona”.

persona1 = Persona("Diego",1990,180,79,["correr","bailar"])
persona2 = Persona("Raquel",1985,170,57,["leer","saltar"])
persona3 = Persona("Marisa",2015,130,34,["futbol","deberes"])

class Agenda():
    def __init__(self):
        self.lista_p=[]
    def añadir_personas(self,p):
        self.lista_p.append(p)

#• Crear un método llamado printPersonas que imprima cada uno de los atributos de cada objeto persona.

    def printPersonas(self):
        for p in self.lista_p:
            p.mostrarTodos()
    
    


# In[158]:


persona1.mostrarTodos()
persona1.mostrarAficiones()
print(persona1.edad())


# In[164]:


Agenda1=Agenda()
Agenda1.añadir_personas(persona1)
Agenda1.añadir_personas(persona2)
Agenda1.añadir_personas(persona3)
Agenda1.printPersonas()


# In[ ]:




