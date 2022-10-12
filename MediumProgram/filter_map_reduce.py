list1 = range(0,10)

abcd = filter(lambda x:x%2==0,list1)
print(list(abcd))

abcd = map(lambda x:x**3,[1,2,3,4,5,6,7])
print(list(abcd))

from functools import reduce

abcd = reduce(lambda x,y:x+y,list1)
print(abcd)

from collections import Iterator
from collections import Iterable