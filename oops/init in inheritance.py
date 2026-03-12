#__init__() in inheritance:
'''when a child class inherits from a class
 we often want to use the parent's constructor.'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
s1=Student("Susmitha",20)
s1.display()
#Even though Student does not have __init__(),it inherits it from Person.
'''if child does not define its own constructor,it inherits its parent __init__() automatically'''
#Child Class with Its Own __init__():
'''If the child class creates its own constructor,
 the parent's constructor is NOT called automatically.'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self, name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Name: ",self.name)
        print("Marks: ",self.marks)
s1=Student("Susmitha",50)#here 50 taken as marks not age
s1.display()
'''here age is not used because the parent constructor never ran'''
#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,marks):
        Person.__init__(self,name,age)
        self.name=name
        self.marks=marks
    def display(self):
        print("Name: ",self.name)
        print("The age: ",self.age)
        print("Marks: ",self.marks)
s1=Student("Susmitha",20,51)
s1.display()
#using super() :
'''Python also has a super() function that will make the 
child class inherit all the methods and properties from its parent:'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self, name, age,marks):
        super().__init__(name, age)
        self.name=name
        self.marks=marks
    def display(self):
        print("Name: ",self.name)
        print("The age: ",self.age)
        print("Marks: ",self.marks)
s1=Student("Susmitha",20,51)
s1.display()
#Add properties:
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        def printname(self):
            print(self.fname,self.lname)
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear=2027
x=Student("Suamitha","Bashaboina")
print(x.graduationyear)
#Add Methods:
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)
class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.garduationyear=2027
x=Student("Susmitha","Bashaboina",2027)
print(x.garduationyear)
x.printname()