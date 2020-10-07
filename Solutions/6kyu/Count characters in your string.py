def count(string):
    dic, checking = {}, set(string)
    for i in checking:
        dic[i] = string.count(i)
    return dic