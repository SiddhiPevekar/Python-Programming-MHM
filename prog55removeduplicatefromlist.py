#to remove duplicate from a list
mylist=[]
n=int(input("enter the number of elements of the list:\n"))
for i in range(n):
    p=input("enter the element of the list:\n")
    mylist.append(p)
print(mylist)
#print(set(mylist))
mylist=(dict.fromkeys(mylist))
print(mylist)
mylist=list(dict.fromkeys(mylist))
print(mylist)
