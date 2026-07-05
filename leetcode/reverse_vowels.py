s= "IceCreAm"
s_1=[]
vowels="aeiouAEIOU"
for i in s:
    if i in vowels:
        s_1.append(i)
s_1=s_1[::-1]
res=""
j=0
for i in s:
    if i in s_1:
        res+=s_1[j]
        j+=1
    else:
        res+=i
print(res)