def high_and_low(numbers):
    return ' '.join([str(max(list(map(int, numbers.split())))), str(min(list(map(int, numbers.split()))))])