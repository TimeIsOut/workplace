def is_prime(num):
    if num < 2:
        return False
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True