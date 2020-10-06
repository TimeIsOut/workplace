import math


def middle_permutation(string):
    a_s, string = '', sorted(list(string))
    dividend = math.factorial(len(string)) // 2 - 1
    for i in range(len(string)):
        perms = math.factorial(len(string) - 1)
        if len(string) == 1:
            a_s += string[0]
            break
        letter = string[dividend // perms]
        a_s += letter
        string.remove(letter)
        dividend -= perms * (math.floor(dividend // perms))
    print(len(string))
    return a_s