#construction of basic inner class:
class Student:
    class Laptop:
        def __init__(self):
            self.name="Susmitha"
            self.brand="Dell"
            self.ram=128
s1=Student()
lap=Student.Laptop()
print(lap.name)
print(lap.brand)
print(lap.ram)
#code on accessing inner class from outside 
class Car:
    class Engine:
        def start(self):
            self.status="ON"
        def display(self):
            print("Car started!")
c1=Car()
e1=Car.Engine()
e1.start()
e1.display()
#Access outer class from inner class:
class Person:
    def __init__(self):
        self.name="Susmitha"
    class Address:
        def __init__(self,person):
            self.name=person.name
            self.city="Hanumakonda"
        def display(self):
            print("The name:",self.name,"from",self.city)
p1=Person()
a1=Person.Address(p1)
a1.display()
#Multiple inner classes:
class Computer:
    class CPU:
        def process(self):
            self.cores=8
            print("The cpu process:",self.cores)
    class RAM:
        def stores(self):
            self.ram="8gb"
            print("it stores the ram of :",self.ram)
com=Computer()
cpu=Computer.CPU()
cpu.process()
ram=Computer.RAM()
ram.stores()
#helper classes:
class School:
    def __init__(self,school_name):
        self.school_name=school_name
        self.classroom=self.Classroom()
    class Classroom:
        def __init__(self):
            self.room_no=104
    def display(self):
        print("The school name:",self.school_name)
        print("The room  no:",self.classroom.room_no)
s1=School("Cambridge")
s1.display()