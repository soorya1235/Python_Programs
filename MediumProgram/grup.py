import itertools

# l1 = [('a',1),('a',2),('b',1),('b',2)]
# for k,g in itertools.groupby(l1,lambda x : x[0]):
#     print(k,":",list(g))

a1 = [
    {
        "city": "bangalore",
        "population" : 1000,
        "region":"south"
    },
    {
        "city":"mumbai",
        "population":2000,
        "region":"north"
    },
    {
        "city":"chennai",
        "population":3000,
        "region":"south"
    },
]

d1 = {}
for k,g in itertools.groupby(a1,lambda x : x["region"]):
    print(k,list(g))
   
