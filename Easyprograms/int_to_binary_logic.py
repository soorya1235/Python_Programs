number = int(input("Enter the number"))
binary_number = []
while number!=0:
    binary_number.append(number%2)
    number = number //2

binary_number.reverse()
print(f'The Binary number is')
for i in range(len(binary_number)):
    print(binary_number[i],end="")