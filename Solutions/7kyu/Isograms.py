def is_isogram(string):
    return all([1 if string.lower().count(i) == 1 else 0 for i in string.lower()])