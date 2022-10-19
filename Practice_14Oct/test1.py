str1 = "aeeeeeeeeeeeeeiiiiiiiiiiiiooooooooooooooooouuuuuuuuuuuuuuuusssssssssssssssttt"
vowels = {"a","e","i","o","u"}
count_vow = dict()
for i in str1:
    if i in vowels:
        count_vow[i] = count_vow.get(i,0) + 1

print("The no of vowles are")
print(count_vow)


count_all = dict()

for i in str1:
    if i not in count_all:
        count_all[i] =  1
    else:
        count_all[i] = count_all[i] + 1

print("The cound of all vowels are",end="\t")        
print(count_all)

    