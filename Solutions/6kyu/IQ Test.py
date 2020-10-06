def iq_test(numbers):
    data = [1 if i % 2 == 0 else 0 for i in list(map(int, numbers.split()))]
    return data.index(0) + 1 if data.count(1) > data.count(0) else data.index(1) + 1