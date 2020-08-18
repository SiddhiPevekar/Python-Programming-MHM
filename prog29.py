#to remove duplicate from a list
lst=[]
n=int(input("enter the number of elements:\n"))
for i in range(n):
    x=input("enter elements:\n")
    lst.append(x)

lst=(dict.fromkeys(lst))
print(lst)
lst=list(dict.fromkeys(lst))#this prints in list form
print(lst)
#print(set(lst)) this prints in the form of set
