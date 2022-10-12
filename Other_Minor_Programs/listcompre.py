#{x:y for x,y in dic.items()}
#{x:y**2 for x,y in dic.items() if x%2==0 or condition}
#{if/else condition for x,y in dic.items}

dic1={"a":2,"b":4,"c":5,"d":6,"e":7,"f":8,"g":9,"h":10,"i":11}

d1 = {x:y**2 for x,y in dic1.items()}
print(d1)

d2={x:"true" if y%2==0 else "false" for x,y in dic1.items()}
print(d2)