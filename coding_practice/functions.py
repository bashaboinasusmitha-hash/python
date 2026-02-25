#find maximum of two numbers:
def maximum(a,b):
    return max(a,b)
print(maximum(10,3))
def maximum(a,b):
    largest=a
    if largest<b:
        largest=b
    return largest
print(maximum(10,2))
#factorial :
def fact(n):
    ans=1
    for i in range(n,0,-1):
        ans=ans*i
    return ans
print(fact(5))
#factorial ussing recursion 
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(5))
#fibonacci series:using recursion
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
for i in range(5):
    print(fib(i),end=" ")   
#fibonacci :
def fib(n):
    a=0
    b=1
    for i in range(n):
        a,b=b,a+b
    return a
print(fib(5))