r=4
c=3
c1=r-1
for i in range(r):
    for j in range(i):
        print("*",end="")
    print()

a=int(input("enter the no.of rows:"))
b=int(input("enter the no. of columns:"))
b1=a-1
for i in range(a):
    for j in range(i+1):
        print('*',end="")
    print()

r=7
c=10
c1=r-1
for i in range(r):
    for j in range(i):
        print(" ",end="")
    temp=(2*r-3-(2*i))
    for k in range(temp):
        print("*",end="")
    print()

r=7
c=10
c1=r-1
for i in range(r):
    for j in range(c1-i):
        print(" ",end="")
    temp=2*i+1
    for k in range(temp):
        print("*",end="")
    print()
r=7
c=10
c1=r-1
for i in range(r):  #for i in range(r-1)
    for j in range(c1-i):
        print(" ",end="")
    temp=2*i+1
    for k in range(temp):
        print("*",end="")
    print()
for i in range(r-2,-1,-1):   #for i in range(r-1,-1,-1):
    for j in range(c1-i):
        print(" ",end="")
    temp=2*i+1
    for k in range(temp):
        print("*",end="")
    
    print()
r=7
c=10
c1=r-1
for i in range(r-2,-1,-1):   #for i in range(r-1,0,-1):
    for j in range(c1-i):
        print(" ",end="")
    temp=2*i+1
    for k in range(temp):
        print("*",end="")
    
    print()
for i in range(r):  #for i in range(1,r)
    for j in range(c1-i):
        print(" ",end="")
    temp=2*i+1
    for k in range(temp):
        print("*",end="")
    print()
r=5
c=7
c1=r-1
for i in range(r):
    for j in range(c1-i):
        print(" ",end="")
    temp=i*2+1
    for j in range(temp):
        if j==0 or j==i*2 or i==r-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
r=5
c=7
c1=r-1
for i in range(r-1,-1,-1):
    for j in range(c1-i):
        print(" ",end="")
    temp=i*2+1
    for j in range(temp):
        if i==c1 or j==i*2 or j==0:
            print("*",end="")
        else:
            print(" ",end="")
    print()
r=5
c=7
c1=r-1
for i in range(r-1):
    for j in range(c1-i):
        print(" ",end="")
    for j in range(i*2+1):
        if j==0 or j==i*2 or i==r-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()