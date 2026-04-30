#random module:
'''What is random number:
Random number does NOT mean a different number every time. Random means something that can not be predicted logically.'''
#generate random number:
'''randint():used to print random integer it takes a number as parameter and generate a random number upto the given number.'''
from numpy import random
x=random.randint(100)
print(x)#62
'''everytime this will print a random number from 0 to 100 '''
#generate random float number:
'''rand(): this method generates a random float number between 0 to 1.'''
x=random.rand()
print(x)#0.2900459098894377
'''everytime this will print a random float number b/w 0 to 1'''
#Generate the random array:
'''Integer: 
the randint() method takes a size parameter where u can specify the shape of an array.'''
x=random.randint(100,size=(5))
print(x)#[44 32 18 28 75]
'''this will print an 1-D array of 5 elements,the elements are randomly picked from 0 to 100
here size=5 is the no.of elements in an array.'''
#2-D array:
x=random.randint(100,size=(3,3))
print(x)
'''[[ 8 46 98]
    [10 93 83]
    [65 47 57]]
this will print 2-D array of size 3 rows,3 columns(each row contains 3 elements.),the elements are randomly picked from 0 to 100.'''
#Float:
'''the rand() allows us to specify  the shape of an array.
1-D array:'''
x=random.rand(5)
print(x)#[0.76451916 0.52340096 0.16425052 0.38708577 0.51404499]
'''this will print an 1-D array of 5 random float numbers b/w 0 to 1.'''
#2-D array:
x=random.rand(3,3)
print(x)
'''output:
[[0.87406468 0.96641207 0.76530711]
 [0.59440201 0.69021756 0.97361566]
 [0.21611865 0.82249356 0.45907353]]
rand(3,3) the first 3 indicates rows and second 3 indicates no.of columns.The elements are randomly generated float numbers b/w 0 to 1.'''
#Generate Random Number from Array:
'''The choice() method allows you to generate a random value based on an array of values
The choice() method takes an array as a parameter and randomly returns one of the values.'''
x=random.choice([3,8,5,9,7])
print(x)#8
'''the choice() method will pick one random number from array.'''
#The choice() method also allows you to return an array of values.
#Add a size parameter to specify the shape of the array.
x=random.choice([3,6,7,5,9],size=(3,5))
print(x)
'''[[9 9 7 7 7]
    [9 9 5 3 3]
    [9 3 7 5 9]]'''