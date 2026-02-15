#salary increment and decrement
salary=25000
increase=salary*(10/100)
decrease=salary*(5/100)
salary+=increase
print(f"The salary after increment {salary}")
salary-=decrease
print(f"the salary after decrement {salary}")
#continous division
num=1000
while num > 10:
    num//=2
    print(num)