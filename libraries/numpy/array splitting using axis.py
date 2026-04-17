#NumPy arrays splitting by using axis:
import numpy as np
arr=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
new_arr=np.array_split(arr,3,axis=1)
print(new_arr)
#output:
'''[array([[1],
[4],
[7]
[10],
[13],
[16]]),array([[2],
[5]
[8],
[11],
[14],
[17]]),array([[3],
[ 6],
[ 9],
[12],
[15],
[18]])]])]'''
'''An alternate solution is using hsplit() opposite of hstack().
Use the hsplit() method to split the 2-D array into three 2-D arrays along columns.'''
arr=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
new_arr=np.hsplit(arr,3)
print(new_arr)
#output:
'''[array([[ 1],
       [ 4],
       [ 7],
       [10],
       [13],
       [16]]), array([[ 2],
       [ 5],
       [ 8],
       [11],
       [14],
       [17]]), array([[ 3],
       [ 6],
       [ 9],
       [12],
       [15],
       [18]])]
[array([[ 1],
       [ 4],
       [ 7],
       [10],
       [13],
       [16]]), array([[ 2],
       [ 5],
       [ 8],
       [11],
       [14],
       [17]]), array([[ 3],
       [ 6],
       [ 9],
       [12],
       [15],
       [18]])]'''
'''similarily an alternate of  vstack() is vsplit().
use the vsplit()  method to split the 2-D arrays into split arrays along rows.'''
arr=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
new_arr=np.vsplit(arr,3)
print(new_arr)
#output:
'''[array([[1, 2, 3],
       [4, 5, 6]]), array([[ 7,  8,  9],
       [10, 11, 12]]), array([[13, 14, 15],
       [16, 17, 18]])]'''
#dsplit() opposite to d stack()
'''dsplit() is used on;y for 3 more than 3 dimension arrays.
arr=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
new_arr=np.dsplit(arr,3)
print(new_arr) this gives an error'''
#ouput:
'''ValueError: dsplit works only on arrays of 3 or more dimensions'''
arr=np.array([[[1,2,3],[4,5,6],[4,7,8],[8,9,0]]])
new_arr=np.dsplit(arr,3)
print(arr)
#output:
'''[[[1 2 3]
    [4 5 6]
    [4 7 8]
    [8 9 0]]]'''