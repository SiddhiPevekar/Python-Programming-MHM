#merging two dictionaries
c={}
n=int(input("enter the number of elements:\n"))
for i in range(n):
    k=int(input("enter the number of keys:\n"))
    v=(input("enter the number of values:\n"))
    c.update({k:v})
print("dictionary is:\n{}".format(c))
d={}
n=int(input("enter the number of elements:\n"))
for i in range(n):
    k=int(input("enter the number of keys:\n"))
    v=(input("enter the number of values:\n"))
    d.update({k:v})
print("dictionary is:\n{}".format(d))
p={**c,**d}
print(p)
 
