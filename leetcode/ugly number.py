'''n=8
if n==1:
    print("true")
else:
    for i in range(2,n):
        if n%i==0:
            if i not in [2,3,5]:
                print("false")
                break
    else:
        if i in  [2,3,5]:
            print("true")
        else:
            print("false")'''
#ugly number:
'''An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
Given an integer n, return true if n is an ugly number.'''
n=8
if n==1:
    print(True)
for i in [2,3,5]:
    while n%i==0:
        n=n//i
print(n==1)#true