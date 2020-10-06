def isSolved(field):
    f = 1
    if field[0][0] == field[1][1] == field[2][2]:
        if field[0][0] == 1:
            f = 0
            return 1
        elif field[0][0] == 2:
            f = 0
            return 2
    elif field[0][2] == field[1][1] == field[2][0]:
        if field[0][2] == 1:
            f = 0
            return 1
        elif field[0][2] == 2:
            f = 0
            return 2
    for i in range(0, 3):
        if field[i][0] == field[i][1] == field[i][2] == 1:
            f = 0
            return 1
        elif field[i][0] == field[i][1] == field[i][2] == 2:
            f = 0
            return 2
        elif field[0][i] == field[1][i] == field[2][i] == 1:
            f = 0
            return 1
        elif field[0][i] == field[1][i] == field[2][i] == 2:
            f = 0
            return 2
            break
    for i in field:
        if 0 in i:
            return -1
    return 0