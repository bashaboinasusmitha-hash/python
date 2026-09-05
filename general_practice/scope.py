'''there are 2 types of scopes in python:local,global scope'''
#local scope:local scope is the variable which  can be accessed only by the inside of the function.
#global variable: the variable declared at outside of the function and evry one can access the variable.
#example:
a=15#global
def display():
    a=10 # local
    print(a)#10
display()
print(a)#15

a=27
def display():
    print(a)#27 it prints 10 because here there is no variable "a" so it access the global variable
display()
print(a)#27

a=10
def div():
    n=78
    def res():
        print(n)#78 
    res()
div()
print(a)#10