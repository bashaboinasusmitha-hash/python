#return max length of subarray which consists atmost k odds
arr=[1,3,4,5,7]
k=2
n=len(arr)
l=0
ans=0
temp=[]
for r in range(n):
    if arr[r]%2==1:
        temp.append(arr[r])    
    while len(temp)>k:
        if arr[l]%2==1:
            temp.pop(0)
        l+=1
    print(arr[l:r+1])
    ans=max(ans,r-l+1)
print(ans)
nums=[1,3,2,6,9,3,9,2,7]
k=3
n=len(nums)
l=0
ans=0
temp=0
for r in range(n):
    if nums[r]%2!=0:
        temp+=1
    while temp>k:
        if nums[l]%2!=0:
            temp-=1
        l+=1
    print(nums[l:r+1])
    ans=max(ans,r-l+1)
print(ans)
#return number of subarrays with atmost k odds:
arr=[1,3,2,6,9,3,9,2,7]
k=3
n=len(arr)
ans=0
temp=0
l=0
for r in range(n):
    if arr[r]%2==1:
        temp+=1
    while temp>k:
        if arr[l]%2==1:
            temp-=1
        l+=1
    print(arr[l:r+1],r-l+1)
    ans+=r-l+1
print(ans)