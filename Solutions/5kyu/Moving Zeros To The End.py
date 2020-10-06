def move_zeros(array):
    lst, count = [], 0
    for i in array:
        if i == 0 and (type(i) == int or type(i) == float):
            count += 1
        else:
            lst.append(i)
    return lst + [0] * count