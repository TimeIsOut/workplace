def to_camel_case(text):
    if text == "":
        return ""
    ans, f = text[0], 0
    for i in text[1:]:
        if i in ["-", "_"]:
            f = 1
        else:
            if f:
                ans += i.upper()
            else:
                ans += i.lower()
            f = 0
    return ans