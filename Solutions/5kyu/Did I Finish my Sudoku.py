def done_or_not(board):
    normal_doing = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in board:
        check = [j for j in i]
        check.sort()
        if check != normal_doing:
            return "Try again!"
    for i in range(9):
        check = [board[j][i] for j in range(9)]
        check.sort()
        if check != normal_doing:
            return "Try again!"
    a, b = 0, 0
    while a != 9 and b != 9:
        check = []
        for i in range(a, a + 3):
            for j in range(b, b + 3):
                check += [board[i][j]]
        check.sort()
        if check != normal_doing:
            return "Try again!"
        if a == 9:
            b += 3
            a = 0
        else:
            a += 3
    return "Finished!"