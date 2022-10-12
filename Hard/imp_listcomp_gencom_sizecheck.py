import sys
g2 = [x**2 for x in range(0,100)]
g1 = (x**2 for x in range(0,100))
print(sys.getsizeof(g1))
print(sys.getsizeof(g2))