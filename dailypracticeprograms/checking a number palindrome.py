#checking a number palindrome
x=10
temp=x
rev=0
while x>0:
    digits=x%10
    rev=rev*10+digits
    x=x//10
print(rev)
if temp==rev:
    print("true")
else:
    print("false")