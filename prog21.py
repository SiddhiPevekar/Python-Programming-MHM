#program to generate random numbers from 1 to 20 and append them in list
import random
a=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    a.append(random.randint(1,20))
print("randomised list is:{}".format(a))
