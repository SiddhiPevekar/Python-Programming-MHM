#program to check if a given key exists in the dictionary or not
a={}
n=int(input("enter the number of elements: "))
for i in range(n):
    k=input("enter the keys: ")
    v=int(input("enter the values: "))
    a.update({k:v})
print(a)
y=input("enter the key to check: ")
if y in a.keys():
    print("key is present and value of the key is: ")
    print(a[y])
else:
    print("key isn't present")
