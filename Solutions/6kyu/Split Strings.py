def solution(s):
    if len(s) % 2 == 0:
        return [s[i] + s[i + 1] for i in range(0, len(s), 2)]
    else:
        s += "_"
    return [s[i] + s[i + 1] for i in range(0 ,len(s), 2)]