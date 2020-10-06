def snail(snail_map):
    print(snail_map)
    if snail_map == [[]]:
        return []
    indexes = {1: (0, 1), 2: (1, 0), 3: (0, -1), 4: (-1, 0)}
    p, ind = [0, 0], 1
    answer = []
    ln = len(snail_map)
    min_c, max_c = 0, ln - 1
    for _ in range(ln ** 2):
        answer.append(snail_map[p[0]][p[1]])
        p[0], p[1] = p[0] + indexes[ind][0], p[1] + indexes[ind][1]
        if (p[0] == min_c or p[0] == max_c) and (p[1] == min_c or p[1] == max_c) and not (p[0] == p[1] == min_c):
            ind += 1
        elif p[0] == p[1] == min_c:
            p = [min_c + 1, min_c + 1]
            min_c += 1
            max_c -= 1
            ind = 1
    return answer