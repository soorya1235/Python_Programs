number = int(input("Enter the number"))
sum_of_even = 0
sum_of_odd = 0

while number!=0:
    no = number % 10
    if no%2==0:
        sum_of_even = sum_of_even + no
    else:
        sum_of_odd = sum_of_odd + no
    number = number // 10
print(f'Sum of Even is {sum_of_even} and Sum of Odd is {sum_of_odd}')
