#Square using Lambda
square=lambda n:n*n
print(square(6))#36
#Write a lambda function to add two numbers.
addition=lambda a:a+a
print(addition(3))#6
#Write a program to sort a list of tuples based on second element using lambda function
li=[(1,2),(8,1),(1,0)]
li.sort(key=lambda x:x[1])
print(li)#[(1, 0), (8, 1), (1, 2)]
#Factorial using Recursion
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        res=n*fact(n-1)
        return res
a=fact(5)
print(a)
#Write a recursive function to print Fibonacci series up to n terms.
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
n=6
for i in range(n):
    print(fib(i),end=" ")
print()
#Write a recursive function to find sum of digits of a number.
def add(n):
    sum=0
    while n>0:
        digits=n%10
        sum+=digits
        n=n//10
    print(sum)
add(201)