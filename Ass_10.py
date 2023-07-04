import tkinter as tk
import webbrowser as wb
obj=tk.Tk()
e=tk.Entry(obj,width=30,font=("Times New Roman",30))
e.grid()
def display():
    s=e.get()
    print(s+"navigating to youtube")
    wb.open("https://www.youtube.com/results?search_query="+s)
b=tk.Button(obj,text="Find YouTube",font=("Times New Roman",30),command=display,bg="white",activebackground="blue",)
b.grid(row=3,column=0)
def display1():
    g=e.get()
    print(g+"navigating to netflix")
    wb.open("https://www.netflix.com/search?q="+g)
b1=tk.Button(obj,text="Find Netflix",font=("Times New Roman",30),command=display1,bg="#d94136",activebackground="blue")
b1.grid(row=4,column=0)
def display2():
    f=e.get()
    print(f+"navigating to primevideo")
    wb.open("https://www.primevideo.com/search/ref=atv_sr_sug_10?phrase="+f)
b2=tk.Button(obj,text="Find Primevideo",font=("Times New Roman",30),command=display2,bg="#19c9e0",activebackground="blue")
b2.grid(row=5,column=0)
def display3():
    a=e.get()
    print(a+"navigating to wikipedia")
    wb.open("https://en.wikipedia.org/w/index.php?search=&title="+a)
b3=tk.Button(obj,text="Find Wikipedia",font=("Times New Roman",30),command=display3,bg="#f7cf79",activebackground="blue")
b3.grid(row=6,column=0)
obj.mainloop()
