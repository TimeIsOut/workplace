def accum(s):
    return '-'.join([((i + 1) * s[i]).capitalize() for i in range(len(s))])