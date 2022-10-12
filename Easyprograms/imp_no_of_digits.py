number = int(input("Enter the number"))
count = 0
while number!=0:
    number = number // 10
    print(number)
    count = count + 1
print(f'The count of digit is {count}')    