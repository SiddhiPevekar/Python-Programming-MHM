#define a function that can accept two strings as input and print the string with maximum length, if they have same length them print both the strings
s1=input("enter any string:\n")
s2=input("enter any string:\n")
def string(s1,s2):
    len1=len(s1)
    len2=len(s2)
    if len1>len2:
        print(s1)
    elif len2>len1:
       print(s2)
    else:
        print(s1,s2)
string(s1,s2)
