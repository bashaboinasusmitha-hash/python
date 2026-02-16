#problems:
#printing even or odd using bitwise operators
n=int(input("Enter a number:"))
if n&1:
    print("the number is odd!")
else:
    print("The number is even!")
n=10
if n & 1==0:
    print("even")
#problem of swapping:
a=5
b=3
a=a^b
b=a^b
a=a^b
print(a,b)
#check powers of 2:
n=int(input("Enter a number:"))
if n & (n-1)==0:
    print("Powers of 2")
#mixed logical and bitwise operators:
#always solve bitwise first and then logical operators
print(5 & 3 or 0)
print(8>>1 and 3)
print(6^2 and 4)
print(4<<2|3)