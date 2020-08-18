#program to find sum of the digits without using recursion
n=int(input("enter any number"))
l=[]
while n!=0:
    x=n%10
    l.append(x)
    n=n//10
print(sum(l))
    
    
      
