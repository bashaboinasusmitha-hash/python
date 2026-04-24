#extract first two elemnts:
import numpy as np
arr=np.array([1,7,3,2,9,0,3])
print(arr[0:2])#[1 7]
#extracting last two elements:
print(arr[-2:])#[0 3]
#Extract elements from index 1 to 3 (inclusive).
print(arr[0:3])#[1 7 3]
#Reverse the array using slicing.
arr=np.array([2,4,7,5,1,0])
n=len(arr)
print(arr[::-1])#[0 1 5 7 4 2]
#Extract elements at even indices.
print(arr[1:n:2])#[4 5 0]
#Extract elements at odd indices.
arr=np.array([2,4,7,5,1,0])
n=len(arr)
print(arr[0:n:2])#[2 7 1]
#Extract elements in reverse order skipping one element
print(arr[-1:0:-2])#[0 5 4]
#Replace elements from index 2 to 4 with 0.
arr[2:5]=0
print(arr)
#extract the elements graeter than the 4:
arr=np.array([2,4,7,5,1,0])
a=arr[arr>4]
print(a)#[7 5]