n=1634
s=n
l=len(str(n))
sum=0
while n!=0:
    r = n%10
    sum = sum + (r**l)
    n = n//10

if sum == s:
    print("ARm strong number")
else:
    print("Not arm storng")