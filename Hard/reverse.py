str ="abcdefgh"
print("".join(list(reversed(str))))

len = len(str) -1
tmp = ""
while len >=0:
    tmp = tmp + str[len]
    len-=1

print(f"The reversed string is {tmp}")
