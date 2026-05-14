#lambda function:
'''lambda functions are anynomous function which means function without a name.Used for simple operations and written in a single line.'''
#squaring a number:
square=lambda x:x*x
print(square(5))#25
#cubing a number:
cube=lambda x:x**3
print(cube(4))#64
#adding of two same numbers:
add=lambda x:x+x
print(add(6))#12
#adding of two different numbers:
add=lambda x,y:x+y
print(add(2,3))#5
#multiplying numbers:
mul=lambda x,y:x*y
print(mul(2,5))#10
#lambda without arguments:
greet=lambda:"hey susmitha!"
print(greet())
#Lambda with Conditional Expression
largest=lambda a,b: a if a>b else b
print(largest(4,3))#4