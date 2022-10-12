number = int(input("Enter the number"))
temp = number
reversed_no = 0
while number!=0:
    no = number % 10
    reversed_no = reversed_no * 10 + no
    number = number // 10
print(f'The Reversed Number is {reversed_no}')

if reversed_no == temp:
    print(f'Palindrome')
else:
    print(f'Not a palindrome')