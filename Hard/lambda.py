x = lambda  x : x**4
print(x(4))

x = filter(lambda x:x%2==0,range(0,100))
print(list(x))

y=map(lambda x:x**2,range(0,10))
print(list(y))

from functools import reduce
z=reduce(lambda x,y:x+y,range(0,5))
print(z)