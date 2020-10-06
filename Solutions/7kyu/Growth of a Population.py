def nb_year(p0, percent, aug, p):
    percent /= 100
    count = 0
    while p0 < p:
        p0 = p0 + p0 * percent + aug
        count += 1
    return count