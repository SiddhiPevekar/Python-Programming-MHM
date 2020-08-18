#program to check whether number is armstrong number or not
n=int(input("enter any number: "))
a=list(map(int,str(n)))    #to convert int into str and list it
b=list(map(lambda x:x**3,a))   #to multiply each element in string by 3 of list a
print(a)
print(b)
if(sum(b)==n):
    print("armstrong number")
else:
    print("not a armstrong number")
