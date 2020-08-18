#program to count the number of times the number price occurs in a string and if it occurs next to punctuation and capital
s=input("enter any string: ")
def count(s):
    count=0
    for word in s.lower().split():
        if 'price' in word:
            count=count+1
    return count

print(count(s))

