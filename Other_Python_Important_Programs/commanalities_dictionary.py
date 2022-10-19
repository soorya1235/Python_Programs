a = {
 'x' : 1,
 'y' : 2,
 'z' : 3
}
b = {
 'w' : 10,
 'x' : 11,
 'y' : 2
}

#keys which are common.
print("Keys which are common")
print (a.keys() & b.keys())

#Find keys which are in A but not in B
print("Keys which are in A but not in B")
print(a.keys() - b.keys())

#Find (key,value) pairs in common
print(a.items() & b.items())

