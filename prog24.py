#leap year(number divisible by 4 and 400 is leap year and year divisible by 4 and 100 is not a leap year)
year=int(input("enter any leap:\n"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))
