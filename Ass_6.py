def ds(roll,name):
    ls=[]
    ls.append((roll,name))
    t=(roll,name)
    s=set()
    s={(roll,name)}
    d={
        "roll":roll,
        "name":name
    }
    ls[0] = (5,"Swati")
    t=(5,"swati")
    s.pop()
    s.add((5,"Swati"))
    d["roll"]=5
    d["name"]="Swati"
    print("The list is:",ls)
    print("The list is:",t)
    print("The list is:",s)
    print("The list is:",d)
    del(ls)
    del(t)
    del(s)
    del(d)
    print(ls)
    print(t)
    print(s)
    print(d)
ds(12,"Urvi")
