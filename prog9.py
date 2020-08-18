#PROGRAM TO PRINT LARGEST EVEN AND LARGEST ODD IN THE LIST
list1=[]
x=int(input("enter the number of elements: "))
for i in range(x):
    n=int(input("enter the element: "))
    list1.append(n)
print(list1)
even=[]
odd=[]
for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(max(even))
print(max(odd))
