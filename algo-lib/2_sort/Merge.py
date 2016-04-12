def merge(array):


    def sort(array, lo, hi):

    def merge(array, lo, mid, hi):
        """ 将array[lo..mid] 和array[mid+1, hi]归并.
        """
        aux = list(array)  # copy array to aux array
        i = lo, j = mid + 1

        for k in range(array):
            if aux[i] < aux[j]: 
                array[k] = aux[i]
                i += 1
            elif aux[j] <= aux[i]:
                array[k] = aux[j]
                j += 1
            elif i > mid:
                array[k] = aux[j]
                j += 1
            elif j > hi:
                array[k] = aux[i]
                i += 1

    return sort(array, low, hi)