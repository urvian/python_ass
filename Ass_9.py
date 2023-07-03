import math
class divisionBy5 (Exception):
        def __init__(self,message):
            super().__init__(message)
class operations:
    
    def mathFunctions(self,a,b):
        print("The ceil is:",math.ceil(a))
        print("The floor is:",math.floor(a))
        print("The factorial is:",math.factorial(a))
        print("The absolute value is:",math.fabs(a))
        print("The square root is:",math.sqrt(a))
        try:
            (a/b)
            raise divisionBy5("You are trying to divide by 5")
        except divisionBy5 as d:
            print(d.args[0])
        print("The sin is:",math.sin(b))
        print("The cos is:",math.cos(b))
        print("The tan is:",math.tan(b))
        print("The gamma is:",math.gamma(b))
        print("is the number infinity:",math.isinf(b))
        print("The sum is:",math.fsum([a,b]))
        print("Subraction of a and b is",a-b)
        print("Multiplication of a and b is",a*b)
        print("floor division of a and b is",a//b)
        print("Modulus of a and b is",a%b)
        print("Exponential of a and b is",a**4)

    # mathFunctions(10,5)
