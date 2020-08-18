#reversing a list without using reverse function(using list slicing trick ie.-1 )
x=[]
def reverse(x):
    n=int(input("enter the number of elements: "))
    for i in range(n):
        a=int(input("enter the element: "))
        x.append(a)
    y=x[::-1] #this reverses the copy of the list and not the original list so we need to store that copy in some variable and then print it
    return y

result=reverse(x)
print(result)

