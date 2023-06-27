#Program for the use of break statement
# a="Urvi"
# for i in a:
#     if i== "v":
#         break  #interrupts; the loop exits from the loop
#     else:
#         print(i)

#Program for the use of continue statement
# a="Urvi"
# for i in a:
#     if i=="v":
#         continue# skips the current iteration and goes to the next iteration
#     else:
#         print(i)

#Program for the use of pass statement
# a="Urvi"
# for i in a:
#     if i == "v":
#         pass# used as a null statement
#     else:
#         print(i)

#Program for for with else 
# a="Urvi"
# for i in a:
#     if i=="r":
#         continue
#     else:
#         print(i)
# else:
#     print("It has a continue statement")

#Program for while with else

i=1
while i<=10:
    if i == 5:
        i+=1
        pass
    else:
        print(i)
    i+=1 
else:
    print("It has break")

