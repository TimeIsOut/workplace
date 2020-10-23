def duplicate_count(text):
    answer = ""
    for i in text.lower():
        if i not in answer and text.lower().count(i) > 1:
            answer += i
    return len(answer)