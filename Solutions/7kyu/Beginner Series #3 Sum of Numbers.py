def get_sum(a,b):
    checks = sorted([a, b])
    return sum([i for i in range(checks[0], checks[1] + 1)])