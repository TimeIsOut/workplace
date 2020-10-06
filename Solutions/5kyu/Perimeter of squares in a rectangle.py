def perimeter(n):
    f1, f2, lst = 1, 1, []
    for i in range(n + 1):
        lst.append(f1 * 4)
        f1, f2 = f2, f1 + f2
    return sum(lst)