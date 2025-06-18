from collections import deque

def busqueda_anchura(grafo, inicio, objetivo):
    visitados = set()
    cola = deque([inicio])
    while cola:
        nodo = cola.popleft()
        if nodo == objetivo:
            return True
        if nodo not in visitados:
            visitados.add(nodo)
            cola.extend(vecino for vecino in grafo.get(nodo, []) if vecino not in visitados)
    return False

if __name__ == "__main__":
    grafo = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    inicio = input("Nodo de inicio: ").strip().upper()
    objetivo = input("Nodo objetivo: ").strip().upper()

    if busqueda_anchura(grafo, inicio, objetivo):
        print(f"Existe un camino de {inicio} a {objetivo}.")
    else:
        print(f"No existe un camino de {inicio} a {objetivo}.")
