#Creating filter array directly from array:
'''We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to.'''
import numpy as np
arr=np.array([1,4,2,5,8,0])
filter_arr=arr>2
arr_new=arr[filter_arr]
print(filter_arr)#[False  True False  True  True False]
print(arr_new)#[4 5 8]
#creating the filtering array of even numbers:
arr=np.array([3,4,2,8,5,2])
filter_arr=arr%2==0
arr_new=arr[filter_arr]
print(filter_arr)#[False True True True False True]
print(arr_new)#[4 2 8 2]
filter_arr=arr%2!=0
new_arr=arr[filter_arr]
print(filter_arr)#[True False False False True False]
print(new_arr)#[3 5]