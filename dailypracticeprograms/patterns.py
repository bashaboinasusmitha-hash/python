r=5
c=5
for i in range(r):
    for j in range(c):
        print("*",end=" ")
    print()
#
r=4
c=4
for i in range(r):
    for j in range(c):
        print("*",end="")
        if j!=c-1:
            print(end="_")
    print()
#right angled traingle
r=5
c=5
c1=r-1
for i in range(r):
    for j in range(i+1):
        print("*",end=" ")
    print()
#inverted rightt angle triangle:
print("inverted:")
r=6
c=5
c1=r-1
for i in range(r):
    for j in range(c1-i):
        print("*",end=" ")
    print()
r=5
c=5
c1=r-1
for i in range(r):
    for j in range(1,i+1):
        print(j,end=" ")
    print()