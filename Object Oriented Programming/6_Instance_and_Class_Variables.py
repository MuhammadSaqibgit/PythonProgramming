"""
INSTANCE AND CLASS VARIABLES
"""


# ============================================================
# 1. INTRODUCTION TO INSTANCE AND CLASS VARIABLES
# ============================================================

"""
Variables are used to store data in Python classes.

When working with classes, variables can mainly be divided
into two types:

1. Instance variables
2. Class variables

Instance variables belong to individual objects.

Class variables belong to the class and are shared by objects.

Understanding the difference between these two types of
variables is important when designing classes.
"""


# ============================================================
# 2. INSTANCE VARIABLES
# ============================================================

"""
An instance variable is a variable that belongs to a specific
object.

Instance variables are usually created using self inside
a class method.

Syntax:

self.variable=value

Each object gets its own copy of an instance variable.

For example, every Student object can have its own name.
"""


class Student:
    def __init__(self,name):
        self.name=name


student_one=Student("Ayesha")
student_two=Student("Bilal")

print("Student One:",student_one.name)
print("Student Two:",student_two.name)


# ============================================================
# 3. EACH OBJECT HAS ITS OWN INSTANCE VARIABLES
# ============================================================

"""
Instance variables belong to individual objects.

If we create two objects from the same class, each object
can have different values for its instance variables.

Changing the instance variable of one object does not change
the instance variable of another object.
"""


class Employee:
    def __init__(self,name,department):
        self.name=name
        self.department=department


employee_alpha=Employee("Hassan","IT")
employee_beta=Employee("Mariam","HR")

print("Employee Alpha:")
print("Name:",employee_alpha.name)
print("Department:",employee_alpha.department)

print()

print("Employee Beta:")
print("Name:",employee_beta.name)
print("Department:",employee_beta.department)


# ============================================================
# 4. MODIFYING INSTANCE VARIABLES
# ============================================================

"""
Because instance variables belong to individual objects,
we can modify them separately.

Changing an instance variable through one object does not
change the same variable in another object.
"""


class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price


product_one=Product("Keyboard",2500)
product_two=Product("Mouse",1800)

product_one.price=3000

print("Product One Price:",product_one.price)
print("Product Two Price:",product_two.price)


# ============================================================
# 5. CLASS VARIABLES
# ============================================================

"""
A class variable is a variable that is defined directly
inside the class body.

Unlike an instance variable, a class variable is associated
with the class itself.

Syntax:

class ClassName:
    variable=value

Class variables are generally shared by all objects of
that class.
"""


class Employee:
    company="Tech Solutions" # Class Variable


employee_one=Employee()
employee_two=Employee()

print("Employee One Company:",employee_one.company)
print("Employee Two Company:",employee_two.company)


# ============================================================
# 6. INSTANCE VARIABLES VS CLASS VARIABLES
# ============================================================

"""
The main difference is:

Instance Variable:
    - Defined using self.variable.
    - Belongs to a specific object.
    - Each object can have a different value.

Class Variable:
    - Defined directly inside the class.
    - Belongs to the class.
    - Normally shared by all objects.

For example:

class Student:
    school="City School"

    def __init__(self,name):
        self.name=name

Here:

school
    is a class variable.

self.name
    is an instance variable.
"""


class Student:
    school="City School"

    def __init__(self,name):
        self.name=name


student_alpha=Student("Zain")
student_beta=Student("Noor")

print("Student Alpha:",student_alpha.name)
print("Student Beta:",student_beta.name)

print("School:",student_alpha.school)
print("School:",student_beta.school)


# ============================================================
# 7. ACCESSING INSTANCE VARIABLES
# ============================================================

"""
Instance variables are normally accessed through an object.

Syntax:

object.variable

For example:

student.name

The value belongs to that particular student object.
"""


class Customer:
    def __init__(self,name,city):
        self.name=name
        self.city=city


customer_a=Customer("Hamza","Lahore")
customer_b=Customer("Sara","Karachi")

print("Customer A Name:",customer_a.name)
print("Customer A City:",customer_a.city)

print("Customer B Name:",customer_b.name)
print("Customer B City:",customer_b.city)


# ============================================================
# 8. ACCESSING CLASS VARIABLES
# ============================================================

"""
Class variables can be accessed through the class itself.

Syntax:

ClassName.variable

They can also normally be accessed through an object.

For example:

School.name

or:

student.school

When accessed through an object, Python can look for the
variable in the class if it is not found in the object.
"""


class School:
    name="Bright Future School"


first_student=School()
second_student=School()

print("Using class:",School.name)
print("Using first object:",first_student.name)
print("Using second object:",second_student.name)


# ============================================================
# 9. INSTANCE AND CLASS VARIABLES TOGETHER
# ============================================================

"""
A class can contain both instance variables and class variables.

For example, a Student class can have:

Class variable:
    school

Instance variables:
    name
    age

The school can be common for all students, while each student
can have a different name and age.
"""


class Student:
    school="Modern Public School"

    def __init__(self,name,age):
        self.name=name
        self.age=age


student_first=Student("Ali",19)
student_second=Student("Mina",21)

print("Student First:")
print("Name:",student_first.name)
print("Age:",student_first.age)
print("School:",student_first.school)

print()

print("Student Second:")
print("Name:",student_second.name)
print("Age:",student_second.age)
print("School:",student_second.school)


# ============================================================
# 10. SHARED CLASS VARIABLE
# ============================================================

"""
Class variables are useful when a value should be common
among all objects.

For example, suppose every employee works for the same company.

Instead of storing the company name separately in every object,
we can define it once as a class variable.
"""


class Worker:
    company="Global Technologies"

    def __init__(self,name):
        self.name=name


worker_one=Worker("Usman")
worker_two=Worker("Hira")
worker_three=Worker("Danish")

print(worker_one.name,"-",worker_one.company)
print(worker_two.name,"-",worker_two.company)
print(worker_three.name,"-",worker_three.company)


# ============================================================
# 11. MODIFYING A CLASS VARIABLE THROUGH THE CLASS
# ============================================================

"""
A class variable can be modified through the class itself.

When we change the class variable using the class name,
the change is normally visible to all objects that are
using the class variable.
"""


class Company:
    name="Alpha Technologies"


company_employee_one=Company()
company_employee_two=Company()

print("Before change:")
print(company_employee_one.name)
print(company_employee_two.name)

Company.name="Beta Technologies"

print()
print("After change:")
print(company_employee_one.name)
print(company_employee_two.name)


# ============================================================
# 12. MODIFYING A CLASS VARIABLE THROUGH AN OBJECT
# ============================================================

"""
There is an important behavior to understand here.

Suppose we write:

employee.company="New Company"

If company is originally a class variable, this assignment
does NOT change the class variable.

Instead, Python creates an instance variable named company
for that particular object.

This is an important pitfall when working with class variables.
"""


class Organization:
    name="Original Organization"


organization_one=Organization()
organization_two=Organization()

organization_one.name="Special Organization"

print("Organization One:",organization_one.name)
print("Organization Two:",organization_two.name)
print("Class Variable:",Organization.name)


# ============================================================
# 13. UNDERSTANDING THE CLASS VARIABLE PITFALL
# ============================================================

"""
Let's examine what happened in the previous example.

Originally:

Organization.name="Original Organization"

Both objects use this class variable.

Then we write:

organization_one.name="Special Organization"

Python creates a new instance variable called name inside
organization_one.

It does not modify:

Organization.name

Therefore:

organization_one.name -> "Special Organization"

organization_two.name -> "Original Organization"

Organization.name -> "Original Organization"
"""


class Library:
    city="Lahore"


library_one=Library()
library_two=Library()

library_one.city="Islamabad"

print("Library One City:",library_one.city)
print("Library Two City:",library_two.city)
print("Class City:",Library.city)


# ============================================================
# 14. HOW PYTHON LOOKS FOR A VARIABLE
# ============================================================

"""
When we access a variable through an object, Python first
looks for that variable in the object.

If it is not found there, Python can look for the variable
in the class.

For example:

object.value

Python first checks:

1. Does the object have value?

If not, it can look for:

2. Does the class have value?

This explains why an object can access a class variable.
"""


class Device:
    category="Electronic"


printer_device=Device()

print("Category:",printer_device.category)


# ============================================================
# 15. OBJECT VARIABLE HIDES THE CLASS VARIABLE
# ============================================================

"""
If an object has an instance variable with the same name
as a class variable, the object's instance variable takes
priority when accessed through that object.

The class variable still exists in the class.

For example:

class Product:
    category="General"

product.category="Computer"

Now:

product.category -> "Computer"

Product.category -> "General"
"""


class Product:
    category="General"


computer_product=Product()

computer_product.category="Computer"

print("Object Category:",computer_product.category)
print("Class Category:",Product.category)


# ============================================================
# 16. MODIFYING THE CLASS VARIABLE CORRECTLY
# ============================================================

"""
If we want to modify the actual class variable, we should
modify it through the class name.

Syntax:

ClassName.variable=new_value

This changes the value stored at the class level.
"""


class School:
    location="Lahore"


student_record_one=School()
student_record_two=School()

School.location="Islamabad"

print("Student Record One School:",student_record_one.location)
print("Student Record Two School:",student_record_two.location)
print("Class Location:",School.location)


# ============================================================
# 17. WHEN TO USE INSTANCE VARIABLES
# ============================================================

"""
Use instance variables when the value can be different
for each object.

Common examples include:

- Name
- Age
- Email
- Salary
- Price
- Address
- Model

For example, each bank account can have a different owner
and balance.

Therefore, owner and balance should be instance variables.
"""


class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance


account_alpha=BankAccount("Farhan",5000)
account_beta=BankAccount("Sadia",9000)

print(account_alpha.owner,account_alpha.balance)
print(account_beta.owner,account_beta.balance)


# ============================================================
# 18. WHEN TO USE CLASS VARIABLES
# ============================================================

"""
Use class variables when a value should normally be common
to all objects of the class.

Common examples include:

- Company name
- School name
- Tax rate
- Number of wheels for a particular vehicle type
- A shared configuration value

For example, if all employees belong to the same company,
the company name can be a class variable.
"""


class Employee:
    company="NextGen Software"

    def __init__(self,name):
        self.name=name


developer_one=Employee("Adeel")
developer_two=Employee("Kiran")

print(developer_one.name,"-",developer_one.company)
print(developer_two.name,"-",developer_two.company)


# ============================================================
# 19. INSTANCE VARIABLE AND CLASS VARIABLE EXAMPLE
# ============================================================

"""
Let's combine both types of variables.

Each Book object will have its own:

- title
- author
- price

These are instance variables.

All books will have the same:

- library_name

This is a class variable.
"""


class Book:
    library_name="Central Library"

    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price


book_alpha=Book("Python Programming","James Wilson",2500)
book_beta=Book("Object Oriented Python","Laura Smith",3000)

print("Book Alpha:")
print("Title:",book_alpha.title)
print("Author:",book_alpha.author)
print("Price:",book_alpha.price)
print("Library:",book_alpha.library_name)

print()

print("Book Beta:")
print("Title:",book_beta.title)
print("Author:",book_beta.author)
print("Price:",book_beta.price)
print("Library:",book_beta.library_name)


# ============================================================
# 20. PRACTICAL EXAMPLE
# ============================================================

"""
Consider an online store.

Every product can have different:

- Name
- Price
- Stock quantity

These should be instance variables because they can be
different for every product.

The store name can be a class variable if all products
belong to the same store.
"""


class StoreProduct:
    store_name="Tech Market"

    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock

    def show_product(self):
        print("Store:",self.store_name)
        print("Product:",self.name)
        print("Price:",self.price)
        print("Stock:",self.stock)


product_alpha=StoreProduct("Monitor",35000,10)
product_beta=StoreProduct("Headphones",5000,25)

product_alpha.show_product()

print()

product_beta.show_product()


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. Variables in a class can mainly be instance variables or
   class variables.
2. Instance variables are normally defined using self.variable.
3. Each object gets its own instance variables.
4. Different objects can have different values for the same
   instance variable.
5. Class variables are defined directly inside the class body.
6. Class variables are associated with the class itself.
7. Class variables are normally shared by all objects.
8. Instance variables can be accessed through an object.
9. Class variables can be accessed through the class or an object.
10. If an object does not have an instance variable, Python can
    find the class variable.
11. Assigning a class variable through an object can create a
    new instance variable instead of changing the class variable.
12. This can cause unexpected behavior if the difference is not
    understood.
13. To modify the actual class variable, use:

    ClassName.variable = value

14. Use instance variables when data is specific to each object.
15. Use class variables when data is intended to be common
    among objects.

Simple rule:

Instance Variable:
    Different for different objects.

Class Variable:
    Common to the class and normally shared by objects.

In the next chapter, we will learn about methods and how
objects can perform actions using methods defined inside
a class.
"""