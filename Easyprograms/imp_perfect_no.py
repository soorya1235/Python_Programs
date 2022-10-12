''''
A perfect number is on whos multiple of number and it sum is equal to 0

example 6 : 1,2,3 = 1+2+3=6  6==6
'''

def isperfectnumber(number):
    sum=0
    for i in range(1,number):
        if number%i==0:
            sum = sum + i
    return sum == number

number = int(input("Enter the number"))
print("Is perfect" if isperfectnumber(number) else "Ncot a Perfect Number")