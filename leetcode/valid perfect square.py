#valid perfect squares:
num=14
for i in range(1,num+1):
    a=i*i
    if a==num:
        print(True)
        break
else:
    print(False)   
#Optimization: 
num=16
i=int(num**0.5)
print(i*i==num)