import time
import random

def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Genera una lista de un millón de números aleatorios entre 1 y 100 y la ordena
lista = [random.randint(1, 100) for _ in range(1000000)]
lista.sort()

buscar = int(input("¿Qué elemento deseas buscar? "))

tiempo_inicial = time.time()
posicion = busqueda_binaria(lista, buscar)
tiempo_final = time.time()

if posicion != -1:
    print(f"Elemento '{buscar}' encontrado en la posición {posicion}.")
else:
    print(f"Elemento '{buscar}' no encontrado en la lista.")

print(f"Tiempo inicial: {tiempo_inicial}")
print(f"Tiempo final: {tiempo_final}")
tiempo = tiempo_final - tiempo_inicial
print(f"Duración total: {tiempo}")