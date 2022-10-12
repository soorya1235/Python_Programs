import json

with open("jsondata.txt","r") as f:
    d = json.load(f)
print(d)
print(type(d))


with open("jsondumps.txt","w") as w:
    w.write(json.dumps(d))
