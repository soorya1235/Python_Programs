class gent:

    def __init__(self,max,start):
        self.max = max
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.max:
            self.start = self.start + 1
            return self.start
        else:
            raise StopIteration

a1 = gent(10,0)
print(next(a1))
print(next(a1))
print(next(a1))
print(next(a1))
print(next(a1))