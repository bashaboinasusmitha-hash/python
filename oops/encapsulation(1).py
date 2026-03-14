#Protected properties in concept of encapsulation:
'''python has a convention for protecting a properties using single underscore(_)prefix:'''
class Person:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary
class Teacher(Person):
    def display(self):
        print("Name:",self.name)
        print("Salary:",self._salary)
t1=Teacher("susmitha",20000)
t1.display()
# the below code still works :But according to programming convention,
#  we should not access it directly outside the class.
p1=Person("susmitha",21000) 
print(p1._salary)
#private methods:
'''A private method is a method that can only be used inside the same class and cannot be accessed directly from outside the class.
we can also make methods private using double underscore prefix'''
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __calculate_grade(self):
        if self.marks>=90:
            return "A"
        else:
            return "B"
    def display(self):
        grade=self.__calculate_grade()
        print("Name:",self.name)
        print("Marks:",self.marks)
        print("Grade:",grade)
s1=Student("susmitha",92)
s1.display()
#if we write t1.__calculate_grade() it gives an error
#Name Mangling:
'''Name Mangling is a mechanism Python uses to protect 
private variables and methods from being accessed directly outside the class.
When we create a private variable or method using two underscores
 __, Python automatically changes its name internally.'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age
p1 = Person("Ravi", 30)
print(p1._Person__age)