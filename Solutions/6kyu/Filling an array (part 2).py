def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def squares(n):
    return [i ** 2 for i in range(1, n + 1)]

def num_range(n, start, step):
    lst, count = [], 0
    while count < n:
        lst.append(start)
        start += step
        count += 1
    return lst

def rand_range(n, mn, mx):
    from random import randint
    return [randint(mn, mx) for _ in range(n)]

def primes(n):
    lst, count = [], 2
    while len(lst) != n:
        if isPrime(count):
            lst.append(count)
        count += 1
    return lst