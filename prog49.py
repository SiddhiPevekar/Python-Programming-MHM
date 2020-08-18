#program to get numbers divsible by 15 from a list
lst=[]
n=int(input("enter the number of elements: "))
for i in range(n):
    x=int(input("enter the element: "))
    lst.append(x)
result=list(filter(lambda p:(p%15==0),lst))#this p if x even gives the same answer
print(result)
