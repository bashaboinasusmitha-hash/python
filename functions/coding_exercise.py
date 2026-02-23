#programs:
def person_info(name,age=18,*marks):
    sum=0
    for i in marks:
        sum=sum+i
    if len(marks)>0:
        avg=sum/(len(marks))
    else:
        avg=None
    return name,age,avg
result=person_info("susmitha",20,21,23,25)
print(result)
#checking even or odd:
def even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
result=even_odd(10)
print(result)
#largest of three numbers:
def largest(a,b,c):
    largest=a
    if largest<b:
        largest=b
    if largest<c:
        largest=c
    return (largest)
print(largest(3,7,5))
#simple interest:
def SI(p,t,r):
    si=(p*t*r)/100
    return si
print(SI(20000,2,3))
#default argument practice
def std(name,city="hyderabad"):
    return(f"hello {name},are u from {city} ?" )
result=std("rama")
print(result)
#using *args printing largest number:
def largest(*args):
    largest=args[0]
    print(args)
    for i in args:
        if largest<i:
            largest=i
    return largest
result=largest(1,7,3,9,5)
print(result)
#**kwargs :
def student(**kwargs):
    return kwargs
print(student(name="susmitha",age=20,dept="cse-aiml",year=3))
#sum of first n natural numbers using recursion:
def add(n):
    return n*(n+1)//2
print(add(5))
#recursive function for factorial:
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
print(fact(3))
#fibonacci series
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
for i in range(5):
    print(fib(i),end=" ")