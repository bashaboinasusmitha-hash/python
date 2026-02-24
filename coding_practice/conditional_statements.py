#largest of three numbers:
nums=list(map(int,input("enter three numbers :").split()))
largest=nums[0]
if largest<nums[1]:
    largest=nums[1]
if largest<nums[2]:
    largest=nums[2]
print(largest)
#split():used to separate the numbers
#map():used to convert evry value to integer
#we can write as:
num1=int(input("enter a number"))
num2=int(input("enter second number:"))
num3=int(input("enter third number :"))
largest=num1
if largest<num2:
    largest=num2
if largest<num3:
    largest=num3
print(largest)
#or else :
nums=(input("enter three numbers:").split())
num1=int(nums[0])
num2=int(nums[1])
num3=int(nums[2])
largest=num1
if largest<num2:
    largest=num2
if largest<num3:
    largest=num3
print(largest)
#leap year check:
year=int(input("Enter a year :"))
if year%4==0 and year%100!=0 or year%400==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} not a leap year")
#grade calculator 
marks=int(input("enter a marks :"))
if marks>=90:
    print("A grade")
elif marks>=75 and marks<=89:
    print("B grade")
elif marks>=50 and marks<=74:
    print("C grade")
else:
    print("Fail!")
#identifying postive or neagtive or zero  
num=int(input("enter a number :"))
if num>0:
    print(f"{num} is postive number")
elif num<0:
    print(f"{num} is negative number")
else:
    print(f"{num} is zero")
#divisible by 5 and 11:
num=int(input("enter a number :"))
if num%5==0 and num%11==0:
    print("Divisible by both")
else:
    print("Not divisible by both")   
