#Demonstation of the use of Operators
#1) Arithmatic Operator
# a=20
# b=10
# print("addition of a and b is",a+b)
# print("Subraction of a and b is",a-b)
# print("Multiplication of a and b is",a*b)
# print("division of a and b is",a/b)
# print("floor division of a and b is",a//b)
# print("Modulus of a and b is",a%b)
# print("Exponential of a and b is",a**4)

#2) Assignment Operator
# x=2
# x+=1
# print("The use of +=",x)
# x-=1
# print("The use of -=",x)
# x*=1
# print("The use of *=",x)
# x/=1
# print("The use of /=",x)
# x//=2
# print("The use of //=",x)
# x**=2
# print("The use of **=",x)
# x%=2
# print("The use of %=",x)

# 3) Comparison or relational Operator
# a=10
# b=20
# print("Greater than operator",a>b)
# print("Less than operator",a<b)
# print("Equal to than operator",a==b)
# print("Not Equal to than operator",a!=b)
# print("Greater than Equal to operator",a>=b)
# print("Less than Equal to operator",a<=b)

#4) Logical Operator
# a=True
# b=False
# print("Logical and Operator",a and b)
# print("Logical or Operator",a or b)
# print("Logical not Operator",not b)

#5) Bitwise Operator
# a=10
# b=5
# print("Bitwise And Operator",a & b)
# print("Bitwise Or Operator",a | b)
# print("Bitwise Xor Operator",a ^ b)
# print("Bitwise Shift Left Operator",a << b)
# print("Bitwise Shift Right Operator",a >> b)

# 6) Identity Operator
# a=10
# b=10
# print("is Identity Operator", a is b)
# print("is not Identity Operator", a is not b)

#7) Special or Membership Operator
# str="UrviAN"

# print("in Speacial Operator","U" in str)
# print("not in Speacial Operator","A" not in str)

# Calculator

i=True
while(i==True):
    print("For addition press +")
    print(      "For subraction press -")
    print(      "For multiplication press *")
    print(      "For division press /")
    print(      "For floor division press //")
    print(      "For exponential press **")
    print(      "For modulus press %" )
    In=input("Enter the symbol for that particular operation")
    if In == "+":
        a=int(input("Enter the first number"))
        b=int(input("Enter the second number"))
        result=a+b
        print(result)
        j=int(input("If you want to exit press 1 else press 0"))
    elif In == "-":
        a=int(input("Enter the first number"))
        b=int(input("Enter the second number"))
        result=a-b
        print(result)
        j=int(input("If you want to exit press 1 else press 0"))
    elif In == "*":
        a=int(input("Enter the first number"))
        b=int(input("Enter the second number"))
        result=a*b
        print(result)
        j=int(input("If you want to exit press 1 else press 0"))
    elif In == "/":
        a=int(input("Enter the first number"))
        b=int(input("Enter the second number"))
        result=a/b
        print(result)
        j=int(input("If you want to exit press 1 else press 0"))
    elif In == "//":
        a=int(input("Enter the first number"))
        b=int(input("Enter the second number"))
        result=a//b
        print(result)
        j=int(input("If you want to exit press 1 else press 0"))
    elif In == "**":
        a=int(input("Enter the number"))
        n=int(input("Enter the raise to (^) number"))
        result=a**n
        print(result)
        j=int(input("If you want to exit press 1 else press 0"))
    elif In == "%":
        a=int(input("Enter the first number"))
        b=int(input("Enter the second number"))
        result=a%b
        print(result)
        j=int(input("If you want to exit press 1 else press 0"))
    if(j==1):
        exit()
    else:
        i==True
     

