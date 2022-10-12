def fibo():
    a=0
    b=1
    while True:
        yield a
        a,b=a+b,b

a=fibo()
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))