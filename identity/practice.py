print("identity opertors are 'is' and 'is not'")
print("working of identity operators: they check whether two variables refers to same object in memory")
#'==' and 'is' totally different in working
print("== is value equality and is for memory identity")
a=[1,2,3]#obj-1
b=[1,2,3]#obj-2
print(a==b)#true because same values
print(a is b)#false (different objects)
a=[1,2]
b=a
print(a is b)#true because both point to same memory
#small integer caching
print("python caches small integers(-5 to 256)")
x=100
y=100
print(x is y)#true
x=1000
y=1000
print(x is y)#false
'''this is because small integers are pre stored in memory and sometimes it returns true depending on environment'''
if x is None:
    print("no value")
#object identiy
a=20
b=20
c=int("1000")
d=int("1000")
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(a is b)
print(c is d)
a=[1,2,3]
b=a[:]
print(a is b)
print(a==b)
b=a.copy()
a=[[1,3],[2,4]]
b=a[:]
b[0][0]=100
print(a)