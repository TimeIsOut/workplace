def format_duration(s):
    if not s: return "now"
    y, d, h, m, s = s // (3600 * 24 * 365), s // (3600 * 24) % 365, s // 3600 % 24, s // 60 % 60, s % 60
    print(y, d, h, m, s)
    working = [[i, k] for i, k in zip([y, d, h, m, s], ["year", "day", "hour", "minute", "second"]) if i]
    joining = []
    for i in working:
        joining.append(f"{i[0]} {i[1]}{'s' if i[0] != 1 else ''}")
    if len(joining) == 1:
        return joining[0]
    elif len(joining) == 2:
        return ' and '.join(joining)
    else:
        return ', '.join(joining[:-1]) + " and " + joining[-1]