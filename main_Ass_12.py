import login.login_page as l
import login.register as r
while True:
    print("1.Register\
           \n2.login")
    print("If you want to register with us press1 \n if you are already registered with us press 2 to login")
    In=int(input("Enter your choice"))
    if In==1:
        r.register()
        print("After you are registered you can go back or cancel the window to go to the login page")
    elif In==2:
        l.login_p()
    
