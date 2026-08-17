"""
CONSTRUCTORS
"""


# ============================================================
# 1. INTRODUCTION TO CONSTRUCTORS
# ============================================================

"""
A constructor is a special method that is automatically called
when an object is created from a class.

Constructors are commonly used to initialize the data of an
object.

For example, when we create a Student object, we may want to
give the object a name and an age immediately.

A constructor allows us to initialize these values when the
object is created.

In Python, the constructor is commonly written using:

__init__()
"""


# ============================================================
# 2. WHY DO WE NEED A CONSTRUCTOR?
# ============================================================

"""
Suppose we create a class called Student.

After creating a Student object, we may want the object to
have information such as:

- Name
- Age
- Course

Without a constructor, we would need to create the object
first and then assign these values separately.

A constructor allows us to initialize the object's data
during object creation.

This makes the code cleaner and easier to understand.
"""


class Student:
    pass


student_record=Student()

student_record.name="Hassan"
student_record.age=20

print("Name:",student_record.name)
print("Age:",student_record.age)


# ============================================================
# 3. __init__() METHOD
# ============================================================

"""
The __init__() method is a special method in Python.

It is automatically called when an object is created.

Basic syntax:

class ClassName:
    def __init__(self):
        # initialization code

The __init__() method normally contains self as its first
parameter because it is an instance method.

It can also contain additional parameters that are used to
initialize object data.
"""


class Student:
    def __init__(self):
        print("Student object has been created.")


student_one=Student()
student_two=Student()


# ============================================================
# 4. HOW __init__() WORKS
# ============================================================

"""
When we create an object:

student=Student()

Python automatically calls the __init__() method.

It is approximately equivalent to:

Student.__init__(student)

This means that the newly created object is automatically
passed to self.
"""


class Computer:
    def __init__(self):
        print("Computer initialized.")


office_computer=Computer()


# ============================================================
# 5. CONSTRUCTOR WITH OBJECT DATA
# ============================================================

"""
The main purpose of a constructor is usually to initialize
the data of an object.

We can use self inside __init__() to store data in the object.

For example:

self.name=name

The value is stored as an attribute of the current object.
"""


class Employee:
    def __init__(self):
        self.department="Sales"
        self.experience=2


sales_employee=Employee()

print("Department:",sales_employee.department)
print("Experience:",sales_employee.experience)


# ============================================================
# 6. DEFAULT CONSTRUCTOR
# ============================================================

"""
A default constructor is a constructor that does not require
additional arguments when an object is created.

For example:

class Vehicle:
    def __init__(self):
        self.type="Car"

The object can be created simply using:

vehicle = Vehicle()

No additional values are required during object creation.
"""


class Vehicle:
    def __init__(self):
        self.vehicle_type="Car"
        self.wheels=4


family_vehicle=Vehicle()

print("Vehicle Type:",family_vehicle.vehicle_type)
print("Wheels:",family_vehicle.wheels)


# ============================================================
# 7. DEFAULT CONSTRUCTOR WITH DIFFERENT OBJECTS
# ============================================================

"""
A default constructor can initialize every object with the
same starting values.

For example, every new Account object can initially have a
balance of zero.
"""


class Account:
    def __init__(self):
        self.balance=0


account_one=Account()
account_two=Account()

print("Account One Balance:",account_one.balance)
print("Account Two Balance:",account_two.balance)


# ============================================================
# 8. PARAMETERIZED CONSTRUCTOR
# ============================================================

"""
A parameterized constructor accepts additional arguments.

This allows us to give different values to different objects
when they are created.

Syntax:

class ClassName:
    def __init__(self,parameter):
        self.attribute=parameter

The values are provided when the object is created.
"""


class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price


keyboard_item=Product("Keyboard",2500)

print("Product:",keyboard_item.name)
print("Price:",keyboard_item.price)


# ============================================================
# 9. PASSING ARGUMENTS DURING OBJECT CREATION
# ============================================================

"""
When a constructor has parameters, we must provide the required
values while creating the object.

For example:

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

We can create an object using:

book=Book("Python Basics","Daniel")

The values are passed to the __init__() method automatically.
"""


class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author


reading_book=Book("Python Basics","Daniel")

print("Title:",reading_book.title)
print("Author:",reading_book.author)


# ============================================================
# 10. CREATING MULTIPLE OBJECTS WITH DIFFERENT VALUES
# ============================================================

"""
A parameterized constructor allows different objects created
from the same class to have different data.

For example, we can create several Product objects with
different names and prices.
"""


class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price


product_alpha=Product("Monitor",35000)
product_beta=Product("Keyboard",3000)
product_gamma=Product("Mouse",1800)

print("Product Alpha:",product_alpha.name,product_alpha.price)
print("Product Beta:",product_beta.name,product_beta.price)
print("Product Gamma:",product_gamma.name,product_gamma.price)


# ============================================================
# 11. MULTIPLE PARAMETERS IN A CONSTRUCTOR
# ============================================================

"""
A constructor can have multiple parameters.

Each parameter can be used to initialize a different
attribute of the object.

For example, a Laptop object can store:

- Brand
- Model
- RAM
"""


class Laptop:
    def __init__(self,brand,model,ram):
        self.brand=brand
        self.model=model
        self.ram=ram


work_laptop=Laptop("Lenovo","ThinkPad E14",16)

print("Brand:",work_laptop.brand)
print("Model:",work_laptop.model)
print("RAM:",work_laptop.ram,"GB")


# ============================================================
# 12. SETTING DEFAULT VALUES FOR PARAMETERS
# ============================================================

"""
Constructor parameters can have default values.

A default value is used when the caller does not provide
a value for that parameter.

Syntax:

def __init__(self,name="Unknown"):
    self.name=name

This makes the parameter optional.
"""


class Customer:
    def __init__(self,name="Unknown"):
        self.name=name


customer_one=Customer("Ayesha")
customer_two=Customer()

print("Customer One:",customer_one.name)
print("Customer Two:",customer_two.name)


# ============================================================
# 13. MULTIPLE DEFAULT PARAMETERS
# ============================================================

"""
A constructor can have multiple parameters with default values.

This allows an object to be created with all values, some
values, or none of the optional values.
"""


class Employee:
    def __init__(self,name="Unknown",department="General"):
        self.name=name
        self.department=department


employee_alpha=Employee("Bilal","IT")
employee_beta=Employee("Mariam")
employee_gamma=Employee()

print("Employee Alpha:",employee_alpha.name,employee_alpha.department)
print("Employee Beta:",employee_beta.name,employee_beta.department)
print("Employee Gamma:",employee_gamma.name,employee_gamma.department)


# ============================================================
# 14. REQUIRED AND DEFAULT PARAMETERS
# ============================================================

"""
A constructor can contain both required and default parameters.

Required parameters must receive a value.

Parameters with default values are optional.

For example:

def __init__(self,name,city="Unknown"):

name is required.

city has a default value.
"""


class Resident:
    def __init__(self,name,city="Unknown"):
        self.name=name
        self.city=city


resident_one=Resident("Hamza","Lahore")
resident_two=Resident("Zainab")

print("Resident One:",resident_one.name,resident_one.city)
print("Resident Two:",resident_two.name,resident_two.city)


# ============================================================
# 15. CONSTRUCTOR VS REGULAR METHOD
# ============================================================

"""
A constructor and a regular method are both defined inside
a class, but they have different purposes.

Constructor:
    - Uses the special name __init__().
    - Runs automatically when an object is created.
    - Usually initializes object data.
    - Does not normally need to be called manually.

Regular method:
    - Can have any valid method name.
    - Runs when we explicitly call it.
    - Usually performs an action or operation.
    - Can be called multiple times.

For example:

__init__()
    Initializes an object.

display()
    Displays information when we call it.
"""


class Device:
    def __init__(self,name):
        self.name=name

    def show_name(self):
        print("Device Name:",self.name)


printer_device=Device("Printer")

printer_device.show_name()


# ============================================================
# 16. CONSTRUCTOR RUNS AUTOMATICALLY
# ============================================================

"""
The __init__() method is automatically executed when an object
is created.

A regular method does not run automatically.

We have to call a regular method ourselves.
"""


class Machine:
    def __init__(self):
        print("Constructor executed.")

    def start_machine(self):
        print("Regular method executed.")


factory_machine=Machine()

factory_machine.start_machine()


# ============================================================
# 17. CONSTRUCTOR AND REGULAR METHOD TOGETHER
# ============================================================

"""
A class can have both a constructor and multiple regular
methods.

The constructor can initialize the object's data.

Regular methods can then use that data to perform actions.
"""


class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount

    def show_balance(self):
        print("Owner:",self.owner)
        print("Balance:",self.balance)


savings_account=BankAccount("Ali",5000)

savings_account.deposit(1500)
savings_account.show_balance()


# ============================================================
# 18. CONSTRUCTOR INITIALIZES EACH OBJECT SEPARATELY
# ============================================================

"""
When multiple objects are created, the constructor runs for
each object separately.

This means each object gets its own initialized data.
"""


class MobilePhone:
    def __init__(self,company,model):
        self.company=company
        self.model=model


phone_one=MobilePhone("Samsung","Galaxy A55")
phone_two=MobilePhone("Apple","iPhone 15")

print("Phone One:")
print("Company:",phone_one.company)
print("Model:",phone_one.model)

print()

print("Phone Two:")
print("Company:",phone_two.company)
print("Model:",phone_two.model)


# ============================================================
# 19. CONSTRUCTOR WITH DEFAULT VALUES
# ============================================================

"""
Default parameter values are useful when we want to provide
a common starting value.

For example, a game character can start with 100 health
unless another value is provided.
"""


class GameCharacter:
    def __init__(self,name,health=100):
        self.name=name
        self.health=health


warrior_character=GameCharacter("Warrior")
wizard_character=GameCharacter("Wizard",80)

print("Warrior:",warrior_character.name,warrior_character.health)
print("Wizard:",wizard_character.name,wizard_character.health)


# ============================================================
# 20. COMPLETE CONSTRUCTOR EXAMPLE
# ============================================================

"""
Let's combine the concepts we have learned.

We will create a LibraryBook class.

The constructor will initialize:

- Title
- Author
- Price

A regular method will display the book information.

The constructor runs automatically when the object is created.

The display method runs only when we call it.
"""


class LibraryBook:
    def __init__(self,title,author,price=1000):
        self.title=title
        self.author=author
        self.price=price

    def display_information(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)


book_one=LibraryBook(
    "Learning Python",
    "Emma Wilson",
    2500
)

book_two=LibraryBook(
    "Python OOP",
    "David Miller"
)

print("Book One:")
book_one.display_information()

print()

print("Book Two:")
book_two.display_information()


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. A constructor is a special method used to initialize an
   object.
2. In Python, the constructor is commonly written as __init__().
3. The __init__() method runs automatically when an object is
   created.
4. The first parameter of __init__() is self.
5. A default constructor does not require additional arguments
   during object creation.
6. A parameterized constructor accepts additional arguments.
7. Arguments can be passed when creating an object.
8. Constructor parameters can have default values.
9. Default values make parameters optional.
10. A constructor can have both required and optional parameters.
11. The constructor usually initializes object attributes.
12. A regular method is called explicitly by using the object.
13. A constructor runs automatically during object creation.
14. A regular method can be called multiple times.
15. Each object gets its own initialized data when the
    constructor runs.

The main difference is:

Constructor:
    Automatically initializes the object.

Regular Method:
    Performs an action when explicitly called.

In the next chapter, we will learn about instance variables
and class variables and understand how data can belong to
individual objects or to the class itself.
"""