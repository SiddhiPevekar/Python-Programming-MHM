#program to search the number of times a particular number occurs in a list
list1=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    x=int(input("enter any element:"))
    list1.append(x)
print(list1)
count=0
y=int(input("enter the element to be searched:"))
for j in list1:
    if j==y:
        count+=1
print(count)
    
