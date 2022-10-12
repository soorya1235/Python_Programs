'''
A number is niven if the number divided by sum of digits is 0
'''

number = int(input("Enter the number"))
temp=number
sum=0
while number!=0:
    no = number % 10
    sum = sum + no
    number = number // 10

print("Niven no" if temp%sum==0 else "Not Niven")

