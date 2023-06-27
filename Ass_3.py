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
     

