arr=[9,3,4,8,1]
n=len(arr)
l=0
k=3
temp=0
ans=0
for r in range(n):
    temp+=arr[r]
    if r-l==k:
        temp-=arr[l]
        l+=1
    if r-l+1==k:
        print(temp)
        ans=max(ans,temp)
print(ans)
arr=[9,3,4,8,1]
n=len(arr)
l=0
k=3
temp=[]
sum=0
ans=float("-inf")
sum=0
for r in range(n):
    temp.append(arr[r])
    sum+=arr[r]
    #print(sum)
    if r-l==k:
        sum-=temp[0]
        temp.pop(0)
        l+=1
    if r-l+1==k:
        print(temp)
        #sum+=arr[r]
        ans=max(sum,ans)
print(ans)
#variable size window:
arr=[9,3,4,8,1]
l=0
k=10
temp=0
ans=0
n=len(arr)   
for r in range(n):
    temp+=arr[r]
    while temp>k:
        temp-=arr[l]
        l+=1
    ans=max(ans,r-l+1)
print(ans)