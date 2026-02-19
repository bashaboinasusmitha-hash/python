print("tuples is a collection of elements in python that are:ordered,immutable,allow duplications,can store different datatypes")
#tuples are written in parantheses()
t=(1,2,"susmitha",20.5,True)
print(t)
print("why tuples:")
print("used when data should not be changed")
print("tuple are faster than lists")
print("used as dictionary keys because immutable")
#operations
#creating a tuple
t=(2,4,"susmitha",False,50.7)
print(t)
#single element tuple
t=(2,)#comma is mandatory
print(t)
#accessing elements (indexing)
t=(1,3,5,"suma",90,3,2)
print(t[3])
print(t[4])
#slicing 
print(t[0:4:2])
print(t[1:3:1])
#length
n=len(t)
print(t)
#concatenation
t1=(1,2,3)
t2=(4,5,6)
t3=(5,2,1)
print(t1+t2)
a=t1+t2
#t3=a
print(t3)
print(t3+t2+t1)
print(t2+t1+t3)
t3+=t2+t1
print(t3)
#type
t=(1,2,3,9.0)
print(type(t))
t=(2)
print(type(t))
t=(1,)
print(type(t))
#repeatition
t=(1,2,3)
print(t*2)#(1,2,3,1,2,3)
t=(10)
print(t*5)
t=(10,)
print(t*5)
#membership operator
print(2 in t)
print(2 not in t)
print(3 in t)
#accessing last elements
t=(20,13,"ajay",True)
print(t[-2])
#min() and max()
t=(1,2,7,7,2,9)
print(min(t))
print(max(t))
print(min(t),max(t))
#t=(1,2,7,9,"susmitha")
#print(min(t))#error because mixed tuple
#count()
print(t.count(7))
print(t.count(9))
#conversion of list to tuple
li=[1,3,5,9]
print(tuple(li))
#nested tuples
t1=(1,2,3)
t2=(0,4,3)
t3=(t1,t2)
print(t3)
print(t3[0])
print(t3[1])
print(t3[0][0])
print(t3[1][0])
print(t3[0][1])