n = 1634  # or n=int(input()) -> taking input from user
s = n  # assigning input value to the s variable
b = len(str(n))
print(b)
sum1 = 0
while n != 0:
    r = n % 10
    print("The value of r is",r)
    sum1 = sum1+(r**b)
    n = n//10
    print("The value of n is",n)
if s == sum1:
    print("The given number", s, "is armstrong number")
else:
    print("The given number", s, "is not armstrong number")