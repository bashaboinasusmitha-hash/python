#self parameter:
'''self parameter is a reference to the current instance of class.
*it is used to access properties and methods that belong to the class
*self must be the first parameter of every instance method.'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print("hello my name is:"+" " +self.name)
p1=Person("susmitha",20)
p1.greet()
print(p1.name)
print(p1.age)
#why use self:
'''without self python don't know which object's properties you want to access'''
class Person:
    def __init__(self,name):
        self.name=name
    def printname(self):
        print(self.name)
p1=Person("susmitha")
p2=Person("ravinder")
p1.printname()
p2.printname()
#self does not have to be named "self":
'''it does not have to be named self,we can call it whatever we like,
but it has to be the first parameter of any method in the class'''
class Person:
    def __init__(mydetails,name,age):
        mydetails.name=name
        mydetails.age=age
    def greet(mydetails):
        print("hello :",mydetails.name)
p1=Person("susmitha",20)
p1.greet()
#Accessing properties with self:
'''we can access any property off the class using self:'''
class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def displayinfo(self):
        print(f"{self.year} {self.brand} {self.model}")
car1=Car("toyota","corolla",2000)
print(car1.model)
car1.displayinfo()      
#calling methods using self:
'''we can also call other methods within the class using self'''
class Person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        return "hello" +" " + self.name
    def welcome(self):
        msg=self.greet()
        print(msg,"!welcome to our website.")
p1=Person("susmitha")
p1.welcome()