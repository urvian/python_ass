# 1)Single Inheritance
class PrivateAccessError(Exception):
        def __init__(self,message):
            super().__init__(message)
class A:
    def __init__(self,a,b,c):
        self.__a=a
        self._b=b
        self.c=c
    def display1(self):
        print(self.__a)
        print(self._b)
        print(self.c)

class B(A):
    
        def display1(self):
            try:
                raise PrivateAccessError("You are trying to access private member of class A") 
                    
            except PrivateAccessError as d:
                print(d.args[0])
                print(self._b)
                print(self.c)
                # super().display1()

# a=A(4,5,6)
# a.display1()

b=B(1,2,3)
b.display1()





