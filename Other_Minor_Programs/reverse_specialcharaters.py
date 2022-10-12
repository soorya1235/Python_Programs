strSample = 'abc/defh$ij$'

listsample = list(strSample)
length = len(listsample) - 1
i=0
j=length -1

while i < j:
    if not listsample[i].isalpha():
        i+=1
    elif not listsample[j].isalpha():
        j-=1
    else:
        listsample[i],listsample[j] = listsample[j],listsample[i]
        i+=1
        j-=1

print("original string is",strSample)
print("Reverse String is","".join(listsample))
