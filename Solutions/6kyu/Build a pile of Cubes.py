def find_nb(m):
    count = 1
    while m > 0:
        m -= count ** 3
        count += 1
    return count - 1 if m == 0 else -1