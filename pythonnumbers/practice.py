'''here are three numeric types in python:
int,float,complex'''
x=1
y=2.4
z=1j
print(type(x))#int
print(type(y))#float
print(type(z))#complex
'''int or integer is a whole number,positive or negative,
without decimals,of unlimited length'''
x=1
y=35656222554887711
z=-3255522
print(type(x))#int
print(type(y))#int
print(type(z))#int
'''float,or floating point number is a number ,positive or 
negative,containing one or more decimals.float can also be scientific number with an
"e" to indicate the power of 10.'''
x=1.20
y=1.0
z=-35.59
print(type(x))
print(type(y))
print(type(z))
x=35e3
y=12E4
z=-87.7e100
print(type(x))
print(type(y))
print(type(z))
''' complex numbers are written with "j" as the imaginary part'''
x=3+5j
y=5j
z=-5j
print(type(x))
print(type(y))
print(type(z))
#type conversions:convertung one type to another with int(),float(),complex():
x=1
y=2.4
z=1j
a=float(x)
b=complex(x)
c=int(y)
d=complex(y)
#d=int(z)
#e=float(z)
print(a)#1.0
print(b)#(1+0j)
print(c)#2
print(d)#(2.4+0j)
#print(e)#error
#we cannot convert complex number to a int or float