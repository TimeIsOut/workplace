def high(x):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    data = [sum([alphabet.index(j) + 1 for j in i]) for i in x.split()]
    maximum = max(data)
    for i, k in zip(x.split(), data):
        if k == maximum:
            return i