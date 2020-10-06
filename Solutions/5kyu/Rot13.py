from string import ascii_lowercase as l
from string import ascii_uppercase as u


def rot13(m):
    ans = ''
    for i in m:
        if i.islower():
            ans += l[(l.index(i) + 13) % 26]
        elif i.isupper():
            ans += u[(u.index(i) + 13) % 26]
        else:
            ans += i
    return ans