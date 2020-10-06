def solution(string,markers):
    data = string.split("\n")
    for i in range(len(data)):
        for j in markers:
            if j in data[i]:
                data[i] = data[i][:data[i].index(j)].strip(" ")
    return '\n'.join(data)