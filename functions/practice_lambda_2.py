#Prime Number
'''Write a function to check whether a number is prime or not.'''
def prime_checker(number):
    if number<=1:
        return("not prime")
    elif number<=0:
        return("not defined")
    else:
        for i in range(2,number):
            if number%i==0:
                return("number is not prime")
        else:
            return("number is prime")
a=prime_checker(6)
print(a)
#Palindrome
'''Write a function to check whether a string is a palindrome'''
def palindrome(num):
    rev=0
    temp=num
    while num>0:
        digit = num%10
        rev=rev*10+digit
        num=num//10
    if temp==rev:
        return("palindrome")
    else:
        return ("not a palindrome")
a=palindrome(606)
print(a)