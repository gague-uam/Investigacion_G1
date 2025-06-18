class Ordenamiento:
    def __init__(self):
        pass

    def quicksort(self, arr, low, high):
        if low < high:
            
            pi = self.partition(arr, low, high)

            self.quicksort(arr, low, pi - 1)
            self.quicksort(arr, pi + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]  
        i = low - 1         

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # Intercambiar

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            swapped = False  

            
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

            
            if not swapped:
                break
    
    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2  
           
            left = arr[:mid]
            right = arr[mid:]
           
            self.merge_sort(left)
            self.merge_sort(right)
            
            i = j = k = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

    def heapsort(self,arr):
        def heapify(arr, n, i):
            largest = i         
            left = 2 * i + 1     
            right = 2 * i + 2    
         
            if left < n and arr[left] > arr[largest]:
                largest = left
          
            if right < n and arr[right] > arr[largest]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]  
                heapify(arr, n, largest)  

        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]  
            heapify(arr, i, 0)  

    def timsort(self, arr):
        MIN_RUN = 32
        n = len(arr)

        
        def insertion_sort(sub_arr, left, right):
            for i in range(left + 1, right + 1):
                key = sub_arr[i]
                j = i - 1
                while j >= left and sub_arr[j] > key:
                    sub_arr[j + 1] = sub_arr[j]
                    j -= 1
                sub_arr[j + 1] = key

        def merge(sub_arr, l, m, r):
            left = sub_arr[l:m + 1]
            right = sub_arr[m + 1:r + 1]

            i = j = 0
            k = l

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    sub_arr[k] = left[i]
                    i += 1
                else:
                    sub_arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                sub_arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                sub_arr[k] = right[j]
                j += 1
                k += 1

        for start in range(0, n, MIN_RUN):
            end = min(start + MIN_RUN - 1, n - 1)
            insertion_sort(arr, start, end)

        size = MIN_RUN
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min(n - 1, left + size - 1)
                right = min((left + 2 * size - 1), n - 1)

                if mid < right:
                    merge(arr, left, mid, right)

            size *= 2