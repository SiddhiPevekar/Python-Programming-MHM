#wap which can map() filter() to make a list whose elements are square of even numbers in [1,2,3,4,5,6,7,8,9,10]
givenlist=[]
n=int(input("enter the number of elements of a list: "))
for i in range(0,n):
    x=int(input("enter the element: "))
    givenlist.append(x)
print(" the list is: {}".format(givenlist))
even=list(filter(lambda p:p%2==0,givenlist))
print(even)
sq=list(map(lambda p:p**2,even))
print(sq)
