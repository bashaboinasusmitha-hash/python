# No Arguments and No Return Value:
'''Write a Python function to print "Welcome to Python" using no arguments and no return value.'''
def greet():
    print("Welcome to Python")#Welcome to Python
greet()
#Arguments but No Return Value
'''Write a function that accepts two numbers and prints their sum.'''
def add(a,b):
    c=a+b
    print(c)#5
add(3,2)
#No Arguments but Return Value
'''Write a function that returns the value of π (3.14) and print it.'''
def pie():
    return 3.14
x=pie()
print(x)
#Arguments and Return Value
'''Write a function that accepts length and breadth and returns the area of a rectangle.'''
def rectangle(length,breadth):
    area=length*breadth
    return area
a=rectangle(5,2)
print(a)
#Built-in functions:
#len() Function
'''Write a program using len() to find the length of a string entered by the user.'''
def length(name):
    n=len(name)#8
    return n
a=length("susmitha")
print(a)