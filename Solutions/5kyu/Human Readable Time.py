def make_readable(sec):
    h, sec = str(sec // 3600), sec % 3600
    m, sec = str(sec // 60), str(sec % 60)
    if len(h) == 1: h = f"0{h}"
    if len(m) == 1: m = f"0{m}"
    if len(sec) == 1: sec = f"0{sec}"
    return f"{h}:{m}:{sec}"