def comp(array1, array2):
    if array1 == None or array2 == None: return False
    return True if sorted([i ** 2 for i in array1]) == sorted(array2) else False
