import re

pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
with open("data.txt","r") as f:
    data = f.read().splitlines()
    #data = f.read()

print(data)
print(type(data))

#if we do f.read and splitlines,it will create a list and in that list we cannot search search for the match,
#so we need to convert it to string

data = str(data)

matches = pattern.finditer(data)

for match in matches:
    print(match)

