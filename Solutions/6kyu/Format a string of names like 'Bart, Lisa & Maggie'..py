def namelist(names):
    if not names: return ''
    if len(names) == 1: return names[0]["name"]
    return ', '.join([i["name"] for i in names[:-1]]) + " & " + names[-1]['name']