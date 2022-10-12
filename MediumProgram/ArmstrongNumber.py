number = 153
temp = number
s = str(temp)
ln = len(s)
print(ln)
sum=0

while number != 0:
    m = number%10
    print(m)
    sum = sum + (m**ln)
    number = number//10

if sum == temp:
    print("Arm strong number")
else:
    print("Not an Arm strong number")