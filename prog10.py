#PROGRAM TO EXCHANGE THE VALUES OF TWO NUMBERS WITHOUT USING A TEMPORARY VALUE
a=int(input("enter the element: "))
b=int(input("enter the element: "))
a=a+b
b=a-b
a=a-b
print("after swapping the values of a and b are {},{}".format(a,b))
