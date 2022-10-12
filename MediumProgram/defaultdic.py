from collections import defaultdict

v1 = defaultdict(lambda : "key not present")
v1['a'] = 1
v1['b'] = 2
v1['c'] = 3
print(v1)
print(v1['a'])
print(v1['x'])

for i,v in v1.items():
    print(f"key is {i} and value is {v}")