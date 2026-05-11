#default argument function questions:
#default salary:
'''write a function to display employees details where salary has a default value of 25000.'''
def employee(name,age,salary=25000):
    return name,age,salary
a=employee("susmitha",25,27000)
b=employee("tharun",25)
print(a)
print(b)
#Write a function greet() with default argument "Guest".
def greet(Greet="Guest"):
    return Greet
print(greet())