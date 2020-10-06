def persistence(n):
    count = 0
    while len(str(n)) != 1:
        num = 1
        for i in str(n):
            num *= int(i)
        n = num
        count += 1
    return count