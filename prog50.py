#program to print even numbers in a list
list1=[]
n=int(input("enter the number of elements: "))
for i in range(n):
    x=int(input("enter the element: "))
    list1.append(x)
print(list1)
i=0
while(i<len(list1)):
    if (list1[i]%2==0):
        print(list1[i],end=" ")
    i+=1
