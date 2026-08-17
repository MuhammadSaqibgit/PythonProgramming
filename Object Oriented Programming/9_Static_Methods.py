"""
STATIC METHODS
"""


# ============================================================
# 1. INTRODUCTION TO STATIC METHODS
# ============================================================

"""
A static method is a method defined inside a class that does
not need access to the object or the class itself.

A static method does not use:

    self

or:

    cls

It is created using the @staticmethod decorator.

Static methods are useful when we have a function that is
related to a class but does not need to access or modify
instance variables or class variables.
"""


# ============================================================
# 2. WHAT IS A STATIC METHOD?
# ============================================================

"""
A static method is defined inside a class using:

@staticmethod

Basic syntax:

class ClassName:

    @staticmethod
    def method_name():
        # code

Unlike an instance method, a static method does not receive
self automatically.

Unlike a class method, a static method does not receive
cls automatically.
"""


class Calculator:

    @staticmethod
    def add_numbers(first_number,second_number):
        return first_number+second_number


result=Calculator.add_numbers(10,20)

print("Result:",result)


# ============================================================
# 3. @staticmethod DECORATOR
# ============================================================

"""
The @staticmethod decorator tells Python that the method
should behave as a static method.

The method does not receive the current object or the
current class automatically.

We can call a static method using the class name.
"""


class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius*9/5)+32


temperature=Temperature.celsius_to_fahrenheit(25)

print("Fahrenheit:",temperature)


# ============================================================
# 4. STATIC METHOD DOES NOT USE self
# ============================================================

"""
An instance method uses self because it works with a
particular object.

A static method does not need self because it does not
need to access the object's data.

For example, checking whether a number is even does not
require any object information.
"""


class NumberChecker:

    @staticmethod
    def is_even(number):
        return number%2==0


print(NumberChecker.is_even(12))
print(NumberChecker.is_even(17))


# ============================================================
# 5. STATIC METHOD DOES NOT USE cls
# ============================================================

"""
A class method uses cls because it works with the class.

A static method does not need cls because it does not
need to access the class or its class variables.

For example, a method that calculates the square of a
number does not need information from the class.
"""


class MathTools:

    @staticmethod
    def square(value):
        return value*value


print("Square:", MathTools.square(8))


# ============================================================
# 6. INSTANCE METHOD, CLASS METHOD, AND STATIC METHOD
# ============================================================

"""
Python classes can contain different types of methods.

1. Instance method
2. Class method
3. Static method

Each type has a different purpose.

Instance method:
    Works with an object.
    Uses self.

Class method:
    Works with the class.
    Uses cls.

Static method:
    Does not need the object or the class.
    Uses neither self nor cls.
"""


class Example:

    class_name="Example Class"

    def __init__(self,value):
        self.value=value

    # Instance method
    def show_value(self):
        print("Value:",self.value)

    # Class method
    @classmethod
    def show_class_name(cls):
        print("Class Name:",cls.class_name)

    # Static method
    @staticmethod
    def multiply_numbers(first_value,second_value):
        return first_value*second_value


example_object=Example(50)

example_object.show_value()

Example.show_class_name()

result=Example.multiply_numbers(5,6)

print("Multiplication:",result)


# ============================================================
# 7. SUMMARY TABLE
# ============================================================

"""
The three method types can be summarized as:

--------------------------------------------------------------
Method Type       First Parameter       Works With
--------------------------------------------------------------
Instance Method   self                  Object
Class Method      cls                   Class
Static Method     None                  Neither
--------------------------------------------------------------

Instance method:
    def method(self):

Class method:
    @classmethod
    def method(cls):

Static method:
    @staticmethod
    def method():

The main question to ask is:

Does the method need object data?

    Yes -> Instance method

Does the method need class data?

    Yes -> Class method

Does the method need neither?

    Yes -> Static method
"""


# ============================================================
# 8. STATIC METHOD AS A UTILITY FUNCTION
# ============================================================

"""
A static method is often used as a utility or helper function.

A utility function performs a specific task that is related
to the class but does not need access to the object or class.

For example, a BankAccount class may need to validate whether
an amount is positive.

The validation does not require any particular bank account.
"""


class BankAccount:

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    @staticmethod
    def is_valid_amount(amount):
        return amount>0


print(BankAccount.is_valid_amount(500))
print(BankAccount.is_valid_amount(-100))


# ============================================================
# 9. STATIC METHOD FOR VALIDATION
# ============================================================

"""
Validation is a common use case for static methods.

For example, suppose a registration system needs to check
whether a username is long enough.

The validation only needs the username.

It does not need:

    self

or:

    cls
"""


class UserRegistration:

    @staticmethod
    def is_valid_username(username):
        return len(username)>=5


print(UserRegistration.is_valid_username("Hassan"))
print(UserRegistration.is_valid_username("Ali"))


# ============================================================
# 10. STATIC METHOD FOR CALCULATION
# ============================================================

"""
Static methods can also be useful for calculations.

For example, an Order class may need a helper that calculates
a discount.

The calculation only needs the price and discount percentage.
It does not need information about a particular Order object.
"""


class Order:

    @staticmethod
    def calculate_discount(price,percentage):
        discount=price*percentage/100
        return discount


discount_amount=Order.calculate_discount(5000,10)

print("Discount:",discount_amount)


# ============================================================
# 11. STATIC METHOD WITH MULTIPLE ARGUMENTS
# ============================================================

"""
A static method can accept as many normal parameters as
needed.

The important point is that Python does not automatically
pass self or cls.

For example:

@staticmethod
def calculate_total(price,quantity,tax):
    ...

All three values are normal arguments.
"""


class Invoice:

    @staticmethod
    def calculate_total(price,quantity,tax_rate):
        subtotal=price*quantity
        tax=subtotal*tax_rate/100

        return subtotal+tax


total_amount=Invoice.calculate_total(2000,3,5)

print("Total Amount:",total_amount)


# ============================================================
# 12. STATIC METHOD WITH AN INSTANCE METHOD
# ============================================================

"""
A class can contain both instance methods and static methods.

The instance method can work with object data.

The static method can perform a helper operation that does
not need object data.
"""


class Rectangle:

    def __init__(self,length,width):
        self.length=length
        self.width=width

    def calculate_area(self):
        return self.length*self.width

    @staticmethod
    def is_valid_dimension(value):
        return value>0


room=Rectangle(10,6)

print("Area:",room.calculate_area())

print("Valid Length:",Rectangle.is_valid_dimension(10))
print("Valid Length:",Rectangle.is_valid_dimension(-5))


# ============================================================
# 13. STATIC METHOD AND CLASS METHOD TOGETHER
# ============================================================

"""
A class can also contain instance methods, class methods,
and static methods at the same time.

Each method can have a different responsibility.
"""


class Employee:

    company="Tech Solutions"

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    # Instance method
    def show_employee(self):
        print("Name:",self.name)
        print("Salary:",self.salary)

    # Class method
    @classmethod
    def show_company(cls):
        print("Company:",cls.company)

    # Static method
    @staticmethod
    def is_valid_salary(salary):
        return salary>0


employee_record=Employee("Mariam",75000)

employee_record.show_employee()

Employee.show_company()

print(Employee.is_valid_salary(75000))
print(Employee.is_valid_salary(-5000))


# ============================================================
# 14. CALLING A STATIC METHOD USING THE CLASS
# ============================================================

"""
The most common way to call a static method is through the
class name.

Syntax:

ClassName.static_method()

For example:

Calculator.add(10,20)
"""


class Calculator:

    @staticmethod
    def subtract(first_number,second_number):
        return first_number-second_number


answer=Calculator.subtract(50,15)

print("Answer:",answer)


# ============================================================
# 15. CALLING A STATIC METHOD USING AN OBJECT
# ============================================================

"""
A static method can also be accessed through an object.

However, the object is NOT automatically passed to the
static method.

This is an important difference between a static method
and an instance method.
"""


class Converter:

    @staticmethod
    def kilometers_to_miles(kilometers):
        return kilometers*0.621371


converter_object=Converter()

distance=converter_object.kilometers_to_miles(10)

print("Miles:",distance)


# ============================================================
# 16. STATIC METHOD DOES NOT HAVE ACCESS TO self
# ============================================================

"""
A static method does not automatically receive self.

Therefore, it cannot directly access instance variables
through self.

For example, this would not work:

@staticmethod
def show_name():
    print(self.name)

There is no automatically provided self in a static method.

If a value is required, it should be passed as a normal
argument.
"""


class Person:

    def __init__(self,name):
        self.name=name

    @staticmethod
    def display_name(name):
        print("Name:",name)


person_object=Person("Ayesha")

Person.display_name(person_object.name)


# ============================================================
# 17. STATIC METHOD DOES NOT NEED OBJECT DATA
# ============================================================

"""
A useful question to ask when deciding whether to use a
static method is:

"Does this method need information from a particular object?"

If the answer is no, a static method may be appropriate.

For example, checking whether a year is a leap year does
not require a particular object.
"""


class CalendarTools:

    @staticmethod
    def is_leap_year(year):
        if(year%400==0):
            return True

        if(year%100==0):
            return False

        return year%4==0


print("2024:",CalendarTools.is_leap_year(2024))
print("2025:",CalendarTools.is_leap_year(2025))


# ============================================================
# 18. STATIC METHOD FOR STRING VALIDATION
# ============================================================

"""
Static methods can be useful for validating strings.

For example, an email validation helper can receive an
email address and check whether it contains certain characters.

The method does not need information from a particular
Email object.
"""


class EmailTools:

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email


print(EmailTools.is_valid_email("user@example.com"))
print(EmailTools.is_valid_email("invalid-email"))


# ============================================================
# 19. STATIC METHOD FOR DATA CONVERSION
# ============================================================

"""
Static methods can also be used for data conversion.

For example, a distance-related class can provide a helper
for converting meters into kilometers.
"""


class DistanceTools:

    @staticmethod
    def meters_to_kilometers(meters):
        return meters/1000


distance_in_km=DistanceTools.meters_to_kilometers(3500)

print("Distance:",distance_in_km,"km")


# ============================================================
# 20. PRACTICAL EXAMPLE
# ============================================================

"""
Let's create a Product class.

The Product object contains:

    name
    price
    quantity

The class will have:

Instance method:
    calculate_total()

Static method:
    is_valid_price()

The instance method needs the object's price and quantity.

The static method only needs a price value, so it does not
need self or cls.
"""


class Product:

    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def calculate_total(self):
        return self.price*self.quantity

    @staticmethod
    def is_valid_price(price):
        return price>=0


product_item=Product("Keyboard",2500,2)

print("Product:",product_item.name)
print("Total:",product_item.calculate_total())

print("Valid Price:",Product.is_valid_price(2500))
print("Valid Price:",Product.is_valid_price(-500))


# ============================================================
# 21. ANOTHER PRACTICAL EXAMPLE
# ============================================================

"""
Consider a Student class.

Each Student object has:

    name
    marks

We can use an instance method to calculate the student's
average.

We can use a static method to validate whether a mark is
within the valid range.

The validation does not need any particular student object.
"""


class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def calculate_average(self):
        return sum(self.marks)/len(self.marks)

    @staticmethod
    def is_valid_mark(mark):
        return 0<=mark<=100


student_record=Student("Noor",[80,75,90])

print("Student:",student_record.name)
print("Average:",student_record.calculate_average())

print("Valid Mark:",Student.is_valid_mark(85))
print("Valid Mark:",Student.is_valid_mark(120))


# ============================================================
# 22. WHEN SHOULD YOU USE A STATIC METHOD?
# ============================================================

"""
A static method is useful when:

1. The function is logically related to the class.
2. The function does not need instance data.
3. The function does not need class data.
4. The function does not need self.
5. The function does not need cls.
6. The function performs a calculation, validation, conversion,
   or another helper operation.

For example:

A Product class:
    is_valid_price()

A Calculator class:
    add_numbers()

A Temperature class:
    celsius_to_fahrenheit()

A Calendar class:
    is_leap_year()
"""


# ============================================================
# 23. WHEN NOT TO USE A STATIC METHOD
# ============================================================

"""
Do not use a static method simply because it is possible.

If a method needs instance variables, use an instance method.

If a method needs class variables or needs to create objects
using the class, a class method may be more appropriate.

For example:

def show_name(self):
    print(self.name)

This should be an instance method because it needs self.name.

Similarly:

@classmethod
def change_company(cls,name):
    cls.company=name

This should be a class method because it needs cls.company.
"""


# ============================================================
# 24. FINAL COMPARISON
# ============================================================

"""
Let's summarize all three method types.

--------------------------------------------------------------
Instance Method
--------------------------------------------------------------

Decorator:
    None

First parameter:
    self

Works with:
    Individual object

Can access:
    Instance variables
    Class variables

Typical use:
    Object behavior


--------------------------------------------------------------
Class Method
--------------------------------------------------------------

Decorator:
    @classmethod

First parameter:
    cls

Works with:
    Class

Can access:
    Class variables

Typical use:
    Alternative constructors
    Factory methods
    Class-level operations


--------------------------------------------------------------
Static Method
--------------------------------------------------------------

Decorator:
    @staticmethod

First parameter:
    None

Works with:
    Neither object nor class

Can access directly:
    Neither instance data nor class data

Typical use:
    Utility functions
    Validation
    Calculations
    Conversions
"""


# ============================================================
# 25. COMPLETE EXAMPLE
# ============================================================

"""
Let's put all three types of methods into one class.

We will create a Course class.

Instance method:
    show_course()

Class method:
    from_string()

Static method:
    is_valid_duration()

This demonstrates when each type of method can be useful.
"""


class Course:

    platform="Online Academy"

    def __init__(self,title,duration):
        self.title=title
        self.duration=duration

    # Instance method
    def show_course(self):
        print("Course:",self.title)
        print("Duration:",self.duration,"hours")
        print("Platform:",self.platform)

    # Class method
    @classmethod
    def from_string(cls,data):
        course_title,course_duration=data.split("|")

        return cls(
            course_title,
            int(course_duration)
        )

    # Static method
    @staticmethod
    def is_valid_duration(duration):
        return duration>0


course_information="Python OOP|20"

python_course=Course.from_string(course_information)

python_course.show_course()

print(
    "Valid Duration:",
    Course.is_valid_duration(python_course.duration)
)


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. A static method is a method that does not need the object
   or the class.

2. A static method is created using the @staticmethod decorator.

3. A static method does not automatically receive self.

4. A static method does not automatically receive cls.

5. Instance methods use self.

6. Class methods use cls.

7. Static methods use neither self nor cls.

8. Static methods are useful for utility or helper functions
   related to a class.

9. Common uses of static methods include:

   - Validation
   - Calculations
   - Data conversion
   - Helper operations

10. A static method can be called using the class:

    ClassName.method()

11. A static method can also be accessed through an object,
    but the object is not automatically passed to the method.

12. If a method needs instance data, use an instance method.

13. If a method needs class data, use a class method.

14. If a method needs neither instance data nor class data,
    a static method may be appropriate.

A simple way to remember:

Instance Method:
    self -> object

Class Method:
    cls -> class

Static Method:
    neither self nor cls

The main idea is to choose the type of method according to
what the method needs to work with.
"""
