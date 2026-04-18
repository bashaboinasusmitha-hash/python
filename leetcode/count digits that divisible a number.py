num=120
nums=str(num)
res=0
for i in nums:
    a=int(i)
    print(a)
    print(type(a))
    if a!=0 and num%a==0:
        res+=1
print(res)