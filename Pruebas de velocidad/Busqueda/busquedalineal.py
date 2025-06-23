import random
import time

# Función de búsqueda lineal
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Configuración inicial
n = 50000  # Tamaño de la lista
lista = random.sample(range(100000), n)  # Lista de 50,000 números únicos

# Mejor caso: buscar el primer elemento
start_time = time.time()
linear_search(lista, lista[0])
best_case_time = time.time() - start_time

# Peor caso: buscar el último elemento
start_time = time.time()
linear_search(lista, lista[-1])
worst_case_time = time.time() - start_time

# Caso promedio: buscar 15 elementos aleatorios presentes en la lista
average_times = []
for _ in range(15):
    target = random.choice(lista)  # Elegir un elemento presente
    start_time = time.time()
    linear_search(lista, target)
    execution_time = time.time() - start_time
    average_times.append(execution_time)

average_time = sum(average_times) / len(average_times)

# Mostrar resultados
print(f"Mejor caso (primer elemento): {best_case_time:.6f} segundos")
print(f"Peor caso (último elemento): {worst_case_time:.6f} segundos")
print(f"Tiempo promedio (15 pruebas): {average_time:.6f} segundos")