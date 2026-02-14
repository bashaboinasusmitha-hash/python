#swapping using temp variable
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
temp=a
a=b
b=temp
print(a)
print(b)
#without third variable
a,b=40,52
a,b=b,a
print(a,b)