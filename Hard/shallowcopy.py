from copy import deepcopy,copy
# a=[1,2,3]
# b=a
# print(a)
# a[0]="soorya"
# print(a)c
# print(b)
# print(id(a))
# print(id(b))

a1=[[1,2,3],[4,5,6]]
b2=copy(a1)
print(id(a1))
print(id(b2))
a1.append([3,4,5])
print(a1)
print(b2)
# a1[0]=[4,4,4]
# print(a1)
# print(b2)
# print(id(a1))
# print(id(b2))
#
# from copy import copy
# v1=[[1,2,3],[4,5,6]]
# v2=copy(v1)
# print(id(v1))
# print(id(v2))
#
# v3=[1,2,3]
# v4=v3
# print(id(v3))
# print(id(v4))