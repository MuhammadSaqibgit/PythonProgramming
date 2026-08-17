"""
PROPERTIES AND GETTERS & SETTERS
"""


# ============================================================
# 1. INTRODUCTION TO PROPERTIES
# ============================================================

"""
In Python, we can access an object's attributes directly.

For example:

person.name

This is simple and convenient.

However, direct access can sometimes be risky.

For example, if an object's age should never be negative,
directly assigning a value can allow invalid data:

person.age=-10

Python will not automatically stop us.

Properties allow us to control how an attribute is accessed
and modified.

Using properties, we can add validation or other logic while
still using simple attribute syntax.
"""


# ============================================================
# 2. WHY DIRECT ATTRIBUTE ACCESS CAN BE RISKY
# ============================================================

"""
Consider a BankAccount class.

Suppose the balance should never be negative.

If we allow direct access:

account.balance=-5000

there is nothing stopping the user from assigning an invalid
value.

This can make an object's data inconsistent.

A better approach is to control how the value is changed.
"""


class BankAccount:

    def __init__(self,balance):
        self.balance=balance


account=BankAccount(5000)

account.balance=-3000

print("Balance:",account.balance)


# ============================================================
# 3. TRADITIONAL GETTER AND SETTER METHODS
# ============================================================

"""
In languages such as Java and C++, it is common to use
getter and setter methods to control access to attributes.

For example:

get_balance()
    Used to read the balance.

set_balance()
    Used to change the balance.

Python can also use this approach, although Python provides
a cleaner way using the @property decorator.
"""


class Account:

    def __init__(self,balance):
        self._balance=balance

    def get_balance(self):
        return self._balance

    def set_balance(self,new_balance):
        if(new_balance>=0):
            self._balance=new_balance
        else:
            print("Balance cannot be negative.")


bank_account=Account(5000)

print("Balance:",bank_account.get_balance())

bank_account.set_balance(7000)

print("Updated Balance:",bank_account.get_balance())

bank_account.set_balance(-1000)


# ============================================================
# 4. PROBLEM WITH TRADITIONAL GETTERS AND SETTERS
# ============================================================

"""
Traditional getter and setter methods work, but they require
method calls.

For example:

account.get_balance()

account.set_balance(5000)

Python provides a more natural approach using properties.

With a property, we can write:

account.balance

and:

account.balance=5000

while still having control over how the value is accessed
and changed.
"""


# ============================================================
# 5. THE @property DECORATOR
# ============================================================

"""
The @property decorator allows a method to be accessed like
an attribute.

Basic syntax:

@property
def property_name(self):
    return self._property_name

The method becomes a property.

We can then access it without parentheses.
"""


class Person:

    def __init__(self,name):
        self._name=name

    @property
    def name(self):
        return self._name


person_object=Person("Ayesha")

print("Name:",person_object.name)


# ============================================================
# 6. PROPERTY WORKS LIKE AN ATTRIBUTE
# ============================================================

"""
Notice the difference.

Without a property:

object.method()

With a property:

object.property

We do not use parentheses when accessing a property.

For example:

person_object.name

Python internally calls the method decorated with @property.
"""


class Student:

    def __init__(self,name):
        self._name=name

    @property
    def name(self):
        return self._name


student_record=Student("Hassan")

print(student_record.name)


# ============================================================
# 7. WHY USE AN UNDERSCORE WITH THE INTERNAL VARIABLE?
# ============================================================

"""
A common convention is to store the actual value in an
attribute beginning with an underscore.

For example:

self._name

and expose it through:

@property
def name(self):

The underscore indicates that _name is intended to be used
internally by the class.

It also prevents a naming conflict.

For example, if the property is named name, we should not
store the value in self.name inside the property getter.

Instead, we use:

self._name
"""


# ============================================================
# 8. CREATING A GETTER WITH @property
# ============================================================

"""
A method decorated with @property is commonly called a getter.

Its job is to return the value.

Example:

@property
def price(self):
    return self._price

Then we can write:

product.price

instead of:

product.get_price()
"""


class Product:

    def __init__(self,price):
        self._price=price

    @property
    def price(self):
        return self._price


product_item=Product(2500)

print("Price:",product_item.price)


# ============================================================
# 9. CREATING A SETTER
# ============================================================

"""
A getter allows us to read a property.

But what if we also want to control how the property is
changed?

We can create a setter using:

@property_name.setter

For example:

@property
def price(self):
    return self._price

@price.setter
def price(self,new_price):
    self._price=new_price

Now we can write:

product.price=3000

Python will automatically call the setter.
"""


class Product:

    def __init__(self,price):
        self._price=price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        self._price=new_price


product_item=Product(2500)

print("Original Price:",product_item.price)

product_item.price=3000

print("Updated Price:",product_item.price)


# ============================================================
# 10. ADDING VALIDATION INSIDE A SETTER
# ============================================================

"""
One of the biggest advantages of a setter is that we can
perform validation before changing the value.

For example, a product price should not be negative.

We can check the value inside the setter.
"""


class Product:

    def __init__(self,price):
        self._price=price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        if(new_price>=0):
            self._price=new_price
        else:
            print("Price cannot be negative.")


product_item=Product(2000)

print("Price:",product_item.price)

product_item.price=3500

print("Updated Price:",product_item.price)

product_item.price=-500

print("Final Price:",product_item.price)


# ============================================================
# 11. PROPERTY VALIDATION WITH AN ERROR
# ============================================================

"""
Instead of simply printing a message, we can raise an error
when invalid data is provided.

This is useful when invalid data should not be silently
ignored.
"""


class Student:

    def __init__(self,marks):
        self._marks=marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self,new_marks):
        if(0<=new_marks<=100):
            self._marks=new_marks
        else:
            raise ValueError("Marks must be between 0 and 100.")


student_record=Student(85)

print("Marks:",student_record.marks)

student_record.marks=95

print("Updated Marks:",student_record.marks)


# Uncomment the following line to see the validation error.

# student_record.marks=120


# ============================================================
# 12. PROPERTY VALIDATION IN __init__()
# ============================================================

"""
An important point is that the setter can also be used during
object creation.

If we assign the property inside __init__():

self.marks=marks

Python will use the setter.

This means the same validation can be applied when the object
is created and when the value is changed later.
"""


class ExamResult:

    def __init__(self,marks):
        self.marks=marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self,new_marks):
        if(0<=new_marks<=100):
            self._marks=new_marks
        else:
            raise ValueError("Marks must be between 0 and 100.")


result_record=ExamResult(80)

print("Marks:",result_record.marks)

result_record.marks=90

print("Updated Marks:",result_record.marks)


# ============================================================
# 13. READ-ONLY PROPERTIES
# ============================================================

"""
A property can be made read-only by creating only a getter
and not creating a setter.

For example:

@property
def full_name(self):
    return self._full_name

There is no:

@full_name.setter

Therefore, we can read:

person.full_name

but we cannot assign:

person.full_name="New Name"

This is called a read-only property.
"""


class Person:

    def __init__(self,first_name,last_name):
        self._first_name=first_name
        self._last_name=last_name

    @property
    def full_name(self):
        return self._first_name+" "+self._last_name


person_object=Person("Ali","Khan")

print("Full Name:",person_object.full_name)


# ============================================================
# 14. WHY full_name CAN BE READ BUT NOT CHANGED
# ============================================================

"""
The full_name property only has a getter.

There is no setter.

Therefore:

person_object.full_name

is allowed.

But:

person_object.full_name="New Name"

is not allowed.

This is useful when a value should be calculated from other
data and should not be directly changed.
"""


class Rectangle:

    def __init__(self,length,width):
        self._length=length
        self._width=width

    @property
    def area(self):
        return self._length*self._width


room=Rectangle(10,5)

print("Area:",room.area)


# ============================================================
# 15. CALCULATED READ-ONLY PROPERTY
# ============================================================

"""
A property does not have to store a separate value.

It can calculate a value whenever it is accessed.

For example, the area of a rectangle can be calculated from
length and width.

The area does not need to be stored separately.

We can create it as a read-only property.
"""


class Box:

    def __init__(self,length,width,height):
        self._length=length
        self._width=width
        self._height=height

    @property
    def volume(self):
        return self._length*self._width*self._height


storage_box=Box(4,5,6)

print("Volume:",storage_box.volume)


# ============================================================
# 16. PROPERTY WITH BOTH GETTER AND SETTER
# ============================================================

"""
A property can have both:

1. Getter
2. Setter

Getter:
    Reads the value.

Setter:
    Changes the value and can perform validation.
"""


class Employee:

    def __init__(self,salary):
        self.salary=salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,new_salary):
        if(new_salary>=0):
            self._salary=new_salary
        else:
            raise ValueError("Salary cannot be negative.")


employee_record=Employee(50000)

print("Salary:",employee_record.salary)

employee_record.salary=60000

print("Updated Salary:",employee_record.salary)


# ============================================================
# 17. PROPERTY WITH MORE COMPLEX VALIDATION
# ============================================================

"""
A setter can contain multiple validation rules.

For example, a username might need:

- At least 5 characters.
- No spaces.

The setter can check these conditions before accepting
the new value.
"""


class User:

    def __init__(self,username):
        self.username=username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self,new_username):
        if(len(new_username)<5):
            raise ValueError(
                "Username must contain at least 5 characters."
            )

        if(" " in new_username):
            raise ValueError(
                "Username cannot contain spaces."
            )

        self._username=new_username


user_account=User("hassan123")

print("Username:",user_account.username)

user_account.username="bilal456"

print("Updated Username:",user_account.username)


# ============================================================
# 18. PROPERTY VS TRADITIONAL GETTER AND SETTER
# ============================================================

"""
Traditional getter and setter approach:

class Product:

    def get_price(self):
        return self._price

    def set_price(self,price):
        self._price=price

Usage:

product.get_price()
product.set_price(3000)

Python property approach:

@property
def price(self):
    return self._price

@price.setter
def price(self,new_price):
    self._price=new_price

Usage:

product.price
product.price=3000

The property approach provides a cleaner interface while
still allowing the class to control access to the data.
"""


# ============================================================
# 19. PROPERTY CAN HIDE IMPLEMENTATION DETAILS
# ============================================================

"""
A property allows us to change how data is stored internally
without changing how users interact with the object.

For example, users can simply write:

product.price

They do not need to know that the actual value is stored in:

self._price

This helps keep the interface of the class simple.
"""


class Product:

    def __init__(self,price):
        self._price=price

    @property
    def price(self):
        return self._price


computer_product=Product(75000)

print("Price:",computer_product.price)


# ============================================================
# 20. COMPLETE PRACTICAL EXAMPLE
# ============================================================

"""
Let's create a BankAccount class.

The account will have:

    owner
    balance

The balance should:

- Be readable.
- Not be allowed to become negative.
- Be changeable only through valid values.

We can use a property to control access to balance.
"""


class BankAccount:

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,new_balance):
        if(new_balance<0):
            raise ValueError("Balance cannot be negative.")

        self._balance=new_balance

    def show_account(self):
        print("Owner:",self.owner)
        print("Balance:",self.balance)


account_record=BankAccount("Mariam",10000)

account_record.show_account()

account_record.balance=15000

print("Updated Balance:",account_record.balance)


# ============================================================
# 21. COMPLETE READ-ONLY PROPERTY EXAMPLE
# ============================================================

"""
Let's create a Person class with a read-only property.

The full name is calculated from first_name and last_name.

There is no reason to store a separate full_name value.

The full_name property calculates it whenever we access it.
"""


class Person:

    def __init__(self,first_name,last_name):
        self._first_name=first_name
        self._last_name=last_name

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"


person_record=Person("Hassan","Ahmed")

print("First Name:",person_record._first_name)
print("Last Name:",person_record._last_name)
print("Full Name:",person_record.full_name)


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. Direct attribute access is simple but can allow invalid
   data to enter an object.

2. Traditional getter and setter methods are commonly used
   in languages such as Java and C++.

3. A getter is used to read a value.

4. A setter is used to change a value.

5. Python provides the @property decorator as a cleaner
   way to implement getters and setters.

6. A getter is created using:

   @property
   def value(self):
       return self._value

7. A setter is created using:

   @value.setter
   def value(self,new_value):
       self._value=new_value

8. A property is accessed like an attribute:

   object.value

   We do not use parentheses.

9. A setter can contain validation logic.

10. Validation inside a setter helps prevent invalid data
    from being assigned to an object.

11. A property can be read-only if it has a getter but
    no setter.

12. Read-only properties are useful for calculated values
    or values that should not be directly changed.

13. The underscore in names such as:

    self._price

    is a common convention for an internal attribute.

14. Properties allow us to keep a simple interface while
    controlling what happens when data is read or changed.

A simple way to remember:

@property
    Controls reading.

@property_name.setter
    Controls changing.

Getter:
    object.value

Setter:
    object.value=new_value

Read-only property:
    Getter exists.
    Setter does not exist.

In the next chapter, we will learn about access modifiers
and how Python handles public, protected, and private members.
"""