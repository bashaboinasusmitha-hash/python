#str() method:
'''the __str__() method is a special method in python classes that is used to retuern
a readable string using representation of an object
*It defines wt should be displayed when an object is printed'''
#without__str__():
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student("susmitha",20)
print(s1)#it prints memory address of an object
#with __str__():
class Student:
    def __init__(self,name):
        self.name=name
    def __str__(self): #automatically calls the method__str__()
        return f"the name is {self.name}"
s1=Student("susmitha")
print(s1)# the name is susmitha
#Multiple Methods
'''a class can have more than one method to perform different tasks like setting data,modifying data
accessing data etc'''
class Student:
    def set_data(self,name,age):
        self.name=name
        self.age=age
    def access_data(self):#displays the details
        print(f"the name is {self.name},the age is {self.age}")
    def modify_data(self,new_age):#modify the details
        self.age=new_age
s1=Student()
s1.set_data("susmitha",21)
s1.modify_data(20)#updated value of age to 20
s1.access_data()
#delete methods:
'''we can delete mmethods from class by using del keyword'''
class Person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print("Hello" ,self.name)
p1=Person("susmitha")
del Person.greet
#p1.greet() #this cause an error