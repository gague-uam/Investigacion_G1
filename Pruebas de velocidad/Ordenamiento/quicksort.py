import random
import time

# Función para particionar la lista
def particion(arr, low, high):
    pivote = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

# Función quick_sort recursiva
def quick_sort(arr, low, high):
    if low < high:
        pi = particion(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Envoltorio para quick_sort que toma solo la lista
def quick_sort_wrapper(arr):
    quick_sort(arr, 0, len(arr) - 1)

# Configuración inicial
n = 5000  # Tamaño de la lista
times = []  # Lista para almacenar los tiempos de ejecución

# Realizar 15 pruebas
for i in range(15):
    # Generar una lista aleatoria de 5,000 elementos
    lista = [random.randint(0, 1000) for _ in range(n)]
    
    # Medir el tiempo de ejecución
    start_time = time.time()
    quick_sort_wrapper(lista)
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