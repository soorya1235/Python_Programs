from operator import countOf
from collections import Counter

str = "aeeeeeeeiiiiiiiiioooooooouuuuuuuuusssss"
vow ={"a","e","i","o",'u'}
output ={}
for i in str:
    if i in vow:
        output[i] = output.get(i,0) + 1
print(f"The output is {output}")

str1="aaaaaaaaaaabbbbbbbbbbbbccccccccccddddddeeeeeeeeef"
output1 = {}

for i in str1:
    if i in output1:
        output1[i] = output1[i] + 1
    else:
        output1[i] =1
print(f"The output1 is {output1}")

d1 =Counter(str)
print("The no of occures of character using counter fuctions is")
print(dict(d1))

print(f"The of a in str is {countOf(str,'i')}")