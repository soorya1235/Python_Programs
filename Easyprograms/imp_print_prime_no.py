'''
A number is prime if it is divisbile 1 or itself..but should not be divisible by other in between them
'''
'''
Below is the example of for-else loop.....
'''
start = int(input("Enter the start"))
end = int(input("Enter the end"))

for i in range(start,end+1):
    if i > 1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")