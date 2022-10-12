dic1 = {"a":1,"b":5,"c":4,"f":2,"e":6}
from collections import Iterable
from collections import Iterator
from functools import reduce

a = sorted(dic1.items(),key=lambda x:x[1])
print(a)
b = sorted(dic1.items(),key=lambda x:x[0])
print(b)

from operator import itemgetter

a = sorted(dic1.items(),key=itemgetter(0))
b = sorted(dic1.items(),key=itemgetter(1))
print(a)
print(b)