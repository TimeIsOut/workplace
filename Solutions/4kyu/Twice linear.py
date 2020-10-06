def dbl_linear(n):
    lst = [1]
    c_1, c_2 = 0, 0
    while len(lst) <= n:
        a, b = lst[c_1] * 2 + 1, lst[c_2] * 3 + 1
        if a > b:
            lst.append(b)
            c_2 += 1
        elif a < b:
            lst.append(a)
            c_1 += 1
        else:
            lst.append(a)
            c_1, c_2 = c_1 + 1, c_2 + 1
    return lst[n]