def parse(data):
    lst, i = [], 0
    for j in data:
        if j == "i":
          i += 1
        elif j == "d":
          i -= 1
        elif j == "s":
          i **= 2
        elif j == "o":
          lst.append(i)
    return lst