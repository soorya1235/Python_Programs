number = 1634
temp = number
s=str(number)
length = len(s)
print(length)
sum=0
while number != 0:
    m = number % 10
    sum = sum + (m**length)
    number = number // 10

if number == temp:
    print("It is arm strong number")
else:
    print("It is not arm strong number")