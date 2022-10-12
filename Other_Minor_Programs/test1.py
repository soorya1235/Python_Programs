import operator

x = lambda x: x**3
print(x(3))

x = [x for x in range(0,20) if x%2==0]
print(x)

x = [x**2 for x in range(0,10)]
print(x)

x =["true" if x%2==0 else "false" for x in range(0,10)]
print(x)

d ={"a":1,"e":2,"f":9,"g":4,"h":5,"i":10}
print(d.keys())
print(d.values())

d1 = {x:y+1 for x,y in d.items()}
print(d1)

d2 = {x:y**3 for x,y in d.items()}
print(d2)

d3 = {x:y for x,y in d.items() if y%2==0}
print(d3)

d4 = {x:"true" if y%2==0 else "false" for x,y in d.items()}
print(d4)

d1 = [x for x in d1.keys()]
print(d1)

a1 = ["abcd","ggg","hhh","iii","qqq"]
d2 = {x:len(x) for x in a1}
str = "abcdefghaaaaaaaaaabbbbbbbbbbbbbbbccccccccccccccccdddddddddddddddddou"
from collections import Counter
d1 = Counter(str)
print(d1)

dict1={}
vow = {"a","e","i","o","u"}
for i in str:
    if i in vow:
       dict1[i] = dict1.get(i,0) + 1

print("the dict1 is")

print("The dict1 is",dict1)