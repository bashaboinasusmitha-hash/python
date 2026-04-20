#Numpy searching arrays:
'''we can search array for certain values and return the indexes of that values.To seach arrays we use" where()"method.'''
import numpy as np
arr=np.array([1,2,3,4,5,4,7,4])
x=np.where(arr==4)
print(x)#(array([3,5,7]),) they are the indexes of number 4 in an array.
#finding the odd value indexes:
arr=np.array([10,11,6,7,9,4])
x=np.where(arr%2==1)
print(x)#(array([1,3,4]),)
#fnding the even values indexes in a array:
y=np.where(arr%2==0)
print(y)#(array([0, 2, 5]),)
z=np.where(arr%5==0)
print(z)#(array([0]),)
#Search sorted():
'''there is a method called "searchsorted() which performs a binary search in the array and returns the index where
the specified value would be inserted to maintain the search order.'''
arr=np.array([6,7,8,9])
x=np.searchsorted(arr,7)
print(x)#1
arr=np.array([6,8,7,9])
x=np.searchsorted(arr,7)
print(x)#1 even the 7 is in the index 2 but still the output gives 1 because the value 7 must be in index 1 to maintain order.
#Search from right side:
'''by default the this method is start search from left indexes.But we can give side="right" then start serah from right.'''
arr=np.array([6,7,8,9])
x=np.searchsorted(arr,7,side="right")
print(x)#2 from right the index of 7 is 2
arr=np.array([6,8,7,9])
x=np.searchsorted(arr,7,side="right")
print(x)#3 because the searchsorted() works only on sorted arrays but here the array is not sorted so it given as unexpected answer.
"NOTE:searchsorted() method is assumed to be used on sorted arrays. "
arr=np.array([6,8,7,9])
arr=np.sort(arr)
x=np.searchsorted(arr,7,side="right")
print(x)#2 because we have sorted the array.
#Multiple values:
'''to search more than one value use an array with specified values:'''
arr=np.array([1,3,5,7])
x=np.searchsorted(arr,[2,4,6])
print(x)#[1 2 3] beacause the values of specified indexes are supposed to inserted in specific place like 2 in index 1 ,4 in 3 etc.
arr=np.array([1,3,5,7])
x=np.searchsorted(arr,[1,3,7])
print(x)#[0 1 3] gives an index of 1 3 and 7