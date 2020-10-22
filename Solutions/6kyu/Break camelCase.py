def solution(s):
    answer = ""
    for i in s:
        if i.isupper():
            answer += " " + i
        else:
            answer += i
    return answer