#NUMPY:
'''numpy is a python libarary used to work with arrays.
Numpy is short for Numerical Python.It was created by Travis Oliphant in 2005.'''
#use of numpy:
'''In python lists serves as arrays,but they are slow to process.So numpy aims to provide an array object
that is upto 50x faster than python lists.The array object in numpy called "ndarray".This ndarray provides alot of supporting 
functions and makes easy working.'''
#numpy creating arrays:
'''we can create ndarray object by using array() function'''
#example:
import numpy
arr=numpy.array([1,2,3,4,5])
print(arr)#[1,2,3,4,5]
#Numpy as np:
'''numpy is usually imported as np alias.'''
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))
#checking numpy version:
print(np.__version__)
#Dimensions in arrays:
#0-dimensions
arr=np.array(24)
print(arr)
#1-D
arr=np.array([1,2,3,4])
print(arr)
#2-D
arr=np.array([[1,2,3],[3,5,6]])
print(arr)
#3-D
arr=np.array([[[1,2,3],[4,5,6],[7,5,3]]])
print(arr)
#Checking Dimensions:
'''Numpy arrays provide "ndim" attribute returns a integer 
that tells us how many many dimensions the array have'''
a=np.array(34)
b=np.array([1,2,3])
c=np.array([[1,2,3],[3,4,5]])
d=np.array([[[1,2,3],[4,5,6],[5,6,7]]])
print(a.ndim)#0
print(b.ndim)#1
print(c.ndim)#2
print(d.ndim)#3