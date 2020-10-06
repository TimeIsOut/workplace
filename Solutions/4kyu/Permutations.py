import itertools


def permutations(string):
    return set(map(''.join, itertools.permutations(string, len(string))))