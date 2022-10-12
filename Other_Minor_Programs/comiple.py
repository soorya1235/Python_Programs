str="a=10\nb=20\nsum=a+b\nprint(sum)"
c = compile(str,"test.txt",'exec')
exec(c)
x=100
print(eval('x+100'))