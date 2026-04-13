#Shape of an numpy arrays:
'''the shape of an array represents the no. of elememts in each dimensions.
Numpy has attribute shape that returns the tuple with each index having no. of corresponding elements.'''
import numpy as np
arr=np.array([1,2,3,4])
print(arr.shape)#(4,)
#2-D:
arr=np.array([[1,2,3,4]])
print(arr.shape)#(1,4) which represnts no. of rows and no. of columns 
arr=np.array([[1,2,3],[4,5,6]])
print(arr.shape)#(2,3) where the aray has two dimensions where 1st represents no.of rows and 2nd represnts columns
arr=np.array([1,2,3,4],ndmin=5)
print(arr)#[[[[[1,2,3,4]]]]]
print(arr.shape)#(1,1,1,1,4) 
arr=np.array([[1,2],[2,3],[4,5]])
print(arr.shape)#(3,2)
arr=np.array([[1,2,3],[1,5,4]])
print(arr.shape)#(2,3)
print(arr.shape[0])#2
print(arr.shape[1])#3
arr=np.array([1,5,3],ndmin=3)
print(arr.shape)#(1,1,3)