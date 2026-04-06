#Numpy data types:
'''by default python has "strings","integers","boolean","float","complex" but in NumPy there are some extra data types:
i- integer,b-boolean,u-unsignedinteger,f-float,c-complex float,m-timedelta,M-datetime,O-object,S-string,U-unicode string'''
#Checking data types of an array:
'''the numpy array object has a property called "dtype" that returns the datatype of array'''
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr.dtype)#int64
arr=np.array(["apple","banana"])
print(arr.dtype)#<U6
arr=np.array(["banana",39])
print(arr.dtype)#U21
arr=np.array(["banana",39,2.8])
print(arr.dtype)#U32
#Creating Arrays with a Defined Data type:
arr=np.array([1,2,3,5],dtype="S")
print(arr)#[b'1' b'2' b'3' b'5']
print(arr.dtype)#|S1
arr=np.array([1,2,3,4,5],dtype="i2")
print(arr)#[1 2 3 4 5]]
print(arr.dtype)#int16
arr=np.array([1,2,3,4,5],dtype="f2")
print(arr)#[1. 2. 3. 4. 5.]]
print(arr.dtype)#float16
#arr=np.array(["a","2","3"],dtype="i")#this gives an value error here a not converted to int
#Converting data type on existing arrays:
'''we can convert a data  by using astype() method.The astype() creates a copy of array and allow us to specify
the datatype as a parameter.the astype() allow us to write a datatype using string like'f' or 'i' and also we can write like 'float','int' '''
#changing datatype from float to integer:
arr=np.array([1.1,2.3,3.5])
print(arr)#[1.1 2.3 3.5]
print(arr.dtype)#float64
newarry=arr.astype(int)
print(newarry)#[1 2 3]
print(newarry.dtype)#int64
#changing datatype from float to integer by using "i"
arr=np.array([1.1,2.3,3.5])
b=arr.astype("i")
print(b)
print(b.dtype)
#Changing datatype from integer to boolean:
arr=np.array([1,0,-1])
b=arr.astype(bool)
print(b)#[True False True]
print(b.dtype)
arr=np.array([1,0,-1,3])
b=arr.astype(bool)
print(b)#[True False True True]
print(b.dtype)#bool