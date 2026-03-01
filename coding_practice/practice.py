colors=[1,1,1,6,1,1,1]
n=len(colors)
dist=0
for i in range(n):
    for j in range(n):
        if colors[i]!=colors[j]:
            diff=abs(i-j)
            dist=max(diff,dist)
print(dist)
arr=[17,18,5,4,6,1]
n=len(arr)
array=[]
for i in range(n-1):
    temp=0
    for j in range(i+1,n):
        temp=max(temp,arr[j])
    array.append(temp)
array.append(-1)
print(array)

arr=[17,18,5,4,6,1]
n=len(arr)
rmax=-1
for i in range(n-1,-1,-1):
    temp=arr[i]
    arr[i]=rmax
    rmax=max(rmax,temp)
print(arr)       
#float("inf") is used to print max value among all existing numbers
#float("-inf") i susd to print least value among all existing numbers          
name = input("Enter your name: ")
place = input("Enter your place: ")
print("my name is", name)
print("i'm living in", place)
n = "hello"
m = str(5)
print(type(n))
print(n + m)
# n = int("hello")
# print(n + 5)
li = []
n = 5
for i in range(n):
    temp = int(input(f"Enter number {i+1}: "))
    li.append(temp)
print(li)
new = []
s = input("Enter numbers separated by space: ")
temp = s.split(" ")
for i in range(len(temp)):
    val = int(temp[i])
    new.append(val)
print(new)
li = list(map(int, input("Enter another list of numbers separated by space: ").split()))
print(li)
s = input("Enter a line of words separated by space: ").split()
print(s)
s = input("Enter a string: ")
a = input("Enter first list separated by space: ").split()
b = input("Enter second list separated by space: ").split()
c = input("Enter another string: ")
print(s)
print(a)
print(b)
print(c)