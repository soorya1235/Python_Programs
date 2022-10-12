def binarysearch(list,n):
    l=0
    h=len(list) - 1

    pos =0

    while l <= h:
        mid = (l+h) //2
        if list[mid] == n:
            globals()['pos'] = mid
            return mid
        if n > list[mid]:
            l = mid + 1
        else:
            h = mid -1
    return False

lst = [1,2,3,4,5,6,7,8,9,10]
s = binarysearch(lst,8)
print(s)
print(pos)




