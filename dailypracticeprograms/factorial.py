#finding fatorial of a number:
n=0
res=1
for i in range(1,n+1):
   res*=i
print(res)
#by functions:
def fact(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res
a=fact(5)
print(a)
#handling negative numbers:
def fact(n):
    if n<0:
        return "not defined"
    res=1
    for i in range(1,n+1):
        res=res*i
    return res
a=fact(4)
print(a)