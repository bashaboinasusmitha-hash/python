#Python Inheritance
'''inheritance allow us to define a class that inherits(take) all the methods
and properties from another class.This helps in code reuse and avoid writing the same code again.'''
#parent class and Child class
'''Parent class : it is the class being inherited from ,also called as "base class
Child C;ass: it is the class that inherits from another class,also called as derived class.'''
#syntax of inheritance:
'''class Parentclass:
    #parent properties and methods
class Childclass:
    #child properties and methods'''
#creating a parent class:
class Animal: #Parent class
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)
a1=Animal("susmitha","bashaboina")
a1.printname()
#creating a child class:
class Person:#parent class
    def set_info(self,name,marks):
        self.name=name
        self.marks=marks
class Student(Person):#child class
    def display(self):
        print("Name: ",self.name)
        print("Marks: ",self.marks)
p1=Student()
p1.set_info("Chinnanna",20)#here set_info is using the child class
p1.display()
#example of inheritance:
class Person:
    def set_name(self,name):
        self.name=name
class Student(Person):
    def set_marks(self,marks):
        self.marks=marks
    def display(self):
        print("Student name is: ",self.name)
        print("The marks are: ",self.marks)
class Teacher(Person):
    def set_salary(self,salary):
        self.salary=salary
    def display(self):
        print("Teacher Name is: ",self.name)
        print("Salary is: ",self.salary)
s1=Student()
s1.set_name("Susmitha")
s1.set_marks(50)
s1.display()
t1=Teacher()
t1.set_name("Laxmi")
t1.set_salary(75000)
t1.display()
#without inheritence:
class Student:
    def set_name(self,name):
        self.name=name
    def set_marks(self,marks):
        self.marks=marks
    def display(self):
        print("Student Name:",self.name)
        print("Marks:",self.marks)
class Teacher:
    def set_name(self,name):
        self.name=name
    def set_salary(self,salary):
        self.salary=salary
    def display(self):
        print("Teacher Name:",self.name)
        print("Salary:",self.salary)
s1=Student()
s1.set_name("Susmitha")
s1.set_marks(85)
s1.display()
print()
t1=Teacher()
t1.set_name("Ravi Sir")
t1.set_salary(50000)
t1.display()
'''in above without inheritence we have written two times set_name :
 one in class Student and another in class Teacher '''