#program to find number occurances in a list
def count(lst,x):
    
    count=0
    for ele in lst:
        if ele==x:
            count=count+1
    return count
lst=[]
n=int(input("enter the number of elements: "))
for i in range(1,n+1):
    p=int(input("enter the elements of list: "))
    lst.append(p)
x=int(input("enter the number to be found: "))
print("{} has occurred {} times".format(x,count(lst,x)))
    
            
    
