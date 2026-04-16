#NumPy array joining:
'''joining array means putting the contents of two or more arrays together.
In SQL we join based on the key,whereas in numpys we join arrays by axis.
we pass sequence of arrays that we want to join in a function"concatenate()". along with arrays we pass axis if axis not provided than by default it taken as 0'''
import numpy as np
arr_1=np.array([1,2,3])
arr_2=np.array([4,5,6])
arr=np.concatenate((arr_1,arr_2))
print(arr)#[1 2 3 4 5 6]
arr=np.concatenate((arr_1,arr_2),axis=0)
print(arr)#[1 2 3 4 5 6]
#joining 2-D arrays:
'''2-d arrays have axis=0,1'''
arr_1=np.array([[1,2,3],[4,5,6]])
arr_2=np.array([[7,8,9],[10,11,12]])
arr=np.concatenate((arr_1,arr_2),axis=0)
print(arr)
#output
'''[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]'''
arr=np.concatenate((arr_1,arr_2),axis=1)
print(arr)
#output
'''[[1 2 3 7 8 9]
[4 5 6 10 11 12]]
axis=0 means row wise and axis=1 means column wise'''
#joining 3-D array:
arr_1=np.array([[[1,2,3]]])
arr_2=np.array([[[4,5,6]]])
arr=np.concatenate((arr_1,arr_2))
print(arr)
#output:
'''[[[1 2 3]]

[[4 5 6]]]'''
arr=np.concatenate((arr_1,arr_2),axis=1)
print(arr)
#output:
'''[[[1 2 3]
[4 5 6]]]'''
arr=np.concatenate((arr_1,arr_2),axis=2)
print(arr)#[[[1 2 3 4 5 6]]]