from operator import itemgetter
from collections.abc import Iterator
from collections.abc import Iterable

l1 = [1,2,3,4,5]
if isinstance(l1,Iterable):
    print("yes it is Iterable")
else:
    print("No it is not Iterable")

if isinstance(l1,Iterator):
    print("yes it is Iterator")
else:
    print("No it is not Iterator")
print(dir(l1))

if "__next__" in dir(l1):
    print("it is present")
else:
    print("it is not present")