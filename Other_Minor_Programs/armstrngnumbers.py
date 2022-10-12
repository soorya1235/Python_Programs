# program to check arm strong number

number=153
temp=number
str=str(number)
length=len(str)
sum=0

while number != 0:
    m = number % 10
    sum = sum + (m**length)
    number = number // 10

if sum == temp:
    print("It is arm strong number")
else:
    print("It is not arm strong number")
