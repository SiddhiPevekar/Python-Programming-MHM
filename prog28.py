#FIND THE LENGTH OF LIST AND SWAP 1ST ELEMENT WITH N-1 ELEMENT
x=[1,2,3,4]
size=len(x)
print(size)
temp= x[0]
x[0]=x[size-1]
x[size-1]=temp
print(x)
