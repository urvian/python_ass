
#ls=[input(),input(),input(),input(),input()]
n=int(input("Enter the number of elements of the list"))
ls=[]
for i in range(n):
    a=int(input())
    ls.append(a)
print("sum is:",sum(ls))
print("The smallest number is:",min(ls))
print("The Largest number is:",max(ls))
ls.sort()
print("The Ascending order is:",ls)
ls.sort(reverse=True)
print("The Descending order is:",ls)

for i in enumerate(ls):
    print(i)

del(ls)
print(ls)