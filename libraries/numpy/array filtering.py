#Array filtering:
'''array filtering means getting some elements from existing array and creating  a new array out of them.
for filtering an array in NumPy we use boolean index list.If the value at index is True means that element contain in filtered array
if the value is False then the value is not in the filtered array.'''
import numpy as np
arr=np.array([2,7,4,3,1])
x=[True,False,True,False,False]
new_arr=arr[x]
print(new_arr)#[2 4] because the new array consists only the values where filter array had the values True.
print(arr)#[2 7 4 3 1]
new_arr=x
print(new_arr)#[True, False, True, False, False]
#CREATING THE FILTER ARRAY:
'''in above example we have given the values of True or False,but now we create a new array based on the conditions.'''
arr=np.array([49,32,35,46,45,39])
filter_arr=[]
for i in arr:
    if i>40:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
new_arr=arr[filter_arr]
print(filter_arr)#[True False False True True False]
print(new_arr)#[49 46 45]
#creating filter array for even numbers:
arr=np.array([4,2,3,7,4,9,6])
filter_arr=[]
for i in arr:
    if i%2==0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
new_arr=arr[filter_arr]
print(new_arr)#[4 2 4 6]
print(filter_arr)#[True, True, False, False, True, False, True]