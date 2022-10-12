d1={"a":1,"b":2,"c":{"e":1,"f":2,"g":3}}
for x in d1.keys():
    if type(d1[x]) is dict:
        print(f"x is dictionary")
        for x,y in d1[x].items():
            print(f"key is {x} and value is {y}")
    else:
        print(f"key is {x} and value is {d1[x]}")

