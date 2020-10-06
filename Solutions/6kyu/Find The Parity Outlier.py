def find_outlier(it):
    return it[[i % 2 for i in it].index(1)] if [i % 2 for i in it].count(1) == 1 else it[[i % 2 for i in it].index(0)]