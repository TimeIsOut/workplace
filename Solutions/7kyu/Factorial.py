def factorial(n):
    if not n or n == 1: return 1
    if n < 0 or n > 12: raise ValueError
    return n * factorial(n - 1)