#reversing a list
x=[]
def reverse(x):
    n=int(input("enter the number of elements: "))
    for i in range(n):
        a=int(input("enter the element: "))
        x.append(a)
    x.reverse()
    return x
reverse(x)
print(x)

