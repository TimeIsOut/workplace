def max_sequence(arr):
    if all([1 if i < 0 else 0 for i in arr]): return 0
    answer = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if sum(arr[i:j + 1]) > answer:
                answer = sum(arr[i:j + 1])
    return answer
