'''Create a list of 5 numbers and print:
Maximum
Minimum
Sum'''
li=[4,6,8,2,1]
ans=0
print(max(li))
print(min(li))
print(sum(li))
maximum=li[0]
minimum=li[0]
for i in li:
    if i>maximum:
        maximum=i
    if i<minimum:
        minimum=i
print(maximum)
print(minimum)
for i in li:
    ans+=i
print(ans)
#Add and remove elements from a list.
li.append(0)#add element at last
print(li)
li.pop(2)#remove element by index.
print(li)
li.remove(6)#remove element 5
print(li)
#Reverse a list.
print(li[::-1])
#Sort a list in ascending and descending order.
li.sort()
print(li)
#descending order:
c=sorted(li,reverse=True)
print(c)
#Find duplicate elements in a list.
li=[5,6,3,2,1,6,5]
duplicate=[]
a=[]
for i in li:
    if i not in duplicate:
        duplicate.append(i)
    else:
        a.append(i)
print(a)