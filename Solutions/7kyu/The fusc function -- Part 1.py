def fusc(n):
    assert type(n) == int and n >= 0
    a, b = 1, 0
    while n != 0:
        if n % 2 == 0:
            a, n = a + b, n / 2
        else:
            b, n = a + b, (n - 1) / 2
    return b