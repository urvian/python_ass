import tkinter as tk
import webbrowser as wb
root=tk.Tk()
root.title("Audible")
#fname
l1=tk.Label(root,text="First Name:",font=("Bahnschrift Condensed",30))
l1.grid()
fname=tk.Entry(root,font=("Bahnschrift Condensed",30),width=30,bg="#f7cf79")
fname.grid()
#lname
l2=tk.Label(root,text="Last Name:",font=("Bahnschrift Condensed",30))
l2.grid()
lname=tk.Entry(root,font=("Bahnschrift Condensed",30),width=30,bg="#f7cf79")
lname.grid()
l6=tk.Label(root,text="Contact Number:",font=("Bahnschrift Condensed",30))
l6.grid()
num=tk.Entry(root,font=("Bahnschrift Condensed",30),width=30,bg="#f7cf79")
num.grid()
#content
l3=tk.Label(root,text="The book or podcast that you viewed on social media",font=("Bahnschrift Condensed",30))
l3.grid()
cont=tk.Entry(root,font=("Bahnschrift Condensed",30),width=30,bg="#f7cf79")
cont.grid()
#site
l4=tk.Label(root,text="The site from which you got to about the book or podcast:",font=("Bahnschrift Condensed",30))
l4.grid()

websites = {
    "Instagram":"instagram",
    "YouTube":"youtube",
    "Facebook":"facebook"
}
def show():
    wb.open("https://help.audible.com/s/global-search/kch%20u?language=")
def store():
    u=fname.get()
    l=lname.get()
    n=num.get()
    c=cont.get()
    selected_website = website_var.get()
    url = websites.get(selected_website)
    f=open("Backend.txt","+a")
    f.writelines(["\nFirst name:",u,"\nLast name:",l,"\nContact number:",n,"\nBook or Podcast name",c,"\nSite name=",url])
    f.close()
website_var=tk.StringVar(root)
website_var.set(list(websites)[0])
def Exec():
    show()
    store()

website_dropdown=tk.OptionMenu(root,website_var,*websites)
website_dropdown.config(bg="#f7cf79")
website_dropdown.grid()
l5=tk.Label(root,text=" ")
b=tk.Button(root,text="Submit",font=("Bahnschrift Condensed",15),command=Exec,bg="#f7cf79",activebackground="blue")
b.grid(row=14)
tk.mainloop()
