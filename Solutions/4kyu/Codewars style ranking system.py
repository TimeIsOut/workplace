class User:
    def __init__(self):
        self.ranks = list(range(-8, 9))
        self.ranks.remove(0)
        self.rank = -8
        self.progress = 0

    def inc_progress(self, num):
        check = self.ranks.index(num) - self.ranks.index(self.rank)
        print(check)
        if check == 0:
            self.progress += 3
        elif check == -1:
            self.progress += 1
        elif check > 0:
            self.progress += 10 * check ** 2
        if self.progress >= 100:
            self.progress, inc = self.progress % 100, self.progress // 100
            if self.ranks.index(self.rank) + inc < len(self.ranks) - 1:
                self.rank = self.ranks[self.ranks.index(self.rank) + inc]
            else:
                self.rank = 8
        if self.rank == 8:
            self.progress = 0