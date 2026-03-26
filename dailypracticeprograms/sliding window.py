#subarray:
nums=[1,8,9]
n=len(nums)
ans=[]
for i in range(n):
    for j in range(i,n):
        temp=[]
        #print(nums[i],nums[j])
        for k in range(i,j+1):
           temp.append(nums[k])
        print(temp)
        ans.append(temp)
print(ans)
for i in ans:
    print(i)
print(ans[0])
#Substring:
s="susmitha"
n=len(s)
#print(n)
ans=[]
for i in range(n):
    #print(s[i])
    for j in range(i,n):
        temp=""
        for k in range(i,j+1):
            temp+=s[k]
        ans.append(temp)
print(ans)
#subsequence:
'''all sub arrays are sub sequences,but not sub sequences are subarrays
ex:[1,4,2] subarrays:[1],[1,4],[1,4,2],[4],[4,2],[2],subsequences:[1,2],[1,4],[2],[4,2]
Note:All subsequences must be in order like [1,4] ,[1,2],[4,2] but not [4,1],[2,1]'''