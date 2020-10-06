import re


def count_smileys(arr):
    return sum([bool(re.match(r"^(:|;)(-|~)?(\)|D)$", i)) for i in arr])