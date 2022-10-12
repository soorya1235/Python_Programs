strSample = 'abc/defh$ij$'
listsample = list(strSample)
i=0
j=len(strSample)-1

while i < j:
    if not listsample[i].isalpha():
        i+=1
    elif not listsample[j].isalpha():
        j-=1
    else:
        listsample[i],listsample[j]=listsample[j],listsample[i]
        i+=1
        j-=1

print(f"Original string is {strSample}")
print("".join(listsample))
