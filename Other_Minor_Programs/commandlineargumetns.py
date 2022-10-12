import sys
print(sys.argv)
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])

def abcd(*args,**kwargs):
    print(args)
    print(kwargs)
    print(type(args))
    print(type(kwargs))


abcd(10,20,a=10,b=20)


