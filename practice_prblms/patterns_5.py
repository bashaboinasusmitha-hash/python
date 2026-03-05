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
for i in range(r-1,-1,-1):
    for j in range(c1-i):
        print(" ",end="")
    temp=i*2+1
    for j in range(temp):
        if j==0 or j==i*2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(6):
    for j in range(i+1):
        if j==0:
            print("1",end="")
        elif j==1:
            print("2",end="")
        elif j==2:
            print("3",end="")
        elif j==3:
            print("4",end="")
        elif j==4:
            print("5",end="")
        elif j==5:
            print("6",end="")
    print()
n=6
for i in range(n):
    for j in range(1,i+1):
        print(j,end="")
    print()
n=6
for i in range(n):
    for j in range(n-1-i):
        print(" ",end="")
    for k in range(i+1,0,-1):
        print(k,end="")
    print()
n=6
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1,0,-1):
        print(k,end="")
    for m in range(2,i+2):
        print(m,end="")
    print()