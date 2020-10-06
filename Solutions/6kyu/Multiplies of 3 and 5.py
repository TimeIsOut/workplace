def solution(number):
    lst = [i for i in range(1, number) if i % 3 == 0 or i % 5 == 0]
    return sum(lst)