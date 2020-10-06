def dig_pow(n, p):
    a = list(str(n))
    j = 0
    for i in a:
        j += int(i) ** p
        p += 1
    if j % n == 0:
        return j // n
    else:
        return -1