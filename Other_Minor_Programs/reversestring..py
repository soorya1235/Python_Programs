sample = 'abc/defh$ij$'
listsample = list(sample)
i=0
j=len(listsample)-1

while i<j:
    if not listsample[i].isalpha():
        i += 1
    elif not listsample[j].isalpha():
        j -= 1
    else:
        listsample[i],listsample[j] = listsample[j],listsample[i]
        i += 1
        j -= 1
print(listsample)
print("Original Sample is",sample)
print("Reversed Sample is","".join(listsample))
