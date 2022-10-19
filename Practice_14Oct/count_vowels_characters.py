from collections.abc import Iterable
from collections.abc import Iterator
from collections import Counter

vow = {"a","e","i","o","u"}
str = "aaaaaeeeeeeeeeiiiissssssssssssttttttttttttuuuuuuuuuuvvvvvvvvvvvvvzzzzzzzzzzz"
d = {}
for i in str:
    if i in vow:
        d[i] = d.get(i,0) + 1
print("The dict is")
print(d)

bc = {}
for i in str:
    if i in bc:
        bc[i] = bc[i] + 1
    else:
        bc[i]=1
print(bc)


a = Counter(str)
print(type(a))
b = dict(a)
print(b)

