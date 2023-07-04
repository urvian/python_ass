import Ass_9 as a
obj=a.operations()
while True:
    print("Press 1 if you want to perform numeric operations\
    \nPress 2 if you want to perform trignometric operations\
    \nPress 3 if you want to perform arithmatic operations\
    \nPress 4 if you want to perform set operations\
    \n Press 5 to perform logarithmic operations")
    In=int(input("Enter your choice"))
    if In==1:
        obj.mathFunctions(10,5)
        j=int(input("If you want to exit press 1 else press 0"))
    elif In==2:
        obj.Trig(2)
        j=int(input("If you want to exit press 1 else press 0"))
    elif In==3:
        obj.Arithmatic(20,10)
        j=int(input("If you want to exit press 1 else press 0"))
    elif In==4:
        m={1,2,3,4,5}
        n={6,7,3,8,1}
        obj.SetOp(m,n)
        j=int(input("If you want to exit press 1 else press 0"))
    elif In==5:
        obj.Log(10)
        j=int(input("If you want to exit press 1 else press 0"))
    else:
        print("Invalid Option")
    if j==1:
        exit()
