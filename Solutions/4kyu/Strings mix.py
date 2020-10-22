def mix(s1, s2):
    s1, s2 = ''.join([i for i in s1 if i.islower()]), ''.join([i for i in s2 if i.islower()])
    set1, set2 = ''.join(sorted(set(s1))), ''.join(sorted(set(s2)))
    working = ''.join(sorted(set(set1 + set2)))
    answer = []
    for i in working:
        if s1.count(i) > s2.count(i) and s1.count(i) > 1:
            answer.append([s1.count(i) * i, "1"][::-1])
        elif s1.count(i) < s2.count(i) and s2.count(i) > 1:
            answer.append([s2.count(i) * i, "2"][::-1])
        elif s1.count(i) == s2.count(i) and s1.count(i) > 1:
            answer.append([s1.count(i) * i, "="][::-1])
    answer = sorted(answer, key=lambda x: (1 / len(x[1]), x[0]))
    return '/'.join([":".join(i) for i in answer])