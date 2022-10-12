'''
duck no is number which will not have 0
'''

number = int(input("Enter the number"))
is_duck = False
while number!=0:
    no = number % 10
    if no == 0:
        is_duck = True
        break
    number = number // 10
if is_duck:
    print(f'It is Duck number')
else:
    print(f'It is not Duck number')

