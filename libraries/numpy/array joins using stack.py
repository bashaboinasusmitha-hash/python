#Joining arrays by stack functions:
'''stack is similar to concatenation but only difference is that stack joins arrays by new axis.
stacking means putting one element over other elemnt.'''
import numpy as np
arr_1=np.array([1,2,3])
arr_2=np.array([4,5,6])
arr=np.stack((arr_1,arr_2))
print(arr)
#output:
'''[[1 2 3 ]
[4 5 6]]'''
arr=np.stack((arr_1,arr_2),axis=1)
print(arr)
#output:
'''[[[1 4]
[2 5]
[3 6]]
we can concatenate two 1-D arrays by using axis=1'''
#Stacking along with Rows:
'''NumPy provides hstack() helper function which is used to stack the arrays along rows.means adding elements in a single horizontally.'''
arr_1=np.array([1,2,3])
arr_2=np.array([7,8,9])
arr=np.hstack((arr_1,arr_2))
print(arr)#[1 2 3 7 8 9]
#2-D array
arr_1=np.array([[1,2,3],[4,5,6]])
arr_2=np.array([[7,8,9],[10,11,21]])
arr=np.hstack((arr_1,arr_2))
print(arr)
#output:
'''[[1 2 3 7 8 9]
[4 5 6 10 11 21]]'''
#Stcking along columns:
'''numpy has heper function vstack() id used to joinn arrays along columns.'''
arr_1=np.array([1,2,3])
arr_2=np.array([7,8,9])
arr=np.vstack((arr_1,arr_2))
print(arr)
#output:
'''[[1 2 3]
[7 8 9]]'''
arr_1=np.array([[1,2,3],[4,5,6]])
arr_2=np.array([[7,8,9],[10,11,21]])
arr=np.vstack((arr_1,arr_2))
print(arr)
#output:
'''[[1 2 3]
[4 5 6]
[7 8 9]
[10 11 21]]'''
#Stacking along depth or height:
'''numpy has helper function dstack() which used to join arrays but depth or along height.'''
arr_1=np.array([[1,2,3],[4,5,6]])
arr_2=np.array([[7,8,9],[10,11,21]])
arr=np.dstack((arr_1,arr_2))
print(arr)
#output:
'''[[[1 7]
[2 8]
[3 9]]
[[4 10]
[5 11]
[6 21]]]'''
arr_1=np.array([1,2,3])
arr_2=np.array([7,8,9])
arr=np.dstack((arr_1,arr_2))
print(arr)
#output:
'''[[[1 7]
[2 8]
[3 9]]]'''