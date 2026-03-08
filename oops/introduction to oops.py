'''introduction to oops: python is a object oriented programming language,allowing you to structure your code using
classes and objects for better organization and reusability'''
#Advantages of oop:
'''provides a clear structure to programs
2.makes code easier to maintain,reuse and debug
3.helps keep your code DRY(don't Repeat Yourself)'''
#DRY principle means you should avoid writing the same code more than once
#CLASSES and OBJECTS:
'''a class defines what an object should look like,and object is created on that class
ex:class =friut,object = apple ,banana,mango
class is like blueprint for creating "objects'''
#creating a class :
'''to create any class we use keyword class'''
class MyClass:
    x=5
print(MyClass)
#creating a object:
'''create an object named p1,and print the value of x'''
p1=MyClass()
print(p1.x)
#Delete objects: use del keyword
class MyClass:
    x=5
p1=MyClass
del p1#deletes the value 5
'''multiple objects'''
#multiple objects:we can cretae multiple objects from the same class:
class MyClass:
    x=4
p1=MyClass()
p2=MyClass()
p3=MyClass()
print(p1.x)
print(p2.x)
print(p3.x)
#pass statement:
'''class definitions cannot be empty,but for any reason u have empty class with no content
then put the statement "pass" by this there is no error'''
class MyClass:
    pass