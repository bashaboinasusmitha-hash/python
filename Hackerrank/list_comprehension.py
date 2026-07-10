x=int(input())
y=int(input())
z=int(input())
n=int(input())
li=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            li_1=[]
            li_1.extend([i,j,k])
            li.append(li_1)
li_final=[]
for i in range(len(li)):
    res=0
    #print(li[i])
    for j in li[i]:
        res+=j
    if res!=n:
        li_final.append(li[i])
print(li_final)

#method 2
x=int(input())
y=int(input())
z=int(input())
n=int(input())
list_final=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k!=n:
                list_final.append([i,j,k])
print(list_final)