li = [99,1,67,4,9,0,1,4444,45]
str = "111111111111222222222224444444444444555555555555555"
for i in range(len(li)-1):
    for j in range(len(li)-1):
        if li[j] > li[j+1]:
            temp = li[j]
            li[j] = li[j+1]
            li[j+1] = temp
print("The sorted list",li)


from collections import Counter
a1 = dict(Counter(str))
print(a1)