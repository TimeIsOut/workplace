def find_even_index(arr):
    for i in range(len(arr)):
        c1, c2 = arr[:i], arr[i + 1:]
        if sum(c1) == sum(c2):
            return i
    return -1