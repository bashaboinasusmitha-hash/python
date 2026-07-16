nums=[4,3,2,7,8,2,3,1]
n=len(nums)
dic={}
li=[]
for i in range(n):
    if nums[i] not in dic:
        dic[nums[i]]=1
    else:
        dic[nums[i]]+=1
print(dic)
for val in dic:
    if dic[val]!=1:
        li.append(val)
print(li)