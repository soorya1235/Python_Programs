number = int(input("Enter the number"))

print(bin(number))
print("With out the 0b character")
print(bin(number).replace("0b",""))

print("Removig the ob using sices")
print(bin(number)[2::])