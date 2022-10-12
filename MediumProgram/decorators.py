def sum_deco(func):
    def inner(a):
        b = func(a)
        return b + 100
    return inner



@sum_deco
def sums(a):
    return a

print(sums(10))