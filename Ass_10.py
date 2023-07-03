import tkinter as tk
import webbrowser as wb
obj=tk.Tk()
e=tk.Entry(obj,width=30,font=("Times New Roman",30))
e.grid()
def display():
    s=e.get()
    print(s+"navigating to youtube")
    wb.open("https://www.youtube.com/results?search_query="+s)
b=tk.Button(obj,text="Find",font=("Times New Roman",30),command=display,bg="purple",activebackground="blue")
b.grid(row=1,column=0)
obj.mainloop()
