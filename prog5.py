#intersection of two lists
l1=[]
n=int(input("enter the number of elements:"))
for i in range(1,n):
    a=int(input("enter the element:"))
    l1.append(a)
print(l1)
l2=[]
m=int(input("enter the number of elements:"))
for j in range(1,m):
    b=int(input("enter the element:"))
    l2.append(b)
print(l2)
mylist=list(set(l1)&set(l2))
print(mylist)
