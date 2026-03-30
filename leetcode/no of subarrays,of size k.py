arr=[11,13,17,23,29,31,7,5,2,3]
n=len(arr)
k=3
ans=0
threshold=5
for i in range(n):
    for j in range(i,n):
        temp=[]
        for m in range(i,j+1):
            temp.append(arr[m])
        s=0
        if len(temp)==k:
            print(temp)
            for num in temp:
                s+=num
            avg=s/len(temp)
            print(avg)
            if round(avg)>=threshold:
                ans+=1
print(ans)
#sliding window:
arr=[2,2,2,2,5,5,5,8]
k=3
threshold=4
n=len(arr)
l=0
ans=0
temp=0
for r in range(n):
    temp+=arr[r]
    if r-l==k:
        temp-=arr[l]
        l+=1
    if r-l+1==k:
        if temp/k>=threshold:
            ans+=1
print(ans)
arr=[11,13,17,23,29,31,7,5,2,3]
#arr.sort()
n=len(arr)
k=3
ans=0
threshold=5
for i in range(n):
    for j in range(i,n):
        temp=[]
        tsum=0
        for m in range(i,j+1):
            temp.append(arr[m])
            tsum+=arr[m]
        s=0
        if len(temp)==k:
           avg=tsum/k
           if avg>=threshold:
               ans+=1
print(ans)