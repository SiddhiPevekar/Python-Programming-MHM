#factorial(recursion)
x=int(input("enter any number:\n"))
def fact(x):
    if x==0:
        return 1
    else:
        return (x*fact(x-1))
print(fact(x))
    
