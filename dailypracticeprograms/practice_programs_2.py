#temperature conversion:
temp=float(input("enter a temperature in celsius:"))
formula=(9/5)*temp+32
print("the temperature in fahreinheit is:",formula)
#swapping of numbers with third variable and without variable:
a=32
b=45
a,b=b,a
print("a is :",a)
print("b is :",b)
num_1=34
num_2=54
temp=num_1
num_1=num_2
num_2=temp
print("number one is :",num_1)
print("number two is:",num_2)
#Write a program to calculate simple interest.
principle_amount=int(input("enter amount:"))
time=float(input("enter a time in years:"))
rate_of_interst=float(input("enter a rate of interest:"))
formula=(principle_amount*time*rate_of_interst/100)
print("the interest of total amount is :",formula)
#Write a program to check whether a year is a leap year.
year=int(input("enter a year:"))
if year%4==0  and year%100!=0 or year%400==0:
    print("year is a leap year")
else:
    print("not an leap year.")