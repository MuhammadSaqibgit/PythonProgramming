"""
CLASS METHODS
"""


# ============================================================
# 1. INTRODUCTION TO CLASS METHODS
# ============================================================

"""
A class method is a method that belongs to the class rather than
to a particular object.

Instance methods work with individual objects and use self.

Class methods work with the class itself and use cls.

A class method is created using the @classmethod decorator.

Basic syntax:

class ClassName:

    @classmethod
    def method_name(cls):
        pass

The cls parameter refers to the current class. Now self parameter
is not used because self is used to indicate instance (object)
"""


# ============================================================
# 2. INSTANCE METHOD VS CLASS METHOD
# ============================================================

"""
There are two important types of methods we have seen so far:

Instance method:
    - Works with an object.
    - Uses self as the first parameter.
    - Can access instance variables.

Class method:
    - Works with the class.
    - Uses cls as the first parameter.
    - Can access class variables.

Simple comparison:

self -> current object
cls  -> current class
"""


class Student:
    school="Bright Future School"

    def __init__(self,name):
        self.name=name

    def show_student(self):
        print("Student Name:",self.name)

    @classmethod
    def show_school(cls):
        print("School Name:",cls.school)


student_record=Student("Ayesha")

student_record.show_student()
student_record.show_school()


# ============================================================
# 3. @classmethod DECORATOR
# ============================================================

"""
The @classmethod decorator tells Python that the method should
be treated as a class method.

The decorator is written directly above the method.

Syntax:

@classmethod
def method_name(cls):
    pass

Python automatically passes the class to cls when the class
method is called.
"""


class Organization:
    organization_name="Global Technologies"

    @classmethod
    def display_name(cls):
        print("Organization:",cls.organization_name)


Organization.display_name()


# ============================================================
# 4. THE cls PARAMETER
# ============================================================

"""
The cls parameter refers to the current class.

It works with class methods in a similar way that self works
with instance methods.

For example:

class School:

    @classmethod
    def show_name(cls):
        print(cls.name)

Here:

cls
    refers to the School class.

self
    refers to a particular object.

The names self and cls are conventions used by Python
programmers.
"""


class School:
    name="Modern Public School"

    @classmethod
    def show_name(cls):
        print("School Name:",cls.name)


School.show_name()


# ============================================================
# 5. self VS cls
# ============================================================

"""
It is important to understand the difference between self
and cls.

self:
    Refers to the current object.

cls:
    Refers to the current class.

For example:

student.show_name()

self refers to student.

Student.show_school()

cls refers to Student.
"""


class Learner:
    school="City Academy"

    def __init__(self,name):
        self.name=name

    def show_name(self):
        print("Name:",self.name)

    @classmethod
    def show_school(cls):
        print("School:",cls.school)


learner_object=Learner("Hassan")

learner_object.show_name()
Learner.show_school()


# ============================================================
# 6. ACCESSING CLASS VARIABLES USING cls
# ============================================================

"""
One common use of a class method is accessing or modifying
class variables.

The cls parameter allows us to access class variables.

Example:

cls.company_name

This refers to the company_name variable belonging to the
current class.
"""


class Employee:
    company_name="NextGen Software"

    @classmethod
    def show_company(cls):
        print("Company:",cls.company_name)


Employee.show_company()


# ============================================================
# 7. MODIFYING A CLASS VARIABLE USING cls
# ============================================================

"""
A class method can also modify a class variable.

For example:

cls.company_name=new_name

This changes the class variable for the class.
"""


class Company:
    name="Alpha Solutions"

    @classmethod
    def change_name(cls,new_name):
        cls.name=new_name


print("Before:",Company.name)

Company.change_name("Beta Solutions")

print("After:",Company.name)


# ============================================================
# 8. CLASS METHODS CAN BE CALLED USING THE CLASS
# ============================================================

"""
A class method is commonly called using the class name.

Syntax:

ClassName.method_name()

For example:

Company.display_name()

Python automatically passes the Company class as cls.
"""


class University:
    title="National University"

    @classmethod
    def display_title(cls):
        print("University:",cls.title)


University.display_title()


# ============================================================
# 9. CLASS METHODS CAN ALSO BE CALLED USING AN OBJECT
# ============================================================

"""
A class method can also be accessed through an object.

However, the method still receives the class as cls,
not the object as self.

This is different from an instance method.
"""


class Department:
    name="Computer Science"

    @classmethod
    def show_department(cls):
        print("Department:",cls.name)


department_object=Department()

department_object.show_department()


# ============================================================
# 10. COMMON USE CASE: ALTERNATIVE CONSTRUCTORS
# ============================================================

"""
One of the most useful applications of class methods is
creating alternative constructors.

We already know that __init__() is used to initialize
an object.

Normally, we create an object like this:

person=Person("Ali", 25)

But sometimes our data is available in another format.

For example, we may have:

"Ali,25"

or:

{"name":"Ali","age":25}

A class method can take this data, process it, and then
create and return an object.

Such a method is commonly called an alternative constructor
or factory method.
"""


# ============================================================
# 11. ALTERNATIVE CONSTRUCTOR FROM A STRING
# ============================================================

"""
Suppose we receive a person's information as a string:

"Ali,25"

We can create a class method that:

1. Receives the string.
2. Splits it into separate values.
3. Creates an object.
4. Returns the object.

Because the method creates an object using the class, cls
is useful here.
"""


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def from_string(cls,data):
        name, age=data.split(",")
        return cls(name,int(age))

    def show_information(self):
        print("Name:",self.name)
        print("Age:",self.age)


person_data="Ali,25"

person_object=Person.from_string(person_data)

person_object.show_information()


# ============================================================
# 12. HOW THE STRING ALTERNATIVE CONSTRUCTOR WORKS
# ============================================================

"""
Consider this line:

person_object=Person.from_string(person_data)

Python calls the class method.

Inside the method:

cls
    refers to Person.

The string:

"Ali,25"

is split into:

name="Ali"
age="25"

Then:

return cls(name,int(age))

creates a Person object.

So the class method provides another way to create a Person
object.
"""


class Customer:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def from_text(cls,information):
        customer_name,customer_age=information.split("-")
        return cls(customer_name,int(customer_age))

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)


customer_data="Mariam-28"

customer_object=Customer.from_text(customer_data)

customer_object.display()


# ============================================================
# 13. ALTERNATIVE CONSTRUCTOR FROM A DICTIONARY
# ============================================================

"""
A class method can also create an object from a dictionary.

Suppose we have:

{
    "name":"Hassan",
    "age":30
}

The class method can read these values and pass them to
the constructor.
"""


class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def from_dictionary(cls,data):
        return cls(
            data["name"],
            data["age"]
        )

    def show_details(self):
        print("Name:",self.name)
        print("Age:",self.age)


employee_data={
    "name":"Hassan",
    "age":30
}

employee_object=Employee.from_dictionary(employee_data)

employee_object.show_details()


# ============================================================
# 14. WHY USE cls IN AN ALTERNATIVE CONSTRUCTOR?
# ============================================================

"""
Consider:

return cls(name,age)

Using cls allows the class method to create an object of
the current class.

This is better than directly writing:

return Person(name,age)

because cls makes the method more flexible.

The method can work correctly even when the class is inherited
by another class.

For now, the important idea is:

cls(...) creates an object using the current class.
"""


class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    @classmethod
    def from_text(cls,data):
        product_name,product_price=data.split(",")
        return cls(product_name,float(product_price))

    def show_product(self):
        print("Product:",self.name)
        print("Price:",self.price)


product_data="Keyboard,2500"

product_object=Product.from_text(product_data)

product_object.show_product()


# ============================================================
# 15. ALTERNATIVE CONSTRUCTOR FROM A DICTIONARY
# ============================================================

"""
Let's create another example using a dictionary.

This can be useful when data comes from an API, JSON object,
database record, or another external source.
"""


class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    @classmethod
    def from_dictionary(cls,data):
        return cls(
            data["title"],
            data["author"],
            data["price"]
        )

    def show_book(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)


book_data={
    "title":"Python Programming",
    "author":"Daniel Wilson",
    "price":3000
}

book_object=Book.from_dictionary(book_data)

book_object.show_book()


# ============================================================
# 16. INSTANCE METHOD VS CLASS METHOD
# ============================================================

"""
Let's compare an instance method and a class method.

Instance method:

def show_name(self):
    print(self.name)

It works with data belonging to a particular object.

Class method:

@classmethod
def show_school(cls):
    print(cls.school)

It works with data belonging to the class.
"""


class Student:
    school="Bright Future School"

    def __init__(self,name):
        self.name=name

    def show_name(self):
        print("Student:",self.name)

    @classmethod
    def show_school(cls):
        print("School:",cls.school)


student_object=Student("Noor")

student_object.show_name()
Student.show_school()


# ============================================================
# 17. CLASS METHOD WITH ADDITIONAL ARGUMENTS
# ============================================================

"""
A class method can accept additional arguments after cls.

For example:

@classmethod
def update_tax(cls,rate):

Here:

cls
    Refers to the class.

rate
    Is an additional argument provided by the caller.
"""


class Store:
    tax_rate=5

    @classmethod
    def update_tax(cls,new_rate):
        cls.tax_rate=new_rate

    @classmethod
    def show_tax(cls):
        print("Tax Rate:",cls.tax_rate)


Store.show_tax()

Store.update_tax(8)

Store.show_tax()


# ============================================================
# 18. CLASS METHOD AS A FACTORY METHOD
# ============================================================

"""
A factory method is a method that provides a convenient way
to create objects.

A class method is often used to implement factory methods.

For example, an Employee object can normally be created using:

Employee("Ayesha","IT")

But we can also provide:

Employee.from_string("Ayesha,IT")

Both create an Employee object, but they accept data in
different formats.
"""


class Worker:
    def __init__(self,name,department):
        self.name=name
        self.department=department

    @classmethod
    def from_string(cls,data):
        worker_name,worker_department=data.split(",")
        return cls(worker_name,worker_department)

    def show_details(self):
        print("Name:",self.name)
        print("Department:",self.department)


worker_one=Worker("Ayesha","IT")

worker_two=Worker.from_string("Bilal,Finance")

print("Worker One:")
worker_one.show_details()

print()

print("Worker Two:")
worker_two.show_details()


# ============================================================
# 19. NORMAL CONSTRUCTOR VS ALTERNATIVE CONSTRUCTOR
# ============================================================

"""
A class can have its normal constructor and one or more
alternative constructors.

Normal constructor:

def __init__(self,name,age):

Alternative constructor:

@classmethod
def from_string(cls,data):

The normal constructor receives separate arguments.

The alternative constructor can accept data in another format
and convert it into the format required by __init__().
"""


class StudentRecord:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def from_string(cls,data):
        student_name,student_age=data.split(":")
        return cls(student_name,int(student_age))

    def show_record(self):
        print("Name:",self.name)
        print("Age:",self.age)


# Normal constructor
student_one=StudentRecord("Zainab",22)

# Alternative constructor
student_two=StudentRecord.from_string("Hamza:24")

print("Student One:")
student_one.show_record()

print()

print("Student Two:")
student_two.show_record()


# ============================================================
# 20. COMPLETE EXAMPLE
# ============================================================

"""
Let's combine everything we have learned.

We will create a Course class.

The class will have:

Class variable:
    platform

Instance variables:
    title
    instructor
    duration

Instance method:
    show_course()

Class method:
    from_string()

The from_string() method will allow us to create a Course
object from a string.
"""


class Course:
    platform="Online Learning Platform"

    def __init__(self,title,instructor,duration):
        self.title=title
        self.instructor=instructor
        self.duration=duration

    def show_course(self):
        print("Course:",self.title)
        print("Instructor:",self.instructor)
        print("Duration:",self.duration,"hours")
        print("Platform:",self.platform)

    @classmethod
    def from_string(cls,data):
        title, instructor,duration=data.split("|")
        return cls(
            title,
            instructor,
            int(duration)
        )


course_data="Python OOP|Emma Wilson|20"

python_course=Course.from_string(course_data)

python_course.show_course()


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. A class method is a method that works with the class itself.
2. A class method is created using the @classmethod decorator.
3. The first parameter of a class method is conventionally
   named cls.
4. cls refers to the current class.
5. self refers to the current object.
6. cls refers to the current class.
7. Class methods can access class variables using cls.
8. Class methods can modify class variables using cls.
9. Class methods can be called using the class name:

   ClassName.method()

10. A class method can also be accessed through an object,
    but it still receives the class as cls.
11. One of the most common uses of class methods is creating
    alternative constructors.
12. Alternative constructors provide additional ways to create
    objects.
13. A class method can create an object using:

    return cls(...)

14. Alternative constructors can be useful when data is
    available in formats such as strings or dictionaries.
15. A class can have both a normal constructor and multiple
    alternative constructors.

Simple comparison:

Instance Method:
    self -> current object

Class Method:
    cls -> current class

A useful pattern is:

@classmethod
def from_string(cls,data):
    ...
    return cls(...)

This allows us to convert external data into an object
conveniently.

In the next chapter, we will learn about static methods and
how they differ from instance methods and class methods.
"""