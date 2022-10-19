import re

str ="aaaaaabeffbhcccaaaaaa"
find =re.compile('a')
s = find.findall(str)
print(s)