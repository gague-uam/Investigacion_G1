import random
import time
from collections import deque

# Generar un grafo no dirigido con 50,000 nodos
def generar_grafo(n, promedio_vecinos=5):
    grafo = {i: set() for i in range(n)}  # Usar conjuntos para evitar duplicados
    # Asegurar conexidad: conectar cada nodo al siguiente
    for i in range(n-1):
        grafo[i].add(i+1)
        grafo[i+1].add(i)
    # Añadir aristas aleatorias
    for nodo in range(n):
        num_vecinos = random.randint(1, min(10, n-1))  # Entre 1 y 10 vecinos
        posibles_vecinos = list(range(n))
        posibles_vecinos.remove(nodo)
        vecinos = random.sample(posibles_vecinos, min(num_vecinos, len(posibles_vecinos)))
        for vecino in vecinos:
            grafo[nodo].add(vecino)
            grafo[vecino].add(nodo)  # Grafo no dirigido
    # Convertir conjuntos a listas para BFS
    return {nodo: list(vecinos) for nodo, vecinos in grafo.items()}

# Función de búsqueda en anchura en un grafo
def bfs_search(grafo, start, target):
    if start == target:
        return start
    queue = deque([start])
    visited = {start}
    
    while queue:
        node = queue.popleft()
        for neighbor in grafo[node]:
            if neighbor not in visited:
                if neighbor == target:
                    return neighbor
                visited.add(neighbor)
                queue.append(neighbor)
    return -1

# Configuración inicial
n = 50000  # Número de nodos
random.seed(42)  # Para reproducibilidad
print("Generando grafo...")
start_gen_time = time.time()
grafo = generar_grafo(n)
end_gen_time = time.time()
print(f"Grafo generado en {end_gen_time - start_gen_time:.3f} segundos")

# Mejor caso: buscar el nodo inicial
start_time = time.time()
result = bfs_search(grafo, 0, 0)
best_case_time = time.time() - start_time
print(f"Mejor caso (nodo inicial, resultado: {result}): {best_case_time:.6f} segundos")

# Peor caso: buscar un nodo lejano (nodo n-1)
start_time = time.time()
result = bfs_search(grafo, 0, n-1)
worst_case_time = time.time() - start_time
print(f"Peor caso (nodo lejano, resultado: {result}): {worst_case_time:.6f} segundos")

# Caso promedio: buscar 15 nodos aleatorios presentes en el grafo
average_times = []
for i in range(15):
    target = random.randint(0, n-1)  # Nodo aleatorio
    start_time = time.time()
    result = bfs_search(grafo, 0, target)
    execution_time = time.time() - start_time
    average_times.append(execution_time)
    print(f"Prueba {i+1} (nodo {target}, resultado: {result}): {execution_time:.6f} segundos")

average_time = sum(average_times) / len(average_times)

# Mostrar resultados finales
print(f"\nResultados finales:")
print(f"Mejor caso (nodo inicial): {best_case_time:.6f} segundos")
print(f"Peor caso (nodo lejano): {worst_case_time:.6f} segundos")
print(f"Tiempo promedio (15 pruebas): {average_time:.6f} segundos")