#program to find numbers divisible by 7 but not multiple by 5 between 2000 and 3200 and append them in list
list1=[]
for i in range(2000,3201):
    if (i%7==0) and (i%5!=0):
        list1.append(str(i))
print(','.join(list1))#join is the function of string, we join all the elements of list using comma and removing list brackets and string ''
