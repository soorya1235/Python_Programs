from collections import Counter
from collections.abc import Iterator
from collections.abc import Iterable
str = "aaaaaaaaabbbbbbbbbbbbbbcccccccccccccccccddddddddddd"
l1=(Counter(str))
print(dict(l1))

ls = [1,2,3,4,5,6]
m1 = iter(ls)

if isinstance(ls,Iterable):
    print("List is Iterable")

if isinstance(m1,Iterator):
    print("List is Iterator")
else:print("List is Not an Iterator")