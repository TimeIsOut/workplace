def stray(arr):
    data = [arr.count(i) for i in arr]
    for i, k in zip(data, arr):
        if i == 1:
            return k