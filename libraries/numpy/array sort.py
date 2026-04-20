#Sorting numpy arrays:
'''sorting arrays menas putting all the elements in a ordered sequence.Ordered sequence is any sequence
 that has an order corresponding to any elements like numberic or alphabetic ascending or descending order.'''
import numpy as np
arr=np.array([1,0,4,2,4,9])
arr_sort=np.sort(arr)
print(arr_sort)#[0 1 2 3 4 4 9]
#alphabetic:
arr=np.array(["banana","apple","dragon","cherri"])
arr_sort=np.sort(arr)
print(arr_sort)#["apple" "banana" "cherri" "dragon"]
#NOTE: this method returns a copy of an array and unchanged the original array.
arr=np.array(["banana","apple","dragon","cherri"])
arr_sort=np.sort(arr)
arr_sort[0]="anu"
print(arr_sort)#['anu' 'banana' 'cherri' 'dragon']
print(arr)#['banana' 'apple' 'dragon' 'cherri'] here the original array is unchanged.
#Sort a boolean array:
arr=np.array([True,False,True])
arr_sort=np.sort(arr)
print(arr_sort)#[False  True  True]
#Sorting 2-D array:
arr=np.array([[3,1,2],[7,5,6]])
arr_sort=np.sort(arr)
print(arr_sort)
#output:
'''[[1 2 3]
    [5 6 7]]'''
#3-d array sorting:
arr=np.array([[[1,4,2,6],[9,4,2,3]],[[0,1,7,4],[9,3,6,1]]])
print(np.sort(arr))
#output:
'''[[[1 2 4 6]
  [2 3 4 9]]
 [[0 1 4 7]
  [1 3 6 9]]]'''