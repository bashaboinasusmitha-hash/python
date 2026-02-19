#counting no.of even numbers in a tuplee
t=(1,2,3,4,5,6,7,9,0)
n=len(t)
count=0
for i in range(n):
    if t[i]%2==0:
        count+=1
print(count)
#sum of all elements in a tuple
t=(1,2,3,4,5,6,7,9,0)
n=len(t)
sum=0
for i in range(n):
    sum=sum+t[i]
print(sum)
#finding second largest element without max()
t=(1,2,3,4,5,6,7,9,0)
largest=float("-inf")
second=float("-inf")
n=len(t)
for i in range(n):
    if t[i]>largest:
        second=largest
        largest=t[i]
    elif (second<t[i] and t[i]!=largest):
        second=t[i]
print(second)
#swapping of two tuples:
a=(1,2,3)
b=(4,5,6)
print(a)
print(b)
a,b=b,a
print(a)
print(b)
#reversing a tuple:
t=(1,2,3,4)
n=len(t)
rev=()
for i in range(n-1,-1,-1):
    print(t[i])
    rev+=(t[i],)
print(rev)
#removing duplicates
t=(1,2,2,3,4,0,1,1)
ans=[]
for i in range(n):
    if i not in ans:
        ans.append(t[i])
print(tuple(ans))
#find frequency of each elements
t=(1,2,2,3,4,0,1,1)
n=len(t)
dic={}
for i in range(n):
    if t[i] in dic:
        dic[t[i]]+=1
    else:
        dic[t[i]]=1
print(dic)
#merge two tuples and sort them
t1=(9,1,2,8)
t2=(1,5,3,0)
t3=(t1+t2)
li=list(t3)
li.sort()
#print(li)
print(tuple(li))
