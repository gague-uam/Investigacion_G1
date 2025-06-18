from model.algoritmo import Ordenamiento

class DaoAlgoritmo:
    def __init__(self):
        self.algoritmo = Ordenamiento()

    def ordenar_quick(self, arr):
        self.algoritmo.quicksort(arr, 0, len(arr) - 1)
        return arr

    def ordenar_bubble(self, arr):
        self.algoritmo.bubble_sort(arr)
        return arr

    def ordenar_merge(self, arr):
        self.algoritmo.merge_sort(arr)
        return arr
    
    def ordenar_heapsort(self, arr):
        self.algoritmo.heapsort(arr)
        return arr
    def ordenar_timsort(self, arr):
        self.algoritmo.timsort(arr)
        return arr