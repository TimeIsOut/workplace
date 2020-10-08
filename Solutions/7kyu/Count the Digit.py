def nb_dig(n, d):
    return ''.join(list(map(str, [i ** 2 for i in range(0, n + 1)]))).count(str(d))