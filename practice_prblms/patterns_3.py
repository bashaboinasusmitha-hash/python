r=4
c=15
for i in range(r):
    for j in range(c):
        if i==0 or i==r-1 or j==0 or j==c-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
r=6
c=5
c1=r-1
for i in range(r):
    for j in range(c1-i):
        print(" ",end="")
    for k in range(c):
        print("*",end="")
    print()
r=5
c=5
c1=r-1
for i in range(r):
    for j in range(c1-i):
        print("*",end="")
    print()
r=5
c=5
c1=r-1
for i in range(r):
    for j in range(i):
        print(" ",end="")
    for k in range(c):
        print("*",end='')
    print()
n=4
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()       
r=5
n=r-1
for i in range(r):
    for j in range(n-i):
        print(" ",end="")
    temp=i*2+1
    for k in range(temp):
        print("*",end="")
    print()