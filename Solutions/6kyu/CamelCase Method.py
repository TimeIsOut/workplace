def camel_case(string):
    a = string.title()
    a = list(a)
    j = 0
    for i in a:
        if i == ' ':
            a.pop(j)
        j += 1
    c = ''.join(a)
    return c