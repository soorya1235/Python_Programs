'''
A number is special number if the sum of digit and product of digits is equal to original no
'''
number = int(input("Enter the number"))
digit1 = number %  10
digit2 = number // 10
result = (digit1+digit2) + (digit1*digit2)
print("Special 2 Digit No" if result==number else "Not a special 2 digit number")