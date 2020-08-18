#program to generate all the divisors of an integer
x=int(input("enter any element:\n"))
l1=[]
for i in range(1,x+1):
    if(x%i==0):
        l1.append(i)
print("the divisors of the element are:",l1)
print("the divisors of the element are:{}".format(set(l1)))
        
