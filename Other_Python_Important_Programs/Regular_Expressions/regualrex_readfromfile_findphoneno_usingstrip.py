import re

with open("data.txt","r") as f:
   # data = f.readlines()
   data = [line.rstrip() for line in f]

print(data)
data = str(data)
print(type(data))
print(data)
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

matches = pattern.finditer(data)
#
# for match in matches:
#     print(match)

