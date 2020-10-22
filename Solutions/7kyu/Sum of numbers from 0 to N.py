def show_sequence(n):
    if n > 0:
        return f"{'+'.join(str(i) for i in range(n + 1))} = {(n ** 2 + n) // 2}"
    elif n == 0:
        return "0=0"
    else:
        return f"{n}<0"