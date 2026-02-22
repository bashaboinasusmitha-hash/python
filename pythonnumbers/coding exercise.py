num=int(input("enter any number:"))
if num<0:
    print("Negative number")
else:
    print("postive number")
#printing cube and squares:
a=2
print(a**2)
print(a**3)
print(pow(2,3))
print(pow(2,2))
#finding absolute value of number without abs():
a=-20
print(a*(-1))
#converting a float number to integer and print  both values:
num=20.4
a=int(num)
print(a)
print(num)
#checking a even or odd number using normal and bitwise operator
num=int(input("enter a number :"))
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")
#using bitwise operator
if num&1:
    print("odd")
else:
    print("even")
#finding largest number 
li=[1,7,3]
largest=li[0]
for i in li:
    if i>largest:
        largest=i
print(largest)
#count how many digits are in  number
num=int(input("enter a number: "))
count=0
if num==0:
    count=1
else:
    while num>0:
        num=num//10
        count+=1
print("no. of digits in number is ",count)
#reeversing a number
num=int(input("enter a number: "))
rev=0
while num>0:
    digits=num%10
    rev=rev*10+digits
    num=num//10
print("the reverse number is ",rev)
#swapping of numbers:
a=int(input("enter a number :"))
b=int(input("enter a number :"))
a,b=b,a
print(a,b)
#problems on random numbers:
#generating a random number between 1 and 50:
import random
print(random.randrange(1,51))
#printing a random floating between 5 and 10
print(random.uniform(5,10))
#printing random element from a list
li=[10,20,30,40,50]
print(random.choice(li))
#generating a even number between 1 and 100
print(random.randrange(2,101,2))
#Generate 5 random numbers between 1 and 20 (repetition allowed).
numbers=random.choices(range(1,21),k=5)
print(numbers)
#Generate 5 unique random numbers between 1 and 20 (no repetition).
print(random.sample(range(1,21),5))