#Array reshaping:
'''array reshaping means changing the shape of an array.
By reshaping we can add or remove the dimensions and the change no.of elements in dimension.'''
#Reshpaing 1-D to 2-D
import numpy as np
arr=np.array([1,2,3,4,5,6])
new_arr=arr.reshape(2,3)
print(new_arr)#[[1 2 3][4 5 6]] #the new must contains 2 rows and in each row 3 elements.
#Reshape 1-D to 3-D:
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_arr=arr.reshape(2,3,2)
print(new_arr)#[[[1 2] [3 4] [5 6]] [7 8] [9 10] [11 12]]
'''meaning there two arrays and that two arrays contains 3 arrays inside of 2 elements in each.'''
#Can we reshape into any shape?
'''yes, as long as the elements required for reshaping are equal in both shapes.
We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements.
Example:
arr=np.array([1,2,3,4,5,6,7,7])
new_arr=arr.reshape(3,3) 
print(new_arr)#gives an error because 3*3=9 but here we have only 8 elements'''
#returns copy or view:
'''check if the returned array is copy or view.'''
arr=np.array([1,2,3,4,5,6])
new_arr=arr.reshape(2,3)
print(new_arr.base)#[1 2 3 4 5 6] so it a view
#Unknown dimension:
'''we allowed to have a single unknown dimension.Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
pass(-1) and then numpy calculate this value for us.'''
arr=np.array([1,2,3,4,5,6,7,8])
new_arr=arr.reshape(2,2,-1)
print(new_arr)
#we cannot pass (-1) more than one time
#flattening arrrays:
'''flattening arrays means converting multidimensional array to 1-D.so for this we can use reshape(-1)'''
arr=np.array([[1,2,3],[3,4,5]])
new_arr=arr.reshape(-1)
print(new_arr)#[1 2 3 3 4 5]