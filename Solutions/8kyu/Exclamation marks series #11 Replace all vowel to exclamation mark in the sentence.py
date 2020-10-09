def replace_exclamation(s):
    for i in "aeiouAEIOU":
        s = s.replace(i, "!")
    return s