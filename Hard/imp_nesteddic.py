a={"a":1,"b":2,"c":{"e":5,"f":6}}
for key in a.keys():
    if type(a[key]) is dict:
        print(f"{key} is a dictionary item")
        for i,v in a[key].items():
            print(f"The key is {i} and vaue is {v}")
    else:
        print(f"key is {key} and value is {a[key]}")