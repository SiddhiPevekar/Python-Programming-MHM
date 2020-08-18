#PROGRAM TO REMOVE NTH INDEX CHARACTER FROM A NON-EMPTY STRING (without function)
x=input("string")
n=int(input("enter the index of the element to be removed:"))
first=x[:n]
last=x[n+1:]
print(first+last)
