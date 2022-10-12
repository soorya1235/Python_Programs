class employee:

    no_of_employee = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        employee.no_of_employee+=1

    @classmethod
    def method_clas(cls,name,age):
         return cls(name,age+20)

    @staticmethod
    def check_age(age):
        if age > 10:
            return "minor"
        else:
            return "major"
    def __repr__(self):
        return f"The name is {self.name} and age is {self.age}"

    @property
    def checkage(self):
        if self.age > 18:
            return "major"
        else:
            return "minor"


e1 = employee("soorya",10)
# print(employee.no_of_employee)
# employee.no_of_employee=100
# print(employee.no_of_employee)
# print(e1.name)
# print(e1.age)

e2 = e1.method_clas("sss",10)
print(e2)

e3= e1.method_clas("abcd",20)
print(e3)

e4 =employee.method_clas("singam",40)
print(e4)