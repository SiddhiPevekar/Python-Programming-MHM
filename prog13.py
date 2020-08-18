#program to shuffle and print the list
from random import shuffle #random.shuffle() is used to shuffle string and list
l=[]
x=int(input("enter the no of elements:"))
for i in range(x):
    n=int(input("enter any element:"))
    l.append(n)
shuffle(l)
print(l)

