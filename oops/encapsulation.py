#Encapsulation :
'''Encapsulation is about protecting data inside a class.it means keeping data(properties)
and methods together in a class,while controlling how the data can be accessed from outside class.
This prevents the accidental changes to your data and hides the internal details of how ur class works'''
#Private Properties:
'''in python we can keep properties private by using a doblue underscore(__)prefix:'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age #this is private property so it cannot be accessed directly outside the class.
p1=Person("Susmitha",20)
print(p1.name)
#print(p1.__age) # this cause an error
#Get private property value:
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def get_age(self):
        return self.__age
p1=Person("susmitha",20)
print(p1.name,p1.get_age())
print(p1.get_age())
#Set private property value:
'''to modify the private property value we need to create setter method
the setter method can also validate the value before setting it '''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("The age must be positive!")
p1=Person("susmitha",20)
print(p1.name,p1.get_age())
p1.set_age(0)
#y use of encapsulation:
'''Data Protection:prevent accidental modification of data
,Validation:we can validate data before setting it,
Flexibity:internal implementation can change without affecting external code
Control:you have full control over how data is accessed and modified '''
class Student:
    def __init__(self,name):
        self.name=name
        self.__grade=0
    def set_grade(self,grade):
        if 0<=grade<=100:
            self.__grade=grade
        else:
            print("The grade must be between 0 and 100")
    def get_grade(self):
        return self.__grade
    def get_status(self):
        if self.__grade>=60:
            return("passed") 
        else:
            return("Failed")
s1=Student("Susmitha")
s1.set_grade(79)
print(s1.get_grade())
print(s1.get_status())