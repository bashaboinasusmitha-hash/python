x=[]
y=[]
print(x is y)
a=[]
b=a
print(a is b)
x=None
if x is None:
    print("yes")
#same or different object
li=[1,3,6,8]
a=li
print(a is li)
if a is li:
    print("same object")
else:
    print("different object")
#using slicing
a=[1,2,3,4]
b=a[:]
print(a is b)
#modify the list
a=[[1,2],[3,4]]
b=a[:]
b[0][0]=10
b[1][0]=20
print(a)
print(b)
#== and is
li=[1,2,3]
li_1=[1,2,3]
print("values equal:",li==li_1)
print("same object:",li is li_1)