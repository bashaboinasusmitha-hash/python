''' functions:functions are the block of reusable code that performs a specific task.
instead of writimg same code again and again,here we write it once inside a function and call it whenever needed
syntax: 
def function name(parameters):
   function body
   return expression
function name(arguments)
return expression and parameters are optional.
*There are two types of functions : built in function and user defined function.
*built in functions are already defined in python ex:print(),input()
*user defined functions are user will defined as per requirement.
y we use functions : code reusability,reduce repition,better readability'''
def greet():
    print("hi")
    print("susmitha")
#without declaring function it prints nothing
#types based on arguments and return
#No arguments No return
def greet():
    print("Hi",end=" ")
    print("Susmitha")
greet()#hi susmitha
greet()#hi susmitha
#functions with arguments and No return:
def greet(name):
    print(f"hello {name}")
greet("susmitha")
def greet(name,branch):
    print(f"hello {name}")
    print(f"are u from {branch} branch")
greet("susmitha","csm")
def add(a,b):
    e=a+b
    print("the addition is ",e)
add(2,5)
add(3,5)
#functions with No arguments,with Return :
def get_value():
    return 10
x=get_value()
print(x)#10
#Arguments with Return:
def multiply(a,b):
    return a*b
res=multiply(3,2)
print(res)#without print statement it will print nothing
print(multiply(2,3))
#variables:
#local variables: they are defined inside a function
#global variables : they are defined outside a function
x=10#global variable
def show():
    x=5#local variable
    print(x)#5
show()
print(x)#10
#lambda functions:it taks only one argument
squares=lambda x:x*x
print(squares(5))#25
addition=lambda x:x+x
print(addition(2))#4
print(addition(2))
#recursion:a function call itself
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(1))
#nested functions : functions inside function
def outer():
    def inside():
        print("hello")
    inside()
outer()
#pass statement:used when function body is empty
def greet():
    pass
#docstring: used to describe a function
def add(a,b):
    """this function add two numbers"""
    return a+b
print(add.__doc__)#this function add two numbers
#difference between return and print:
#return:stores and reuses the values,it sends the value back to function call
#print():it displays the value
#after return the function stop execution.
def test():
    return 10
    print("hello")#it will not print 