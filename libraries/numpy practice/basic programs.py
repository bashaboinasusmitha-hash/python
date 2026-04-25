#Creating a numpy array of elements from 1 to 10:
import numpy as np
arr=np.arange(1,11)
print(arr)
#creating an array filled with zeros(3x3)
arr=np.zeros((3,3))
print(arr)
#creating an 2x4 numpy array ffilled with ones
arr=np.ones((2,4))
print(arr)
#Generate an array of even numbers from 2 to 20.
arr=np.arange(2,21,2)
print(arr)
#Indexing and slicing:
'''Extract the first 3 elements from an array.'''
arr=np.array([1,8,2,7,4,5])
print(arr[0:3])
#Reverse an array.
print(arr[::-1])
'''From a 2D array, extract:
first row
last column'''
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr[0])
print(arr[::-1])
print(arr[:,-1])