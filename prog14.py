#program to input a string and print the characters in even indices in reverse form
s=input("input any string:\n")
s=s[::2] #as slicing makes changes in copy of string, so we need to store that copy in some variable, same applies to list
print("string with even indices is: {}".format(s))
s=s[::-1] #as slicing makes changes in copy of string, so we need to store that copy in some variable, same applies to list
print("reverse string is: {}".format(s))

