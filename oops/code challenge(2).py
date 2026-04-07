#Product Price System:
class Product:
    def __init__(self):
        self.__price=0
    def set_price(self,price):
        self.__price=price
    def get_price(self):
        return self.__price
    def discount(self,percent):
        self.percent=self.__price*(percent/100)
        self.__price-=self.percent
        print("Discounted price:",int(self.__price))
p1=Product()
p1.set_price(1000)
print("Price:",p1.get_price())
p1.discount(10)
#Password Protection program:
class UserAccount:
    def __init__(self):
        self.__password=0
    def set_password(self,password):
        self.__password=password
    def check_password(self,password):
        if password==self.__password:
            print("Access Granted!")
        else:
            print("Access Denied!")
p1=UserAccount()
p1.set_password("susmitha@160")
p1.check_password("Susmitha@160")
#Student result system:
class Student:
    def __init__(self,name):
        self.name=name
        self.__marks=0
    def set_marks(self,marks):
        self.__marks=marks
    def result(self):
        if self.__marks>=40:
            print("Pass")
        else:
            print("Fail!")
s1=Student("Susmitha")
s1.set_marks(39)
s1.result()
#Temperature converter:
class Temperature:
    def __init__(self):
        self.__celsius=0
    def set_temperature(self,temp):
        self.__celsius=temp
    def to_fahrenheit(self):
        f=(self.__celsius*9/5)+32
        print("Temperature in faherenheit:",(f))
t1=Temperature()
t1.set_temperature(37)
t1.to_fahrenheit()
#Challenge question:
class LibraryBook:
    def __init__(self):
        self.__availability=False
    def borrow_book(self):
        if self.__availability:
            #self.__availability=True
            print("Book Borrowed")
        else:
            print("Book not available!")
    def return_book(self):
        self.__availability=False
        print("Book returned")
    def check_status(self):
        if self.__availability:
            print("Not available")
        else:
            print("Available")
l1=LibraryBook()
l1.borrow_book()
l1.return_book()
l1.check_status()