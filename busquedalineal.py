import time
import random

def busqueda_lineal(lista, objetivo):
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i  
    return -1  

lista = [random.randint(1, 100) for _ in range(1000000)] 

buscar = int(input("¿Qué elemento deseas buscar? "))

tiempo_inicial = time.time()
posicion = busqueda_lineal(lista, buscar)
tiempo_final = time.time()

if posicion != -1:
    print(f"Elemento '{buscar}' encontrado en la posición {posicion}.")
else:
    print(f"Elemento '{buscar}' no encontrado en la lista.")

print(f"Tiempo inicial: {tiempo_inicial}")
print(f"Tiempo final: {tiempo_final}")
tiempo = tiempo_final - tiempo_inicial
print(f"Duración total: {tiempo}")