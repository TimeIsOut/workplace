def validPhoneNumber(pN):
    return True if pN[0] == '(' and pN[4] == ')' and pN[5] == ' ' and pN[9] == '-' and len(pN) == 14 else False