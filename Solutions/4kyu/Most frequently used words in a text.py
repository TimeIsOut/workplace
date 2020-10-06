def top_3_words(text):
    dic = {}
    for i in [".", ",", "!", "?", ":", ";", "-", "_", "/"]:
        text = text.replace(i, " ")
    for i in text.split():
        if i not in dic.keys():
            dic[i] = 0
        dic[i] += 1
    dic = sorted([i[::-1] for i in [[key, val] for key, val in dic.items()]], reverse=True)
    dic = [i for i in dic if any([j.isalpha() for j in i[1]])]
    dic = [i for i in dic if i[1] != '']
    checking, c_lst, new_lst = 0, [], []
    for i in dic:
        if checking != i[0] and not c_lst:
            checking = i[0]
            c_lst.append(i)
        elif checking != i[0] and c_lst:
            new_lst += sorted(c_lst)
            c_lst = [i]
            checking = i[0]
        elif checking == i[0]:
            c_lst.append(i)
    new_lst += sorted(c_lst)
    dic = new_lst
    print(dic)
    if not dic:
        return []
    elif len(dic) < 3:
        return [i[1].lower() for i in dic]
    else:
        return [dic[0][1].lower(), dic[1][1].lower(), dic[2][1].lower()]