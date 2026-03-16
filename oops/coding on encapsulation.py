#basic private property:
class Student:
    def __init__(self):
        self.__marks=0
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        self.__marks=marks
c1=Student()
c1.set_marks(85)
print("Marks:",c1.get_marks())
#Bank Account System:
class BankAccount:
    def __init__(self):
        self.__balance=0
    def deposite(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount
    def show_balance(self):
        return self.__balance 
b1=BankAccount()
b1.deposite(5000)
b1.withdraw(500)
print("Balance:",b1.show_balance())
#Employee salary:
class Employee:
    def __init__(self):
        self.__salary=0
    def set_salary(self,amount):
        self.__salary=amount
    def get_salary(self):
        return self.__salary
    def increase_salary(self,amount):
        self.__salary+=amount
        print("Increased Salary:",self.__salary)
e1=Employee()
e1.set_salary(50000)
print("Salary:",e1.get_salary())
e1.increase_salary(5000)
#Protected Property:
class Person:
    def __init__(self,age):
        self._age=age
class Student(Person):
    def display(self):
        print("Age:",self._age)
p1=Student(20)
p1.display()
#Private Property Access:
class Car:
    def __init__(self):
        self.__speed=0
    def set_speed(self,speed):
        self.__speed=speed
    def get_speed(self):
        print("speed:",self.__speed)
c1=Car()
c1.set_speed("120 km/h")
c1.get_speed()