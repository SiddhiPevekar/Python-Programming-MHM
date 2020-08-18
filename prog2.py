#PROGRAM TO PUT EVEN AND ODD ELEMENTS IN A LIST INTO TWO DIFFERENT LISTS
list1=[]
n=int(input("enter the number of elements:\n"))
for i in range(1,n+1):
    a=int(input("enter the element:\n"))
    list1.append(a)
even=[]
odd=[]
for j in list1:
    if (j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("list of even elements is: {}".format(even))
print("list of odd elements is: {}".format(odd))
