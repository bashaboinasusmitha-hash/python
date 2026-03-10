#Python Class Methods
'''A class methods is a method that is bound to the class instaed of object
*It can access and modify the class variables
*It cannot directly access the instance variables
*It uses cls instead of self'''
class Student:
    college="GuruNanak institute of Technology"#class variable(college)
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_college(cls,new_name):#change_college=class method
        cls.college=new_name  #it modifies the class variable
print(Student.college)
Student.change_college("GNIT")
print(Student.college)
#methods with parameters:
'''A method with parameters is a function inside the class thet accepts 
values(arguments) when it is called
*Method->function inside the class
*Parameter -> values passed to method'''
class Student:
    def display(self,name,marks):
        self.name=name
        self.marks=marks
s1=Student()
s1.display("susmitha",50)
print("the name is :",s1.name)
print("the marks are :",s1.marks)
class Details:
    def display(self,name,age):
        print("Name :" ,name)
        print("Age :", age)
d1=Details()
d1.display("susmitha",20)#method calling 
class Calculator:
    def add(self,num1,num2):
        return num1+num2
    def mul(self,num1,num2):
        return num1*num2
c1=Calculator()
print("the adition is : ",c1.add(10,2))
print("the multiplication is :",c1.mul(2,4))
#Methods Accessing properties:
'''methods accessing proprties means methods that read or use the properties of object
*These methods use self to access the properties'''
class Student:
    def info(self,name,marks):#info stores the values in properties
        self.name=name
        self.marks=marks
    def display(self): # display() uses the proprties stored by info()
        print("Name",self.name)
        print("Marks :",self.marks)
s1=Student()
s1.info("susmitha",98)
s1.display()
#Methods modifying properties:
'''methods modify the properties are methods that change or upadate the value of object properties'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age =age
    def birthday(self):
        self.age+=1
        print("happy birthday! now u are " ,self.age, "old")
p=Person("Suma",19)
p.birthday()#20
p.birthday()#21
p.birthday()#22