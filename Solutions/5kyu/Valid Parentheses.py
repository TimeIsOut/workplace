def valid_parentheses(string):
    o = 0
    for i in string:
        if i == "(":
            o += 1
        elif i == ")":
            o -= 1
            if o == -1:
                return False
    if o != 0:
        return False
    return True