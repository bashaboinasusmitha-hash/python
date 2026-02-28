#bubble sort
li=[2,6,1,5,0]
n=len(li)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
    print(li)
print(li)
li=[2,6,1,5,0]
n=len(li)
for i in range(0,n-1):
    didswapped=False
    for j in range(0,n-i-1):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
            didswapped=True
    print(li)
    if didswapped==False:
        break 
print(li)
li=[1,0,4,6,3]
li.sort()
print(li)
li=[0,4,8,1,7]
print(sorted(li))
print(li)
li=[2,6,1,5,0]
n=len(li)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if li[j]<li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
print(li)
li=[2,6,1,5,0]
li.reverse()
print(li)
li=[2,6,1,5,0]
li.sort(reverse=True)
print(li)
