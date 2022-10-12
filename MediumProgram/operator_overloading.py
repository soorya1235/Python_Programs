class stu:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self, other):
        m1 = self.a + other.a
        m2 = self.b + other.b
        return m1 + m2


a1 = stu(10,20)
a2 = stu(30,40)
print(a1+a2)