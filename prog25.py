#program to print all the  numbers divisible by given number in a given range
lower=int(input("enter any lower limit:\n"))
upper=int(input("enter any upper limit:\n"))
n=lower=int(input("enter any number:\n"))
for i in range(lower,upper+1):
    if(i%n==0):
        print(i)
    
