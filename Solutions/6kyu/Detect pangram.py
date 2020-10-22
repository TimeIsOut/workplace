from string import ascii_lowercase as a

def is_pangram(s):
    for i in a:
        if i not in s.lower():
            return False
    return True