#difference between the copy and view:
'''copy is the new array and the view is just view of the original array.
copy owns the data if any changes made to copy doesn't change the original array and any changes made in original arry doen't affect copy array.
but the view doesn't own the data if any changes made to view array it affects the original array and vice versa.'''
import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.copy()
arr[0]=42
print(arr)#[42 2 3 4 5]
print(x)#[1 2 3 4 5] here there is no changes as chages made in arr
x[1]=40
print(x)#[1 40 3 4 5]
print(arr)#[42 2 3 4 5]
y=arr.view()
arr[0]=20
print(arr)#[20  2  3  4  5]
print(y)#[20  2  3  4  5] here changes made to both view and original array
#Make chages to view:
arr=np.array([1,5,3,6,8])
x=arr.view()
x[0]=31
print(x)#[31  5  3  6  8]
print(arr)#[31  5  3  6  8]
#Check if array owns the data:
'''as mentioned above copies owns the data,views doesn't own so we have attributes "base" if it returns None if array owns the data. '''
arr=np.array([1,3,5,7,8])
x=arr.copy()
y=arr.view()
print(x.base)#None
print(y.base)#[1 3 5 7 8]
arr[1]=2
x[2]=4
print(x)#[1 3 4 7 8]
print(arr)#[1 2 5 7 8]
print(y)#[1 2 5 7 8]
print(x.base)#None
print(y.base)#[1 2 5 7 8]