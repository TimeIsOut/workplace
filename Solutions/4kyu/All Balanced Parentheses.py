def backtrack(lst, string, open, close, n):
    if len(string) == n * 2:
        lst.append(string)
    if open > 0:
        backtrack(lst, string + "(", open - 1, close, n)
    if close > open:
        backtrack(lst, string + ")", open, close - 1, n)


def balanced_parens(n):
    lst = []
    backtrack(lst, "", n, n, n)
    return lst