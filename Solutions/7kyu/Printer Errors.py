def printer_error(s):
    return f"{sum([1 for i in s if i not in 'abcdefghijklm'])}/{len(s)}"