from itertools import permutations
from itertools import product
from itertools import combinations

test1 = ["abc","def"]
test2 = permutations(test1[0],2)
print(list(test2))

test2 = product(test1[0],repeat=3)
test2 = list(test2)
print(test2)
test3=[]
for i in test2:
    test3.append("".join(i))

print(test3)
