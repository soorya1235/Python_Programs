class test:

    def __init__(self,max):
        self.max = max
        self.n =0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            self.n += 1
            return self.n
        else:
            raise StopIteration

t1 = test(10)
print(t1)
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(dir(t1))