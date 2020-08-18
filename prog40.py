#program to read height in cms and convert it to feet and inches
cm=int(input("enter the height in centimeters:\n"))
feet=0.394*cm
inches=0.0328*cm
print("the length in feet is",round(feet,2 ))#this two will keep decimal places upto two
print("the length in inches is",round(inches,2))
