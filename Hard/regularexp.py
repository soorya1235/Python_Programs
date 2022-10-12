import re

str="this is the final string"
s1= re.search(r't\w\w',str)
print(s1.group())

s2=re.findall(r'\w\w\w',str)
print(s2)

s3=re.split(r'\s',str)
print(s3)

s4=re.sub(r'\w\w\w','cool',str)
print(s4)

s5=re.match(r't\w\w\w',str)
print(s5.group())

s6=re.search(r'\b',str)
print(s6.group())