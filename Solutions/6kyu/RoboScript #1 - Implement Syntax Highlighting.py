def highlight(code):
    data = []
    answer, previous_char = "", ""
    for i in code:
        if previous_char == i or previous_char.isdigit() == i.isdigit() == 1:
            data[-1] += i
        else:
            data.append(i)
        previous_char = i
    for i in range(len(data)):
        if data[i][0] == "F":
            data[i] = f'<span style="color: pink">{data[i]}</span>'
        elif data[i][0] == "L":
            data[i] = f'<span style="color: red">{data[i]}</span>'
        elif data[i][0] == "R":
            data[i] = f'<span style="color: green">{data[i]}</span>'
        elif data[i][0].isdigit():
            data[i] = f'<span style="color: orange">{data[i]}</span>'
    return ''.join(data)