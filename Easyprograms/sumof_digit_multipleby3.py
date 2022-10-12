num = int(input("Enter a number "))
result = 0
if num <=0:
    print(f"{num} invalid number")
else:
    while num != 0:
        d = num % 10
        if d in (3,6,9):
            result += d

        num //= 10

    print(f"sum of digits- multiples of 3: {result}")