def points(games):
    summa = 0
    for i in games:
        x, y = i.split(":")
        if x > y:
            summa += 3
        elif x == y:
            summa += 1
    return summa