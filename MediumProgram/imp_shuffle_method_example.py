import copy
import random


list1= [1,5,2,9,66,44,23,21,66]

list2 = copy.deepcopy(list1)
list2.sort()
# print(list1)
# print(list2)
random.shuffle(list1)
global length
length = len(list1)

def check_sorted(list1,list2,length):
    for i in range(0,length):
         random.shuffle(list1)
         if list1 == list2:
             print(f"List is sorted at {i} location")
             break
         else:
          print(f"List is not sorted,Below are the original and Sorted to compare")
          print(f"Original List is {list1}")
          print(f"Sorted list is {list2}")

temp = length
global i
i=0
j=i

for i in range(temp):
    print(length)
    #print(j)
    a=list1.pop(j)
    #print(list1)
    b=list2.pop(j)
    # print(a,"popped out from list1")
    # print(b,"popped out from list2")
    #print(list2)
    temp = len(list1)
    temp = temp -1
    print(f"List size is {temp}")
    check_sorted(list1,list2,length)
