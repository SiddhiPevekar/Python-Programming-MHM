#program to count positive and negative numbers in a list
x=[]
pos_count=0
neg_count=0
n=int(input("enter the number of elements:\n"))
for i in range(n):
    a=int(input("enter the element:\n"))
    x.append(a)
for num in x:
    if num>=0:
        pos_count+=1
    else:
        neg_count+=1
print(pos_count)
print(neg_count)
        
