"""
METHODS
"""


# ============================================================
# 1. INTRODUCTION TO METHODS
# ============================================================

"""
A method is a function that is defined inside a class.

Methods are used to define the behavior of objects.

For example, a Car object can have methods such as:

- start()
- stop()
- accelerate()

A method can read an object's data, modify its data, or perform
some other action.

The main difference between a method and a regular function is
where it is defined and how it is normally used.

Function:
    Defined outside a class.

Method:
    Defined inside a class and usually called through an object.
"""


# ============================================================
# 2. REGULAR FUNCTION VS METHOD
# ============================================================

"""
A regular function is defined outside a class.

Example:

def greet():
    print("Hello")

A method is defined inside a class.

Example:

class Person:
    def greet(self):
        print("Hello")

The method is associated with objects created from the class.
"""

# Function

def welcome_user():
    print("Welcome to Python!")

welcome_user()

# Method

class Person:
    def greet(self):
        print("Hello from a method.")

person_object = Person()

person_object.greet()


# ============================================================
# 3. WHAT IS AN INSTANCE METHOD?
# ============================================================

"""
An instance method is a method that works with a particular
object.

The first parameter of an instance method is conventionally
named self.

Example:

class Student:
    def display(self):
        print("Student information")


student_object=Student()
student_object.display()

Here, display() is an instance method.

The self parameter refers to the current object.
"""


class Student:
    def display(self):
        print("Student information")


student_object=Student()

student_object.display()


# ============================================================
# 4. INSTANCE METHODS USE self
# ============================================================

"""
The self parameter allows an instance method to access the
data belonging to the current object.

For example:

self.name

means the name attribute belonging to the current object.
"""


class Employee:
    def set_name(self,name):
        self.name=name

    def show_name(self):
        print("Employee Name:",self.name)


employee_record=Employee()

employee_record.set_name("Hassan")
employee_record.show_name()


# ============================================================
# 5. CALLING METHODS ON OBJECTS
# ============================================================

"""
An instance method is normally called using an object.

Syntax:

object_name.method_name()

For example:

employee_record.show_name()

Python automatically passes employee_record as self.
"""


class Television:
    def turn_on(self):
        print("Television is now ON.")


living_room_tv=Television()

living_room_tv.turn_on()


# ============================================================
# 6. METHODS THAT READ DATA
# ============================================================

"""
Some methods are used only to read or display data.

These methods do not change the object's data.

For example, a Student object can have a method that displays
the student's name and age.
"""


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_information(self):
        print("Name:",self.name)
        print("Age:",self.age)


student_alpha=Student("Ayesha",20)

student_alpha.show_information()


# ============================================================
# 7. METHODS THAT MODIFY DATA
# ============================================================

"""
Other methods are used to modify the data stored inside
an object.

For example, a BankAccount object can have a method that
changes its balance.

A method can modify an instance variable by assigning a new
value to self.variable.
"""


class BankAccount:
    def __init__(self,balance):
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount


savings_account=BankAccount(5000)

print("Before deposit:",savings_account.balance)

savings_account.deposit(2000)

print("After deposit:",savings_account.balance)


# ============================================================
# 8. READ METHOD VS MODIFY METHOD
# ============================================================

"""
A method that reads data usually retrieves or displays
information.

A method that modifies data changes the object's state.

For example:

show_balance()
    Reads the balance.

deposit()
    Modifies the balance.
"""


class Wallet:
    def __init__(self,amount):
        self.amount=amount

    def show_amount(self):
        print("Wallet Amount:",self.amount)

    def add_money(self,amount):
        self.amount+=amount


personal_wallet=Wallet(3000)

personal_wallet.show_amount()

personal_wallet.add_money(1500)

personal_wallet.show_amount()


# ============================================================
# 9. METHODS CAN PERFORM ACTIONS
# ============================================================

"""
Methods are not limited to displaying or modifying variables.

They can also perform actions.

For example, a machine can have methods that start and stop
the machine.
"""


class Machine:
    def start(self):
        print("Machine started.")

    def stop(self):
        print("Machine stopped.")


factory_machine=Machine()

factory_machine.start()
factory_machine.stop()


# ============================================================
# 10. PASSING EXTRA ARGUMENTS TO METHODS
# ============================================================

"""
An instance method can accept additional parameters besides
self.

For example:

def add_score(self,points):

Here:

self
    Refers to the current object.

points
    Is an additional argument provided when the method is called.
"""


class GamePlayer:
    def __init__(self,name):
        self.name=name
        self.score=0

    def add_score(self,points):
        self.score+=points

    def show_score(self):
        print(self.name,"has",self.score,"points.")


game_player=GamePlayer("Hamza")

game_player.add_score(10)
game_player.add_score(25)

game_player.show_score()


# ============================================================
# 11. METHODS WITH MULTIPLE ARGUMENTS
# ============================================================

"""
A method can accept multiple arguments.

The self parameter comes first, followed by the other
parameters.

For example:

def update_profile(self,email,city):

self
    Current object.

email
    Additional argument.

city
    Additional argument.
"""


class Customer:
    def __init__(self,name):
        self.name=name
        self.email=""
        self.city=""

    def update_profile(self,email,city):
        self.email=email
        self.city=city

    def show_profile(self):
        print("Name:",self.name)
        print("Email:",self.email)
        print("City:",self.city)


customer_record=Customer("Mariam")

customer_record.update_profile(
    "mariam@example.com",
    "Lahore"
)

customer_record.show_profile()


# ============================================================
# 12. METHODS CAN RETURN VALUES
# ============================================================

"""
A method can also return a value using the return statement.

For example, a Rectangle object can have a method that
calculates and returns its area.
"""


class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def calculate_area(self):
        return self.length*self.width


room_rectangle=Rectangle(10,6)

area=room_rectangle.calculate_area()

print("Area:",area)


# ============================================================
# 13. METHODS CAN USE OBJECT DATA
# ============================================================

"""
A method can use multiple instance variables belonging to
the current object.

The self parameter allows the method to access those variables.
"""


class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def calculate_total(self):
        return self.price*self.quantity


order_item=Product("Keyboard",2500,3)

total_price=order_item.calculate_total()

print("Product:",order_item.name)
print("Total Price:",total_price)


# ============================================================
# 14. METHODS CAN CALL OTHER METHODS
# ============================================================

"""
A method can call another method of the same object using self.

Syntax:

self.method_name()

This allows multiple methods inside a class to work together.
"""


class Light:
    def turn_on(self):
        print("Light is ON.")

    def turn_off(self):
        print("Light is OFF.")

    def restart(self):
        self.turn_off()
        self.turn_on()


bedroom_light=Light()

bedroom_light.restart()


# ============================================================
# 15. DIFFERENCE BETWEEN ATTRIBUTES AND METHODS
# ============================================================

"""
Attributes and methods are both defined inside classes, but
they represent different things.

Attribute:
    Stores data or information about an object.

Method:
    Defines an action or behavior that an object can perform.

For example:

class Car:
    def __init__(self,brand):
        self.brand=brand

    def start(self):
        print("Car started.")

Here:

self.brand
    is an attribute.

start()
    is a method.
"""


class Car:
    def __init__(self,brand):
        self.brand=brand

    def start(self):
        print(self.brand,"has started.")


family_car=Car("Toyota")

print("Attribute:",family_car.brand)

family_car.start()


# ============================================================
# 16. ACCESSING ATTRIBUTES VS CALLING METHODS
# ============================================================

"""
An attribute is accessed without parentheses.

Example:

object.name

A method is called using parentheses.

Example:

object.show_name()

This is an important difference.

Attribute:
    object.attribute

Method:
    object.method()
"""


class Book:
    def __init__(self,title):
        self.title=title

    def display_title(self):
        print("Book Title:",self.title)


reading_book = Book("Python Programming")

# Accessing an attribute
print(reading_book.title)

# Calling a method
reading_book.display_title()


# ============================================================
# 17. ATTRIBUTE STORES DATA, METHOD PERFORMS ACTION
# ============================================================

"""
A simple way to remember the difference is:

Attribute=What an object has.

Method=What an object does.

For example, a MobilePhone can have:

Attributes:
    brand
    model
    battery

Methods:
    call()
    charge()
    restart()
"""


class MobilePhone:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def call(self):
        print("Calling from",self.model)

    def restart(self):
        print(self.model,"is restarting.")


smartphone=MobilePhone("Samsung","Galaxy A55")

print("Brand:",smartphone.brand)
print("Model:",smartphone.model)

smartphone.call()
smartphone.restart()


# ============================================================
# 18. METHODS CAN READ AND MODIFY THE SAME DATA
# ============================================================

"""
A class can have different methods that work with the same
instance variable.

One method may modify the variable.

Another method may read the variable.

This creates a clear way to control how an object's data
is used.
"""


class Counter:
    def __init__(self):
        self.value=0

    def increase(self):
        self.value+=1

    def decrease(self):
        self.value-=1

    def show_value(self):
        print("Current Value:",self.value)


number_counter=Counter()

number_counter.increase()
number_counter.increase()
number_counter.increase()

number_counter.show_value()

number_counter.decrease()

number_counter.show_value()


# ============================================================
# 19. METHODS WITH DIFFERENT OBJECTS
# ============================================================

"""
The same method can work with different objects.

The value of self changes depending on which object calls
the method.

This allows one class to define behavior that can be used
by many objects.
"""


class Dog:
    def __init__(self,name):
        self.name=name

    def bark(self):
        print(self.name,"says Woof!")


dog_one=Dog("Bruno")
dog_two=Dog("Max")

dog_one.bark()
dog_two.bark()


# ============================================================
# 20. A COMPLETE METHOD EXAMPLE
# ============================================================

"""
Let's combine the concepts we have learned.

We will create a ShoppingCart class.

The class will have:

Attribute:
    items

Methods:
    add_item()
    remove_item()
    show_items()
    item_count()

Some methods will modify the object's data, while others
will read the data.
"""


class ShoppingCart:
    def __init__(self):
        self.items=[]

    def add_item(self,item):
        self.items.append(item)

    def remove_item(self,item):
        if item in self.items:
            self.items.remove(item)

    def show_items(self):
        print("Items:",self.items)

    def item_count(self):
        return len(self.items)


shopping_cart=ShoppingCart()

shopping_cart.add_item("Keyboard")
shopping_cart.add_item("Mouse")
shopping_cart.add_item("Monitor")

shopping_cart.show_items()

print("Number of items:",shopping_cart.item_count())

shopping_cart.remove_item("Mouse")

shopping_cart.show_items()

print("Number of items:",shopping_cart.item_count())


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. A method is a function defined inside a class.
2. A regular function is normally defined outside a class.
3. Instance methods work with a particular object.
4. The first parameter of an instance method is conventionally
   named self.
5. self refers to the current object.
6. Methods are normally called using an object:

   object.method()

7. Methods can read data stored in an object.
8. Methods can modify data stored in an object.
9. Methods can accept additional arguments after self.
10. Methods can return values using the return statement.
11. A method can call another method using self.
12. Attributes store data about an object.
13. Methods define actions or behavior of an object.
14. Attributes are accessed without parentheses:

    object.attribute

15. Methods are called with parentheses:

    object.method()

A simple way to remember the difference:

Attribute:
    What an object has.

Method:
    What an object does.

For example, a Car object can have:

    brand
    model
    color

and can perform:

    start()
    stop()
    accelerate()

In the next chapter, we will learn about class methods and
how they are different from instance methods.
"""