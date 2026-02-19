#traversing a loop with tuples
t=("suma",True,3,4,4.0)
for i in t:
    print(i)
t=("suma",True,3,4,4.0)
n=len(t)
for i in range(n):
    print(t[i])
#using conditional statements 
t=("suma",True,3,4,4.0)
if 3 in t:
    print("number exists")
else:
    print("not exist")
if "susmitha" in t:
    print("true")
else:
    print("false")
#finding largest number without max()
t=(1,2,3,9,4,3)
n=len(t)
largest=t[0]
for i in range(n):
    if t[i]>largest:
        largest=t[i]
print(largest)
#finding minimum without min()
t=(1,2,3,9,4,3)
n=len(t)
smallest=t[0]
for i in range(n):
    if t[i]<smallest:
        smallest=t[0]
print(smallest)
#printing odd and even numbers
t=(1,4,2,8,3,7,0)
n=len(t)
t1=[]
t2=[]
for i in range(n):
    if t[i]%2==0:
        t1.append(t[i])
    else:
        t2.append(t[i])
print(tuple(t1))
print(tuple(t2))