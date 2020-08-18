#program to read a number n and compute n+nn+nnn
n=int(input("enter any number:\n"))
temp=str(n)#as we can add tthem directly but using str we can join them
t1=temp+temp #string
t2=temp+temp+temp#string
compute=n+int(t1)+int(t2) #so here we need to change it to number
print(compute)
