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

