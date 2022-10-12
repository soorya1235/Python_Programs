import operator

str="aaaaaaaaaaabbbbbbbbbbbbbcccccccccddddddddddddeeeeeeeeeeeffffffffffggggg"
d1 = {}
for i in str:
    if i in d1:
        d1[i] = d1[i] + 1
    else:
        d1[i]=0
print(d1)

string ="aeiou"
print("".join(list(reversed(string))))

length = len(string) -1
print(length)

temp=""
while length >= 0:
    temp = temp + string[length]
    length = length -1
print(temp)

abcd = "aaaaaaaaaabbbbbbbbbbbbbbbc"
a1 = operator.countOf(abcd,'c')
print(a1)

l1 = "abcd this is cool"
length = l1.split(" ")
print(length)

i = {x:len(x) for x in length}
print(i)

