import re

with open("data.txt","r") as f:
    data = f.readlines()


for i in data:
    #print(i)
    s = re.search(r'\d{0,4}\.\d{0,4}\.{0,4}\.\d{0,4}',i)
    if s != None:
        print(s.group())
