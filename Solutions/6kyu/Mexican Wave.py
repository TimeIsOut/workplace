def wave(str_1):
    return [str_1[:i] + str_1[i].upper() + str_1[i + 1:] for i in range(len(str_1)) if str_1[i] != " "]