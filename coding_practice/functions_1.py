#palindrome check
def palindrome(name):
    n=len(name)
    name=list(name)
    print(name)
    for i in range(n//2):
        if name[i]!=name[n-i-1]:
            return ("not a palindrome")
    return "palindrome"
print(palindrome("nana"))
#count upper case:
'''def uppercase(name):
    name=list(name)
    n=len(name)
    count=0
    for i in range(n):
        if name[i]==name[i].upper():
            count+=1
        if name[i]!=name[i].upper():
            count=0
    return count
print(uppercase("sUSmitha"))'''
def uppercase(name):
    count=0
    for i in name:
        if i.isupper():
            count+=1
    return count
print(uppercase("SUSmitha"))