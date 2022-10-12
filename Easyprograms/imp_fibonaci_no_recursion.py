def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = int(input("Enter the number"))
for i in range(0,number):
    print(fibonacci(i),end=" ")