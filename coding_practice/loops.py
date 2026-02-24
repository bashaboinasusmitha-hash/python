#printing 1 to 100 numbers
for i in range(1,101):
    print(i)
#sum of n numbers:
n=int(input("enter any number :"))
ans=0
for i in range(1,n+1):
    ans+=i
print(ans)
#printing multiplication table:
n=int(input("enter a number :"))
for i in range(1,11):
    table=n*i
    print(f"{n}  * {i} = {table}")
#reversing a number:
n=int(input("enter a number :"))
rev=0
if n==0:
    rev=0
while n>0:
    digits=n%10
    rev=rev*10+digits
    n=n//10
print(rev)
#count digits in a number:
number=int(input("enter a number :"))
count=0
if number==0:
    count=1
else:
    while number>0:
        number=number//10
        count+=1
print(count)