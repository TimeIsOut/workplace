def recycle(a):
    b = {"pa": [], "gl": [], "or": [], "pl": []}
    for i in a:
        working_name = ""
        for key, val in i.items():
            if key == "type":
                working_name = val
            elif key == "material" or key == "secondMaterial":
                b[val[:2]].append(working_name)
    return tuple(b.values())