from itertools import permutations
from itertools import combinations
from itertools import product

str = "abc"

p1 = permutations(str,3)
print(p1)
print(type(p1))
count=0
for i in p1:
    print("".join(i))
    count+=1
print(count)
#
# p2 = product(str,repeat=3)
# count = 0
# for i in p2:
#     print("".join(i))
#     count+=1
# print(count)
#print(f"The length of permutation is {len(list(p2))}")

p1 = combinations(str,3)
print(p1)
print(type(p1))
count=0
for i in p1:
    print("".join(i))
    count+=1
print(count)
