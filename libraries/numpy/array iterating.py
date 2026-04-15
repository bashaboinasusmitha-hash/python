#Iterating an array:
'''iterating an array means going to every element one by one. for that we use "for" loop.'''
#iterating 1-D :
import numpy as np
arr=np.array([1,2,3,4])
for i in arr:
    print(i)
#output:
'''1
2
3
4'''
#Iterating 2-D array:
'''here the loop go through each row:'''
arr=np.array([[1,2,3],[4,5,6]])
for i in arr:
    print(i)
#output:
'''[1,2,3]
[4,5,6]
for iterating evry element we use double for loop'''
for i in arr:
    for j in i:
        print(j)
#1 2 3 4 5 6 
#iterating 3D 
'''In a 3-D array it will go through all the 2-D arrays.'''
arr=np.array([[[1,2,3],[3,4,5]],[[7,9,10],[10,3,9]]])
for i in arr:
    print("x represents 2-D:")
    print(i)
#output:
'''x represents 2-D:
[[1 2 3]
 [3 4 5]]
x represents 2-D:
[[ 7  9 10]
 [10  3  9]]'''
#iterating every elemnt needs 3 for loops:
for i in arr:
    for j in i:
        for k in j:
            print(k)# 1 2 3 3 4 5 7 8 9 10 3 9
#Iterating arrays using nditer()
'''the function "nditer()" is a helping function that can be used from very basic to very advanced iterations.
"Iterating on each element:" it become difficult use n loops for n dimensions so we have nditer().'''
import numpy as np
arr=np.array([[[1,2],[3,7]],[[5,6],[7,8]]])
for i in np.nditer(arr):
    print(i)#1 2 3 7 5 6 7 8
#Iterating Array with different data types:
'''we can use "op_dtypes" argument and pass the expected datatype to change the datatype while iterating the elements.
numpy does not change data type of the element in place so it need some other extra space that extra space is called buffer.
and in order to change in nditer() we pass flags=["buffered"]'''
arr=np.array([1,2,3])
for i in np.nditer(arr,flags=["buffered"],op_dtypes=['S']):
    print(i)#np.bytes_(b'1') np.bytes_(b'2') np.bytes_(b'3')
#iterating with step size:
arr=np.array([[1,2,3],[5,6,7]])
for i in np.nditer(arr[:,::2]):
    print(i)#1 3 5 7
#Enumerated iteration using ndenumerater():
'''It is used to iterate through a NumPy array with index + value'''
arr=np.array([1,2,3])
for index,i in np.ndenumerate(arr):
    print(index,i)#(0,) 1 (1,) 2 (2,) 3
arr=np.array([[1,3,4],[5,6,8]])
for index ,i in np.ndenumerate(arr):
    print(index,i)
#output:
'''(0, 0) 1
(0, 1) 3
(0, 2) 4
(1, 0) 5
(1, 1) 6
(1, 2) 8'''
arr=np.array(["a","b","c"])
for i in arr:
    print("Hello "+ i)#Hello a Hello b Hello c