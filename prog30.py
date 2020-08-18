#to create a list by taking input from the user
lst=[]
n=int(input("enter the number of elements:\n"))
for i in range(0,n):
    ele=int(input("enter elements:\n"))
    lst.append(ele) #adding element in list

print(lst)
