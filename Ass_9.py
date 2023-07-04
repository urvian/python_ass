import math
class divisionBy5 (Exception):
        def __init__(self,message):
            super().__init__(message)
class operations:
    def mathFunctions(self,a,b):
        print("The ceil is:",math.ceil(a))
        print("The floor is:",math.floor(a))
        print("The absolute value is:",math.fabs(a))
        print("The square root is:",math.sqrt(a))
        print("The sum is:",math.fsum([a,b]))
        #factorial
        fact=1
        for i in range(1,b+1):
            fact=fact*i
        print("the factorial is", fact)
        #fibonacci
        m=0
        n=1
        for i in range(a):
            print(m,end=" ")
            m,n=n,m+n
        #reverse of a number
        rev=0
        while a>0:
            last=a%10
            rev=(rev*10)+last
            a//=10
        print("The reverse of the number is",rev)
        print("The gamma is:",math.gamma(b))
        print("is the number infinity:",math.isinf(b))
        print("value of a to the power of b",math.pow(a,b))
    # mathFunctions(10,5)
    def Trig(self,a):
        print("The sin is:",math.sin(a))
        print("The cos is:",math.cos(a))
        print("The tan is:",math.tan(a))
    # Trig(5)
    def Arithmatic(self,a,b):
        print("addition of a and b is",a+b)
        print("Subraction of a and b is",a-b)
        print("Multiplication of a and b is",a*b)
        (a/b)
        try:
            raise divisionBy5("You are trying to divide by 5")
        except divisionBy5 as d:
            print(d.args[0])
        print("floor division of a and b is",a//b)
        print("Modulus of a and b is",a%b)
        print("Exponential of a and b is",a**4)
    # Arithmatic(10,5)
    def SetOp(self,a,b):
        set_union = a.union(b)
        print("set union is:",set_union)
        set_intersection = a.intersection(b)
        print("set intersection is:",set_intersection)
        set_difference = a.difference(b)
        print("set difference is:",set_difference)
        set_symdiff = a.symmetric_difference(b)
        print("set symmetric difference is:",set_symdiff)
    # m={1,2,3,4,5}
    # n={6,7,3,8,1}
    # SetOp(m,n)
    def Log(self,x):
        print("The log1p",math.log1p(x))
        print("the log2",math.log2(x))
        print("the log10 is",math.log10(x))
        print("The log is",math.log(x))
    # Log(10)
