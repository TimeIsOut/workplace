class add(int):
    __call__ = lambda self, value: add(self + value)