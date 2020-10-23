def stock_list(listOfArt, listOfCat):
    if not listOfArt or not listOfCat: return ''
    answer = dict([[i, 0] for i in listOfCat])
    for i in listOfArt:
        if i.split()[0][0] in answer.keys():
            answer[i.split()[0][0]] += int(i.split()[1])
    return ' - '.join(f"({' : '.join([i, str(k)])})" for i, k in answer.items())