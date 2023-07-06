def register():
    import tkinter as tk
    import webbrowser as wb
    root=tk.Tk()
    root.title("Register")
    #title
    head=tk.Label(root,text="Register",font=("Britannic Bold",45))
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
        f=open("login_back.txt","+a")
        f.write(f"\nUsername: {username}\nPassword: {password}\n")
        l3["text"]="Data Updated Successfully, Thankyou!!"
        f.close()
    b=tk.Button(root,text="Register",font=("Franklin Gothic Medium",15),command=file,bg="#f7cf79",activebackground="blue")
    b.grid()
    tk.mainloop()
# register()
