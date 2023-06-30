def ds(roll,name):
    ls=[]
    ls.append((roll,name))
    print("The list is:",ls)
    t=(roll,name)
    print("The tuple is:",t)
    s=set()
    s={(roll,name)}
    print("The set is:",s)
    d={
        "roll":roll,
        "name":name
    }
    print("The dictionary is:",d)
    ls[0] = (5,"Swati")
    t=(5,"swati")
    s.pop()
    s.add((5,"Swati"))
    d["roll"]=5
    d["name"]="Swati"
    print("The updated list is:",ls)
    print("The updated tuple is:",t)
    print("The updated set is:",s)
    print("The updated dictionary is:",d)
    # del(ls)
    # del(t)
    # del(s)
    # del(d)
    # print(ls)
    # print(t)
    # print(s)
    # print(d)
ds(12,"Urvi")
