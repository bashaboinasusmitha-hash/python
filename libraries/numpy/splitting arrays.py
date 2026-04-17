#NumPy array splitting:
'''splitting arrays is opposite to joining an arrays.joins combine multiple arrays whereas, splitting of arrays we separate the one array into multiple arrays.
here we use array_split() in this we pass the array which we need to separate and also the no.of splits we want.'''
import numpy as np
arr=np.array([1,2,3,4,5,6])
new_arr=np.array_split(arr,3)
print(new_arr)
#output:
'''[array([1,2]),array([3,4]),array([5,6])]
if array not has required no. of elements the array_split() adjust accordingly from end of an array.'''
arr=np.array([1,2,3,4,5])
new_arr=np.array_split(arr,3)
print(new_arr)
arr=np.array([1,2,3,4,5])
new_arr=np.array_split(arr,2)
print(new_arr)#[array([1, 2, 3]), array([4, 5])]
#output:
'''[array([1,2]),array([3,4]),array([5])]
NOTE: we have "split()" but it not adijust the array size when the required no.of elements are less
arr=np.array([1,2,3,4,5])
new_arr=np.split(arr,3)
print(new_arr) this gives an error.'''
#Split into arrays:
'''we can acces the elements inside of different arrays.'''
arr=np.array([1,2,3,4,5,6])
new_arr=np.array_split(arr,3)
print(new_arr)
print(new_arr[0])#[1 2]
print(new_arr[1])#[3 4]
print(new_arr[2])#[5 6]
#Splitting 2-D arrays:
arr=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
new_arr=np.array_split(arr,3)
print(new_arr)
#output
'''
[array([[1,2],
       [3,4]]), array([[5,6],
       [7,8]]), array([9,10],
       [11,12]])]'''
arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
new_arr=np.array_split(arr,3)
print(new_arr)
#output:
'''
[array([[1,2,3],
       [4,5,6]]), array([[7,8,9],
       [10,11,12]]), array([[13,14,15]])]'''