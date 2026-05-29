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
#Write a function to find largest element in a list.
def largest(*kwags):
    maxi=kwags[0]
    for i in range(len(kwags)):
        if kwags[i]>maxi:
            maxi=kwags[i]
    return maxi
print(largest(2,5,3,7,8,9))
'''Write a lambda function for:
Square of number
Even or odd
Maximum of two numbers'''
square=lambda x:x**2
print(square(2))
even_odd=lambda x:"even" if x%2==0 else "odd"
print(even_odd(6))
max_min=lambda x,y: x if x>y else y
print(max_min(5,7))
#Write a function with default arguments.
def default(a,b="susmitha"):
    print(a,b)
ans=default(2)
#Write a function using *args.
def add(*args):
    a=sum(args)
    return a
print(add(2,3,5,6))
#Write a function using **kwargs.
def details(**kwags):
    return kwags
print(details(name="susmitha",roll_no=6624))