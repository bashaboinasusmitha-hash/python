print("what is a list? ")
print("list is a container that stores multiple values,different data types, they are ordered and we can modify it later")
#allow different data types
a=["susmitha",10,True,10.3]
print(a)
#allows duplicates
a=[10,1,2,10,1,4,2]
print(a)
#mutable:
a=[10,20,3,15,36]
a[0]=25
print(a)
#nested list
li=[[10,48,3],[1,2,3,4]]
print(li)
print(li[0])
print(li[0][1])
print(len(li))
li[0]=[10,20]
print(li)
#accessing of elements
a=[10,20,41,10]
print(a[2])
print(a[1])
#operations
#slicing:
a=[1,3,6,0,1,2]
print(a[0:3])
print(a[1:4:1])
print(a[:5:1])
#append:it is used to add elements at last
li=[1,3,5,2,7]
li.append(2)# here 2 is element add at last of list
#insert: insert element at specific index:
li=[1,3,5,2,6,1]
li.insert(1,10)#it means at index 1 the element 10 will insert
print(li)
#remove:it removes the values
li=[20,4,16,30]
li.remove(20)#it removes element 20
print(li)
#pop: by default delete last element and remove elment by index if given
li=[20,10,25,32,12,13,]
li.pop()
li.pop(3)
print(li)
#sort:
a=[12,13,8,3,28,1]
a.sort()
print(a)
#reverse: reverse the list
a=[2,4,1,7,3,0]
a.reverse()
print(a)
#extend: add multiple values at a time:
b=[1,2,3,5,3,1,7]
b.extend([2,4,1,5])
print(b)
#count : it counts number of times a value occured in a list
a=[2,6,2,4,1,2,8,9]
print(a.count(2))
#min(): it used to get minimum value of list
print(min(a))
#max
print(max(a))
print("note: mixed list cannot sorted!")
#accessing elements from last
a=[1,3,7,0,2,4]
print(a[-1])#4
print(a[-2])#2
print(a[-3])#0