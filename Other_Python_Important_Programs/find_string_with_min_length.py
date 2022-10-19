# find the string with minimum length
s = min("GfG", "Geeks", "GeeksWorld", key = len)
m = max("GfG", "Geeks", "GeeksWorld", key = len)
print(s)
print(m)

abc = [('a',10),('b',5),('c',1)]
print(min(abc))
print(max(abc))

#printing the mininum key that is c
a = min(abc,key = lambda x : x[1])
print(a)

#printing the maximum key tha is having the highest value.
b = max(abc,key = lambda x:x[1])
print(b)