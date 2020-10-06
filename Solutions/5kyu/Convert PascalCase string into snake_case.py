def to_underscore(string):
    string = str(string)
    ans = ""
    for i in range(len(string)):
        if string[i].isupper() and i == 0:
            ans += string[i].lower()
        elif string[i].isupper() and i != 0:
            ans += "_" + string[i].lower()
        elif string[i].isdigit():
            ans += string[i]
        else:
            ans += string[i]
    return ans
