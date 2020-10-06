def solution(args):
    answer, lst = [], []
    check = args[0]
    for i in args[1:]:
        if i - check == 1:
            if not lst:
                lst.append(str(check))
            lst.append(str(i))
        elif lst:
            if len(lst) != 2:
                answer.append("-".join([lst[0], lst[-1]]))
            else:
                answer.append(",".join(lst))
            lst = []
        else:
            answer.append(str(check))
        check = i
    if lst:
        if len(lst) != 2:
            answer.append("-".join([lst[0], lst[-1]]))
        else:
            answer.append(",".join(lst))
        lst = []
    else:
        answer.append(str(check))
    return ','.join(answer)