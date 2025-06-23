import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

n = 5000
times = []

for i in range(15):
    lista = [random.randint(0, 1000) for _ in range(n)]
    start_time = time.time()
    bubble_sort(lista)
    end_time = time.time()
    execution_time = end_time - start_time
    times.append(execution_time)
    print(f"Prueba {i+1}: {execution_time:.3f} segundos")

worst_time = max(times)
best_time = min(times)
average_time = sum(times) / len(times)

print(f"\nPeor tiempo (n=5,000): {worst_time:.3f} segundos")
print(f"Mejor tiempo (n=5,000): {best_time:.3f} segundos")
print(f"Tiempo promedio (n=5,000): {average_time:.3f} segundos")