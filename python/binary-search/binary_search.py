

def binary_search(array, x):
    i = 0
    j = len(array)
    while i < j:
        k = (i + j) // 2
        v = array[k]
        if x < v:
            j = k
        elif x > v:
            i = k + 1
        else:
            return k
    else:
        raise ValueError('%d not found' % x)
