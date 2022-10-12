import operator
from collections import Counter
from operator import itemgetter
from operator import countOf



str = "aaaaaaaaaabbbbbbbbbbcccccccccccedeeeeeeeeeeeeeeee"

abcd = Counter(str)
ls = dict(abcd)
print(ls)

d = operator.countOf(str,'a')
print(d)
