from collections import Counter
dic1 = {"a":1,"b":2,"c":3}
keys = dic1.keys()
val = dic1.values()
print(keys)
print(val)

list = [x for x in dic1.keys()]
print(list)

string = "today is raining a lot"
print(Counter(string))


str = string.split(" ")
print(str)
length = {}
for i in str:
    length[i] = len(i)
print(length)

x = {x:len(x) for x in str}
print(x)


