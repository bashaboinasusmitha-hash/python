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
#Keyword Argument Questions
#Student Information
'''Write a function to display student name, age, and course using keyword arguments.'''
def student_details(name,age,course):
    return name,age,course
print(student_details(age=24,name="susmitha",course="CSM"))
print(student_details("tharun",age=26,course="ECE"))
print(student_details(course="CSE",age=23,name="ramadevi"))
#Variable-Length Argument Questions
#Write a function using *args to calculate the sum of multiple numbers.
def add(*numbers):
    c=0
    for i in numbers:
        c+=i
    return c
print(add(1,5,3,2,6,7))
#Largest Number using *args
'''Write a function using *args to find the largest among given numbers.'''
def largest(*numbers):
    great=numbers[0]
    for i in range(len(numbers)):
        if great<numbers[i]:
            great=numbers[i]
    return great
print(largest(1,5,3,8,0,1,6))
#Write a function using **kwargs to display employee details.
def employee(**details):
    for key,value in details.items():
        print(key,value)
employee(name="susmitha",age=25,id=10,salary=25000)