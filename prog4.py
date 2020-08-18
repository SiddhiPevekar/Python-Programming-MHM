#PROGRAM TO FIND THE UNION OF TWO LISTS
list1=[]
x=int(input("enter the number of elements:"))
for i in range(1,x):
    n=int(input("enter the element:"))
    list1.append(n)
print(list1)
list2=[]
y=int(input("enter the number of element:"))
for j in range(1,y):
    m=int(input("enter the element:"))
    list2.append(m)
print(list2)
u=list(set().union(list1,list2))
print(u)

