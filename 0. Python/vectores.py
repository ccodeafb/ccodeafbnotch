import random

#Crear vector(n, m): Crea un vector de n números aleatorios que van desde 0 hasta m.

def crear_vector(n, m):
    vector = []
    for v in range(n):
        vector.append(random.randint(0, m))
    return vector

#Suma vector(v1, v2): Suma dos vectores v1 y v2 si y solo si tienen el mismo numero de elementos.

def suma_vector(v1,v2):
    v3 = []
    if len(v1) == len(v2):
        for i in range(len(v1)): 
            v3.append(v1[i]+v2[i])
    else: print("La longitud no es la misma, no se pueden sumar")
    return v3

        
#Producto numero vector(n, v1): Multiplica el vector v1 por el numero n.

def prod_vector(n,v1):
    v2 = []
    for i in range(len(v1)): 
        v2.append(v1[i]*n)
    return v2

#Resta vector(v1, v2): Resta dos vectores v1 y v2 si y solo si tienen el mismo numero de elementos.

def resta_vector(v1,v2):
    v3 = []
    if len(v1) == len(v2):
        for i in range(len(v1)): 
            v3.append(v1[i]-v2[i])
    else: print("La longitud no es la misma, no se pueden restar")
    return v3
    


#Producto vector(v1, v2): Multiplica dos vectores v1 y v2 si y solo si tienen el mismo número de elementos

def mult_vector(v1,v2):
    v3 = []
    if len(v1) == len(v2):
        for i in range(len(v1)): 
            v3.append(v1[i]*v2[i])
    else: print("La longitud no es la misma, no se pueden multiplicar")
    return v3
       










