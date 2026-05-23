#Remove all even numbers from a list.
li=[1,2,4,5,7,4,3,9]
n=len(li)
li_new=[]
for i in li:
    if i%2!=0:
        li_new.append(i)
print(li_new)
#Find second largest number in a list.
li=[3,4,3,1,2,6,7]
max=float('-inf')
second=float("-inf")
for i in li:
    if i>max:
        second=max
        max=i
    elif i!=max and i>second:
        second=i
print(second)
#Tuple Programs
#Create a tuple and print its elements.
tup=(2,4,"susmitha",7.9,True)
print(tup)
#Count occurrences of an element in tuple.
tup=(2,4,6,0,2,3,5,6,2)
dic={}
for i in tup:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
#Find index of an element in tuple.
tup=(2,4,6,0,2,3,5,6,2)
print(tup.index(2))#prints only first occured number index.
for i in range(len(tup)):
    print(tup[i],i)
#Convert tuple into list.
tup=(2,4,6,0,2,3,5,6,2)
print(list(tup))
#Create nested tuples and access inner elements.
tup=(2,4,5,2,(6,7,9),(2,3,5,1),0,8)
print(tup[4])
print(tup[4][1])
print(tup[4][2])
#set programs:
'''Create two sets and perform:
Union
Intersection
Difference'''
s1={1,3,2,7,8,3,9}
s2={3,6,1,0,5,6,2,8}
print(s1.union(s2))
print(s1|s2)
print(s1.intersection(s2))
print(s1-s2)
#Remove duplicate elements from a list using set.
s1=[4,5,7,9,4,6,4,5,8,9]
s2=set(s1)
print(s2)
#Check whether an element exists in a set.
s1={1,3,2,7,8,3,9}
if 10 in s1:
    print("True")
else:
    print("False")
#Add and remove elements from set.
s1={1,3,2,7,8,3,9}
s1.add(10)
print(s1)
s1.discard(8)
print(s1)