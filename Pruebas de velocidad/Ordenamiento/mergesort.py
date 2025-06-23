import random
import time

# Función merge para fusionar dos sublistas ordenadas
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Función merge_sort recursiva
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# Configuración inicial
n = 5000  # Tamaño de la lista
times = []  # Lista para almacenar los tiempos de ejecución

# Realizar 15 pruebas
for i in range(15):
    # Generar una lista aleatoria de 5,000 elementos
    lista = [random.randint(0, 1000) for _ in range(n)]
    
    # Medir el tiempo de ejecución
    start_time = time.time()
    merge_sort(lista)
    end_time = time.time()
    
    # Calcular y almacenar el tiempo de la prueba
    execution_time = end_time - start_time
    times.append(execution_time)
    print(f"Prueba {i+1}: {execution_time:.3f} segundos")

# Calcular el peor tiempo, mejor tiempo y tiempo promedio
worst_time = max(times)
best_time = min(times)
average_time = sum(times) / len(times)

# Mostrar resultados finales
print(f"\nPeor tiempo: {worst_time:.3f} segundos")
print(f"Mejor tiempo: {best_time:.3f} segundos")
print(f"Tiempo promedio: {average_time:.3f} segundos")