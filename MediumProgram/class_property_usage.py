class test:

    exams = 0

    def __init__(self,maths,stats):
        print(f"Constructor is called...")
        self.maths = maths
        self.stats = stats

    @classmethod
    def method_class(cls):
        cls.exams+=1


    @staticmethod
    def method_static():
        return 100

    @property
    def get_marks(self):
        return self.maths + self.stats


a1 = test(30,40)
a1.method_class()
test.method_class()
# a1.method_static()
# test.method_static()
# print("printing using class variable.")
#print(test.get_marks)
print(a1.get_marks)
