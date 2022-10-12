number = int(input("Enter the number"))
sum=0
while number!=0:
    no = number % 10
    if no in (2,3,5,7):
        sum = sum + no
    number = number // 10
print(f'The sum is {sum}')

