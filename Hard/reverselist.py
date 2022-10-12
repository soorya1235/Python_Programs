abcd = ["abc","bcc","def"]
output = []
for i in range(0,len(abcd)):
    output.append(abcd[i][::-1])
print("The reversed output in list is",output)


str="this is cool"
str1 = str.split(" ")
print(str1)

found = str.find("iss",0,len(str)-1)
print(found)