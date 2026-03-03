print("hello",end=' ')
print("susmitha")
print("how r u?")
print("hello",end='5')
print("susmitha",end='y')
print("how r u?")
li=["susmitha","sushma","suma"]
for i in range(len(li)):
    print(li[i],end=" ")
li=[["*","*","*"],["*","*","*"],["*","*","*"]]
#li=[[1,2,3,4],[5,6,7,8]]
r=len(li)
c=len(li[0])
for i in range(r):
    for j in range(c):
        print(li[i][j],end=" ")
    print()
r=3
c=3
for i in range(r):
    for j in range(c):
        print("*",end=" ")
    print()
r=3
c=10
for i in range(r):
    for j in range(c):
        print("*",end="")
        if j!=c-1:
   
            print(end="-")
    print()