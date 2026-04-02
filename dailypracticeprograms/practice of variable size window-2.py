'''You are given an array and You should
Find the maximum length of the
subarray which has atmost k ODD
numbers'''
arr=[12,1,3,1,1,6,7,1,8,1]
n=len(arr)
k=2
l=0
ans=0
temp=0
for r in range(n):
    if (arr[r]%2 == 1):
        temp+=1
    while temp>k:
        if (arr[l]%2 == 1):
            temp-=1
        l+=1
    ans=max(ans,r-l+1)
print(ans)
#Time complexity:O(n)