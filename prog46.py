#program to print positive numbers in given range
start=int(input("enter the start of the range: "))
end=int(input("enter the end of the range: "))
for num in range(start,end+1):
    if num>=0:
        print(num,end=" ")
