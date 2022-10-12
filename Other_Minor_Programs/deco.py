
def modify(func):
    def inner(a,b):
        c = func(a,b)
        return c * 100
    return inner



@modify
def add(a,b):
    return a+b

print(add(10,20))