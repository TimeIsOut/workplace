def arithmetic(a, b, operator):
    dic = {"add": "+", "subtract": "-", "multiply": "*", "divide": "/"}
    return eval(f"{a}{dic[operator]}{b}")