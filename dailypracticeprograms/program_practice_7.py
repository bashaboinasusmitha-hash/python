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
#while loop:
#Reverse a number.
number=67
rev=0
while number>0:
    digits=number%10
    rev=rev*10+digits
    number=number//10
print(rev)
#Check palindrome number.
number=505
rev=0
x=number
while number>0:
    digits=number%10
    rev=rev*10+digits
    number=number//10
if rev==x:
    print("Numberis a palindrome")
else:
    print("Not a palindrome.")
#Count number of digits in a number.
number=3456
count=0
while number>0:
    number=number//10
    count+=1
print(count)
#Find Armstrong number.
number=153
temp=number
lenght=len(str(number))
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**lenght
    temp=temp//10
if sum==number:
    print("Armstrong number.")
else:
    print("Not an Armstrong number.")