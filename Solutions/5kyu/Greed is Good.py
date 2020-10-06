def score(dice):
    nums, score = [0, 0, 0, 0, 0, 0], 0
    for i in dice:
        nums[i - 1] += 1
    for i in range(1, 7):
        score += [10, 2, 3, 4, 5, 6][i - 1] * 100 * (nums[i - 1] // 3)
        nums[i - 1] %= 3
    score += 100 * nums[0]
    score += 50 * nums[4]
    return score