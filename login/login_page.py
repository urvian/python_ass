def login_p():
    import tkinter as tk
    import webbrowser as wb
    from Exception import number
    import gui as g
    import util as u
    
    root=tk.Tk()
    root.title("login")
    #title
    head=tk.Label(root,text="Login",font=("Britannic Bold",45))
    head.grid()
    #username
    username=tk.Label(root,text="Username",font=("Britannic Bold",30))
    username.grid()
    e1=tk.Entry(root,font=("Franklin Gothic Medium",30),width=30,bg="#f7cf79")
    e1.grid()
    #password
    password=tk.Label(root,text="Password",font=("Britannic Bold",30))
    password.grid()
    e2=tk.Entry(root,font=("Franklin Gothic Medium",30),width=30,bg="#f7cf79",show="*")
    e2.grid()
    def display():
        if e2["show"]=="*":
            e2["show"]=""
        else:
            e2["show"]="*"
    cb=tk.Checkbutton(root,text="Show Password",command=display)
    cb.grid()
    l3=tk.Label(root,text=" ",font=("Franklin Gothic Medium",25))
    l3.grid()
    def file():
        username=e1.get()
        password=e2.get()
        try:
            # f=open("login_back.txt","r")
            credentials=u.read_credentials()
            if f"Username: {username}\nPassword: {password}\n" in credentials:
                g.navigate()
            else:
                l3["text"]="Invalid Username or Password!! PLease Try Again. "
                raise number("Either the username or password is invalid")
        except number as n:
            print(n.args[0])
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(e)
    b=tk.Button(root,text="Login",font=("Franklin Gothic Medium",15),command=file,bg="#f7cf79",activebackground="blue")
    b.grid()
    tk.mainloop()
login_p()
