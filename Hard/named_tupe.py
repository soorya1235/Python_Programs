from collections import namedtuple

cust = namedtuple('cust',['v1','v2','v3'])
cust = cust("one","two","three")
print(cust.v1)
print(cust.v2)
print(cust.v3)

