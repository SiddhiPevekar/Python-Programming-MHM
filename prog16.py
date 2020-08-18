#program to reverse a number
n=int(input("enter any number:\n"))
rev=0
while(n!=0):
    a=n%10
    rev=rev*10+a
    n=n//10
print("reverse of a number:{}".format(rev))
