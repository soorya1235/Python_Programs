from abc import ABCMeta,abstractmethod
class test(metaclass=ABCMeta):

    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass

    def add(self,a,b):
        return a-b

class test3(test):

    def method1(self):
        print("methood1")

    def method2(self):
        print("method2")

    def method4(self):
        print("Method 4 called")

    def add(self,a,b):
        return a+b

a1 = test3()
print(a1.add(30,20))