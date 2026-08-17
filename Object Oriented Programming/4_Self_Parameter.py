"""
SELF PARAMETER
"""


# ============================================================
# 1. INTRODUCTION TO self
# ============================================================

"""
The self parameter is one of the most important concepts in
Python classes and objects.

When we create multiple objects from the same class, each object
needs to work with its own data.

The self parameter allows a method to know which object is
currently using that method.

In simple words:

self = the current object
"""

# Basic Example

class Car:
    car_name="Empty" 
    car_model=0
    car_color="Empty"
    def start_engine(self): # Method
        print("Engine is Started")

car1=Car()
car1.car_name="Civic"
car1.car_model=2026
car1.car_color="Black"

print(f"Car Name: {car1.car_name}")
print(f"Car Model: {car1.car_model}")
print(f"Car Color: {car1.car_color}")

car1.start_engine()


# ============================================================
# 2. WHY DOES self EXIST?
# ============================================================

"""
Suppose we create a class called Student.

We create two objects:

student_alpha
student_beta

Both objects can have different names.

When we call a method using student_alpha, Python needs to know
that the method should work with student_alpha's data.

Similarly, when we call the method using student_beta, Python
needs to know that it should work with student_beta's data.

The self parameter solves this problem.

It refers to the object that is currently calling the method.
"""


class Student:
    def show_name(self):
        print("Student object is using this method.")


student_alpha=Student()
student_beta=Student()

student_alpha.show_name()
student_beta.show_name()


# ============================================================
# 3. self REFERS TO THE CURRENT INSTANCE
# ============================================================

"""
The self parameter refers to the current instance of a class.

For example:

student_alpha.show_name()

Here, self refers to student_alpha.

When we write:

student_beta.show_name()

self refers to student_beta.

Therefore, the value of self depends on which object calls
the method.
"""


class Player:
    def identify(self):
        print("Current object:", self)


player_red=Player()
player_blue=Player()

player_red.identify()
player_blue.identify()


# ============================================================
# 4. self AND OBJECT DATA
# ============================================================

"""
The real power of self becomes clear when objects store data.

We can use self to create attributes that belong to the
current object.

For example:

self.name=name

This means that the value of name is stored inside the
current object.

If two different objects are created, each object can store
its own value.
"""


class Customer:
    def set_name(self,name):
        self.name=name

    def show_name(self):
        print("Customer Name:",self.name)


customer_one=Customer()
customer_two=Customer()

customer_one.set_name("Ayesha")
customer_two.set_name("Hassan")

customer_one.show_name()
customer_two.show_name()


# ============================================================
# 5. WHY EVERY INSTANCE METHOD NEEDS self
# ============================================================

"""
An instance method is a method that works with a particular
object.

Python automatically passes the current object to the method.

The first parameter of an instance method receives this object.

By convention, this parameter is named self.

For example:

class Student:
    def display(self):
        print("Hello")

When we write:

student.display()

Python internally passes the student object to display():

Student.display(student)

Therefore, self receives the current object.
"""


class Teacher:
    def introduce(self):
        print("This method belongs to:",self)


teacher_record=Teacher()

teacher_record.introduce()


# ============================================================
# 6. self IS PASSED AUTOMATICALLY
# ============================================================

"""
When we call an instance method using an object, Python
automatically passes that object as the first argument.

For example:

account.show_balance()

Python treats it approximately like:

Account.show_balance(account)

We normally do not pass self manually.

Python handles it automatically when the method is called
through an object.
"""


class Account:
    def display(self):
        print("Current account object:",self)


bank_account=Account()

bank_account.display()


# ============================================================
# 7. USING self TO ACCESS OBJECT ATTRIBUTES
# ============================================================

"""
The self parameter is commonly used to access attributes
belonging to the current object.

Syntax:

self.attribute_name

For example:

self.name
self.age
self.city

When an object accesses one of these attributes, self makes
sure that the correct object's data is used.
"""


class Person:
    def set_details(self,name,age):
        self.name=name
        self.age=age

    def show_details(self):
        print("Name:",self.name)
        print("Age:",self.age)


person_a=Person()
person_b=Person()

person_a.set_details("Bilal",21)
person_b.set_details("Zainab",24)

person_a.show_details()
person_b.show_details()


# ============================================================
# 8. self BINDING DIFFERENT OBJECTS
# ============================================================

"""
Let's look at an important example.

We create two objects from the same class:

product_a
product_b

Both objects have a price attribute.

When product_a.set_price() is called, self refers to product_a.

When product_b.set_price() is called, self refers to product_b.

Therefore, each object stores its own price.
"""


class Product:
    def set_price(self,price):
        self.price=price

    def display_price(self):
        print("Price:",self.price)


product_a=Product()
product_b=Product()

product_a.set_price(1500)
product_b.set_price(2800)

print("Product A:")
product_a.display_price()

print("Product B:")
product_b.display_price()


# ============================================================
# 9. WHAT HAPPENS IF WE FORGET self?
# ============================================================

"""
If we forget to include self as the first parameter of an
instance method, Python will still try to pass the current
object automatically.

This can cause an error because the method does not have a
parameter available to receive the object.

For example:

class Example:
    def display():
        print("Hello")

example=Example()
example.display()

Python passes example automatically, but display() does not
have a parameter to receive it.

This results in a TypeError.
"""


class IncorrectExample:
    def display():
        print("Hello")


incorrect_object=IncorrectExample()

# Uncomment the following line to see the error:
# incorrect_object.display()


# ============================================================
# 10. CORRECT USE OF self
# ============================================================

"""
The correct way to define an instance method is to include
self as its first parameter.

For example:

class Example:
    def display(self):
        print("Hello")

Now Python can pass the current object into self.
"""


class CorrectExample:
    def display(self):
        print("Hello from the object.")


correct_object=CorrectExample()

correct_object.display()


# ============================================================
# 11. self IS A NAME BY CONVENTION
# ============================================================

"""
self is not a special Python keyword.

It is simply the conventional name used for the first
parameter of an instance method.

Technically, another name can be used.

For example:

class Example:
    def display(current_object):
        print(current_object)

This code can work because Python passes the current object
to the first parameter.

However, we should always use the name self.

Using self is the standard Python convention and makes code
easy for other programmers to understand.
"""


class Demonstration:
    def display(current_object):
        print("Current object:",current_object)


demo_object=Demonstration()

demo_object.display()


# ============================================================
# 12. WHY WE SHOULD ALWAYS USE THE NAME self
# ============================================================

"""
Although another name can technically be used, we should
not change self in normal Python programming.

The name self is universally understood by Python programmers.

Compare:

def show(self):
    pass

with:

def show(current_object):
    pass

Both can work, but self is much clearer and follows the
standard Python convention.

Therefore:

Use self.

Do not replace it with another name in normal code.
"""


class StandardExample:
    def show(self):
        print("Using the standard self convention.")


standard_object=StandardExample()

standard_object.show()


# ============================================================
# 13. self WITH MULTIPLE ATTRIBUTES
# ============================================================

"""
An object can have multiple attributes.

We use self to store each attribute inside the current object.

For example:

self.name
self.age
self.city

Each object can have different values for these attributes.
"""


class Resident:
    def set_information(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city

    def display_information(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)


resident_one=Resident()
resident_two=Resident()

resident_one.set_information("Hamza",25,"Lahore")
resident_two.set_information("Mariam",22,"Islamabad")

print("Resident One:")
resident_one.display_information()

print()

print("Resident Two:")
resident_two.display_information()


# ============================================================
# 14. self WITH TWO DIFFERENT OBJECTS
# ============================================================

"""
This example clearly demonstrates how self connects a method
with the object that calls it.

When:

laptop_one.show_details()

is executed:

self=laptop_one

When:

laptop_two.show_details()

is executed:

self=laptop_two

Therefore, the same method can work with different objects
and their individual data.
"""


class Laptop:
    def set_model(self,model):
        self.model=model

    def show_model(self):
        print("Model:",self.model)


laptop_one=Laptop()
laptop_two=Laptop()

laptop_one.set_model("ThinkPad")
laptop_two.set_model("MacBook")

print("Laptop One:")
laptop_one.show_model()

print("Laptop Two:")
laptop_two.show_model()


# ============================================================
# 15. self AND METHOD CALLING
# ============================================================

"""
self can also be used to call another method of the same
object.

For example:

self.start()

means that the start() method of the current object should
be called.

This allows methods inside a class to work together.
"""


class Machine:
    def start(self):
        print("Machine started.")

    def operate(self):
        print("Preparing machine...")
        self.start()


factory_machine=Machine()

factory_machine.operate()


# ============================================================
# 16. self IS DIFFERENT FOR EACH OBJECT
# ============================================================

"""
When multiple objects are created from the same class, each
object gets its own self when a method is called.

For example:

first_device.show()
second_device.show()

During the first call:

self=first_device

During the second call:

self=second_device

This is why one class can manage data belonging to many
different objects.
"""


class Device:
    def set_name(self,name):
        self.name=name

    def show_name(self):
        print("Device:",self.name)


first_device=Device()
second_device=Device()

first_device.set_name("Printer")
second_device.set_name("Scanner")

first_device.show_name()
second_device.show_name()


# ============================================================
# 17. COMPLETE self EXAMPLE
# ============================================================

"""
Let's combine everything we have learned.

We will create a class called Book.

Each Book object will store its own:

- title
- author

The self parameter ensures that the correct object's data
is accessed.
"""


class Book:
    def set_information(self,title,author):
        self.title=title
        self.author=author

    def display_information(self):
        print("Title:",self.title)
        print("Author:",self.author)


novel_book=Book()
reference_book=Book()

novel_book.set_information("The Silent River","Daniel Stone")
reference_book.set_information("Python Fundamentals","Emma Clark")

print("Novel Book:")
novel_book.display_information()

print()

print("Reference Book:")
reference_book.display_information()


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. self refers to the current instance of a class.
2. self allows an instance method to access the current object.
3. The first parameter of an instance method is conventionally
   named self.
4. Python automatically passes the current object to self.
5. We normally do not pass self manually when calling a method.
6. self can be used to access object attributes:

   self.name
   self.age
   self.price

7. self allows different objects to store and access their own
   separate data.
8. If self is forgotten from an instance method, calling that
   method through an object can result in a TypeError.
9. self is not a Python keyword.
10. Another name can technically be used instead of self.
11. However, self is the standard Python convention and should
    always be used.
12. self can also be used to call another method of the same
    object.
13. The value of self changes depending on which object calls
    the method.

The main idea to remember is:

self = the current object

This allows the same class and methods to work with many
different objects while keeping each object's data separate.

In the next chapter, we will learn about constructors and
the __init__() method.
"""