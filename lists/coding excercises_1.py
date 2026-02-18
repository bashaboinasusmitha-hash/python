li=[1,2,3,4,0,3]
li.append(2)
li.insert(2,0)
li.sort()
li.pop(0)
print(li)
#without using min() sort() removing smallest elemnt
li=[1,2,3,4,0,3]
n=len(li)
smallest=li[0]
for i in li:
    if i<smallest:
        smallest=i
print(smallest)
#count even numbers
li=[1,2,3,4,9,6,3]
n=len(li)
count=0
for i in range(n):
    if li[i]%2==0:
        count+=1
print(count)
#reversing the list
a=[10,13,19,20,37]
n=len(a)
li=[]
for i in range(n-1,-1,-1):
    li.append(a[i])
print(li)
#reversing alist without taking another variable to store
a=[10,13,19,20,37]
n=len(a)
for i in range(n//2):
    a[i],a[n-1-i]=a[n-1-i],a[i]
print(a)
#removing a duplicates
a=[1,2,2,3,4,4,1,5,7]
set=set(a)
print(set)
#without set()
a=[1,2,2,3,4,4,1,5,7]
li=[]
n=len(a)
for i in range(n):
    if a[i] not in li:
        li.append(a[i])
print(li)
#printing second largest number 
a=[10,30,2,50,28]
n=len(a)
largest=float("-inf")
smallest=float("-inf")
for num in a:
    if num>largest:
        smallest=largest
        largest=num
    elif num>smallest and num!=largest:
        smallest=num
print(smallest)
#sum of all elements:
a=[[1,2],[3,4],[5,6]]
r=len(a)
b=0
for i in range(r):
    b+=a[i][0]+a[i][1]
print(b)
#creating separate lists for even and odd in list
a=[1,2,5,4,7,8]
n=len(a)
li=[]
li_1=[]
li_2=[]
for i in range(n):
    if a[i]%2==0:
        li_1.append(a[i])
    else:
        li_2.append(a[i])
li.append(li_1)
li.append(li_2)
print(li)