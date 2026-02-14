#calculation of bmi taking prompt for user 
weight=input("Enter your weight in kgs:")
height=input("Enter your height in meters:")
a=int(weight)
b=float(height)
bmi=a/b**2
print(bmi)
bmi=a//b**2
print(bmi)
#practice questions regarding importance of bodams rule
print(5+2*3-1+10/5)
#conversion of temp from celsius to fahrenheit
temp=float(input("Enter the temperature in celsius:"))
fahrenheit=(temp*9/5)+32
print(fahrenheit)
#claculation of simple interest
p=int(input("enter principle amount:"))
t=int(input("enter the time in years:"))
r=float(input("enter the rate of interest:"))
si=(p*t*r)/100
print(f"total simple interest is {si}")
#coverting total seconds to hours,min,remaining seconds
seconds=int(input("Enter the total seconds:"))
hours=seconds//3600
remain_secs=seconds%3600
mins=remain_secs//60
remaining_secs=remain_secs%60
print(f"the total hours is {hours}")
print(f"the total minutes are {mins}")
print(f"remaining seconds are {remaining_secs}")
