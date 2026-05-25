#Loop Programs
#for loop:
#Print numbers from 1 to 100.
for i in range(1,101):
    print(i)
#Print multiplication table of a number.
number=5
for i in range(1,11):
    a=number*i
    print(number,"*",i,"=",a)
#Find factorial of a number.
number=3
result=1
if number==0 or number==1:
    print(1)
else:
    for i in range(2,number+1):
        result*=i
    print(result)
#Print Fibonacci series.
n=5
a,b=0,1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
print()
#Find sum of digits of a number.
number=56
number=str(number)
sum=0
for i in number:
    print(i)
    sum+=int(i)
print(sum)