import random
import time

# Función de búsqueda binaria
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Configuración inicial
n = 50000  # Tamaño de la lista
lista = sorted(random.sample(range(100000), n))  # Lista ordenada de 50,000 números únicos

# Mejor caso: buscar el elemento central
start_time = time.time()
binary_search(lista, lista[n // 2])
best_case_time = time.time() - start_time

# Peor caso: buscar el último elemento
start_time = time.time()
binary_search(lista, lista[-1])
worst_case_time = time.time() - start_time

# Caso promedio: buscar 15 elementos aleatorios presentes en la lista
average_times = []
for _ in range(15):
    target = random.choice(lista)  # Elegir un elemento presente
    start_time = time.time()
    binary_search(lista, target)
    execution_time = time.time() - start_time
    average_times.append(execution_time)

average_time = sum(average_times) / len(average_times)

# Mostrar resultados
print(f"Mejor caso (elemento central): {best_case_time:.6f} segundos")
print(f"Peor caso (último elemento): {worst_case_time:.6f} segundos")
print(f"Tiempo promedio (15 pruebas): {average_time:.6f} segundos")