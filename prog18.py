#program to check if a number is a palindrome
n=int(input("enter any number"))#if at the end of the number is 0, the prog will not give correct output
rev=0
c=n
while n!=0:
    a=n%10
    rev=rev*10+a
    n=n//10
print(rev)
if c==rev:
    print("{} is palindrome".format(c))
else:
    print("{} is not a palindrome".format(c))
    
