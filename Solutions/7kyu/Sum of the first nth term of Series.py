def series_sum(n):
    if n == 0:
        return "0.00"
    c = 0
    for i in range(0, n):
        c += 1 / (1 + 3*i)
    return str(round(c, 2)).ljust(4, "0")