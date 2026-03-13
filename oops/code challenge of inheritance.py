class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(self.name)
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
d1=Dog("Rex")
d1.speak()
#code challenge for polymorphism:
class Cat:
    def sound(self):
        print("Meow")
class Fox:
    def sound(self):
        print("Wa-pa-pa-pa-pa-pow!")
c1=Cat()
f1=Fox()
c1.sound()
f1.sound()
#inheritsnce :
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self, name,age,marks):
        super().__init__(name, age)
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)
s1=Student("susmitha",20,90)
s1.display()
#person->Student->Teacher:
class Person:
    def __init__(self,name):
        self.name=name
class Student(Person):
    def __init__(self, name,marks):
        super().__init__(name)
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Marks:",self.marks)
class Teacher(Person):
    def __init__(self, name,salary):
        super().__init__(name)
        self.salary=salary
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
s1=Student("susmitha",90)
s1.display()
t1=Teacher("Ravi",100000)
t1.display()