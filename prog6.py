#program to remove duplicate items from the list
list1=[]
n=int(input("enter the number of elements in the list:\n"))
for i in range(1,n+1):
    x=int(input("enter the element: "))
    list1.append(x)
print("the list is:\n{}".format (set(list1)))
