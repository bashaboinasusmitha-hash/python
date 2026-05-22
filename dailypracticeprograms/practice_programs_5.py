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