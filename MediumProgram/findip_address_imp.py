import re
with open("testdata.txt","r") as f:
    data = f.readlines()

#print(data)
print(len(data))
string = str(data)
print(type(string))
#print(string)

#result = re.search(r'\d\d:\d\d:\d\d:\d\d',string)

str= "Subnet Mask . . . . . . . . . . . : 255.255.255.0"
s = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',str)
print(s.group())

# list1 = []
for i in data:
    s = re.search(r'\d{0,4}\.\d{1,4}\.\d{1,4}\.\d{1,4}',i)
    if s != None:
       print("IP Address Found",s.group())

