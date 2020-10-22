def no_boring_zeros(n):
    if not n: return 0
    return int(str(n).rstrip("0"))