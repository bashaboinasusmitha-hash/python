#Creating a numpy array indexing:
'''array indexing is the same as accessing an array element.we can access an element by referring to its index number.
The indexes in Numpy arrays start with 0,means the first element ha index 0 and second one has index 1 etc.'''
import numpy as np
arr=np.array([1,3,2,4])
print(arr[0])#1
print(arr[1])#3
print(arr[2]+arr[3])#6
#Accessing of 2-D arrays:
'''to accesss the elemenys from 2-D arrays we can use comma separated integers representing the dimension and index of element.
2-D arrays like table with rows and columns,where the dimension represents the row ans index represnts columnn.'''
arr=np.array([[1,2,3,2],[6,7,8,4]])
print(arr[0,1])#2 means at 1st row second element
print(arr[1,3])#4
#Access the 3-D arrays:
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[0,1,2])#6
'''explanation:here the first number represnts the first dimension,which contains two arrays:
[[1,2,3],[4,5,6]] and [[7,8,9],[10,11,12]] since we selected 0 [[1,2,3],[4,5,6]] and
second number represents second dimensions so [4,5,6] and third no. is 2 so number at index 2 is 6'''
#Negative Indexing :
'''use negative indexing to acces an array from the end'''
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr[1,-1])#8
#Numpy Array Slicing:
arr=np.array([1,2,3,4,5,6])
print(arr[1:5])#[2 3 4 5]
print(arr[4:])#[5 6]
print(arr[:4])#[1 2 3 4]
#Negative slicing:
print(arr[-3:-1])#from index 3 from last to index 1 from last [4 5]
#step
arr=np.array([1,2,3,4,5,6,7,8])
print(arr[1:6:2])#[2 4 6]
print(arr[::2])#[1 3 5 7]
#Slicing 2-D array:
arr=np.array([[1,2,3,4],[4,5,6,7]])
print(arr[1,1:4])#[5 6 7]
print(arr[0:2,2])#[3 6] from both elements return index of 2
print(arr[0:2,1:4])#[[2 3 4][5 6 7]]