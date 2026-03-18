#Intersection of two arrays:
nums1=[1,2,2,1]
nums2=[2,2]
nums1=set(nums1)
nums2=set(nums2)
print(nums1)
print(nums2)
a=nums1.intersection(nums2)
print(list(a))
#palindrome check:
x=120
temp=x
rev=0
while x>0:
    digits=x%10
    rev=rev*10+digits
    x=x//10
if temp==rev:
    print("Palindrome")
else:
    print("Not a palindrome")
#or :
def isPalindrome(x):
    if x < 0:
        return False#if negative number it give false
    temp = x
    rev = 0
    while x > 0:
        digits = x % 10
        rev = rev * 10 + digits
        x = x // 10
    return temp == rev #if number temp==rev returns True else False
print(isPalindrome(121))
# or:
x = int(input("enter a number:"))
if x < 0:
    print("Not a palindrome")
else:
    temp = x
    rev = 0
    while x > 0:
        digits = x % 10
        rev = rev * 10 + digits
        x = x // 10
    if temp == rev:
        print("Palindrome")
    else:
        print("Not a palindrome")