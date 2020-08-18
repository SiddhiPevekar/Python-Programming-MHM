#PROGRAM TO MERGE TWO LISTS AND SORT IT
list1=[]
list2=[]
n=int(input("enter the number of elements:\n"))
for i in range(1,n+1):
    x=int(input("enter the element:\n"))
    list1.append(x)
m=int(input("enter the number of elements:\n"))
for i in range(1,m+1):
    y=int(input("enter the element:\n"))
    list2.append(y)
my_list=list1+list2
my_list.sort()
print(my_list)
