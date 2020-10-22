def unique_in_order(iterable):
    if not iterable: return []
    check = iterable[0]
    answer = [iterable[0]]
    for i in iterable[1:]:
        if i != check:
            check = i
            answer += [i]
    if check != iterable[-1]:
        answer += [i]
    return answer