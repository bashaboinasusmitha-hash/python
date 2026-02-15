#printing cube of one number
x=7
x**=3
print(x)
#printing remainder using assigning operator
y=29
y%=6
print("the remainder is", y)
#floor divison
z=45
z//=4
print(z)
#loop based programs
res=0
for i in range(1,21):
    res+=i
print(res)
#printing product using loops
ans=1
for i in range(1,6):
    ans*=i
print(ans)
#subtracting
num=int(input("Enter a number:"))
res=0
for i in range(num,-1,-2):
    print(i)