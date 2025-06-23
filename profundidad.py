def busqueda_profundidad(grafo, inicio, objetivo):
    visitados = set()
    pila = [inicio]
    while pila:
        nodo = pila.pop()
        if nodo == objetivo:
            return True
        if nodo not in visitados:
            visitados.add(nodo)
            pila.extend(vecino for vecino in grafo.get(nodo, []) if vecino not in visitados)
    return False

if __name__ == "__main__":
    # Grafo simple de ejemplo
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

    if busqueda_profundidad(grafo, inicio, objetivo):
        print(f"Existe un camino de {inicio} a {objetivo}.")
    else:
        print(f"No existe un camino de {inicio} a {objetivo}.")
