#functions:
#Write a function to add two numbers.
def add(a,b):
    c=a+b
    return c
print(add(2,4))
#Write a function to check whether a number is prime.
def prime(number):
    if number<=1:
        return "not a prime number"
    else:
        for i in range(2,number+1):
            if i%2==0:
                return "not a prime number"
    return "prime number"
print(prime(5))
#Write a recursive function for factorial.
def fact(number):
    if number==0 or number==1:
        return 1
    else:
        return number*fact(number-1)
print(fact(5))