"""
SUPER() FUNCTION
"""


# ============================================================
# 1. INTRODUCTION TO super()
# ============================================================

"""
The super() function is used in inheritance to access methods
and attributes from a parent class.

It is especially useful when a child class overrides a method
but still wants to use the functionality provided by its
parent class.

In simple words:

    super() → gives access to the next class in the MRO.

The most common uses of super() are:

    1. Calling the parent class constructor.
    2. Calling a parent class method.
    3. Working with multiple inheritance.

We have already seen a small preview of super() in the
previous chapter.

In this chapter, we will learn how super() works in more
detail.
"""


# ============================================================
# 2. A SIMPLE EXAMPLE OF super()
# ============================================================

"""
Suppose we have a parent class with a method called show().

The child class overrides show(), but we also want to execute
the parent's version.

We can use:

    super().show()
"""


class Parent:

    def show(self):
        print("This is the Parent class.")


class Child(Parent):

    def show(self):
        super().show()
        print("This is the Child class.")


child_object=Child()

child_object.show()


"""
Output:

    This is the Parent class.
    This is the Child class.

The line:

    super().show()

calls the parent's version of show().
"""


# ============================================================
# 3. WHY DO WE NEED super()?
# ============================================================

"""
Consider the following situation:

A child class overrides a parent method.

If the child completely replaces the method, the parent's
behavior is no longer automatically executed.

For example:

    class Parent:

        def show(self):
            print("Parent")


    class Child(Parent):

        def show(self):
            print("Child")

The parent method is not called.

Sometimes this is exactly what we want.

But sometimes we want:

    Parent behavior
        +
    Child behavior

This is where super() becomes useful.
"""


class Employee:

    def work(self):
        print("Employee is working.")


class Developer(Employee):

    def work(self):
        super().work()
        print("Developer is writing code.")


developer_object=Developer()

developer_object.work()


"""
Output:

    Employee is working.
    Developer is writing code.

The child keeps the parent's behavior and adds its own
behavior.
"""


# ============================================================
# 4. CALLING THE PARENT CONSTRUCTOR
# ============================================================

"""
One of the most common uses of super() is calling the parent
class's __init__() method.

Suppose the parent class initializes an attribute called name.

The child class also needs that initialization.

We can write:

    super().__init__(name)

This calls the parent's constructor.
"""


class Person:

    def __init__(self,name):
        self.name=name


class Student(Person):

    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade


student_object=Student("Ayesha","A")

print("Name:",student_object.name)
print("Grade:",student_object.grade)


"""
Here:

    super().__init__(name)

calls:

    Person.__init__(name)

The parent creates:

    self.name

Then the child creates:

    self.grade
"""


# ============================================================
# 5. WHY super().__init__() IS USEFUL
# ============================================================

"""
Suppose a parent class has several initialization statements.

Instead of copying all of them into the child class, we can
call the parent constructor using super().

This keeps the code cleaner and avoids repeating code.
"""


class Account:

    def __init__(self,owner,account_number):
        self.owner=owner
        self.account_number=account_number


class SavingsAccount(Account):

    def __init__(self,owner,account_number,interest_rate):
        super().__init__(owner,account_number)
        self.interest_rate=interest_rate


savings_object=SavingsAccount(
    "Hamza",
    "SA1025",
    4.5
)

print("Owner:",savings_object.owner)
print("Account Number:",savings_object.account_number)
print("Interest Rate:",savings_object.interest_rate)


"""
The parent is responsible for:

    owner
    account_number

The child is responsible for:

    interest_rate

This separation makes the classes easier to maintain.
"""


# ============================================================
# 6. CALLING A PARENT METHOD
# ============================================================

"""
super() can also be used to call a parent method other than
__init__().

Syntax:

    super().method_name()
"""


class Vehicle:

    def start(self):
        print("Vehicle has started.")


class Car(Vehicle):

    def start(self):
        super().start()
        print("Car is ready to drive.")


car_object=Car()

car_object.start()


"""
The call:

    super().start()

runs:

    Vehicle.start()

Then the child continues with its own behavior.
"""


# ============================================================
# 7. super() WITH MULTIPLE METHODS
# ============================================================

"""
A child class can use super() to call multiple methods from
its parent.
"""


class User:

    def login(self):
        print("Checking user credentials.")

    def logout(self):
        print("User logged out.")


class Admin(User):

    def login(self):
        super().login()
        print("Checking admin permissions.")

    def logout(self):
        super().logout()
        print("Closing admin session.")


admin_object=Admin()

admin_object.login()
admin_object.logout()


# ============================================================
# 8. super() DOES NOT MEAN "CALL THE PARENT CLASS DIRECTLY"
# ============================================================

"""
A common beginner misunderstanding is:

    super() always means:
    "call my parent class."

A more accurate explanation is:

    super() gives access to the next class in the
    Method Resolution Order (MRO).

This distinction becomes very important when multiple
inheritance is used.

With simple inheritance, the next class in the MRO is usually
the parent class.

With multiple inheritance, it may be another class according
to the MRO.
"""


# ============================================================
# 9. super() AND MRO
# ============================================================

"""
Consider:

        ParentA      ParentB
            \          /
             \        /
              Child

The MRO might be:

    Child
    ParentA
    ParentB
    object

When Child uses:

    super()

Python follows the MRO and moves to the next class.

So super() is connected directly to MRO.
"""


class ParentA:

    def show(self):
        print("ParentA")


class ParentB:

    def show(self):
        print("ParentB")


class Child(ParentA,ParentB):

    def show(self):
        print("Child")
        super().show()


child_object=Child()

child_object.show()

print(Child.mro())


"""
The MRO is:

    Child
    ParentA
    ParentB
    object

Therefore:

    super().show()

finds show() in ParentA.
"""


# ============================================================
# 10. super() IN MULTIPLE INHERITANCE
# ============================================================

"""
Now let's look at a more important multiple inheritance
example.

Suppose we have two parent classes:

    Writer
    Speaker

and a child class:

    Presenter

Presenter inherits from both.
"""


class Writer:

    def work(self):
        print("Writer is writing.")


class Speaker:

    def speak(self):
        print("Speaker is speaking.")


class Presenter(Writer,Speaker):

    def work(self):
        super().work()
        print("Presenter is presenting.")


presenter_object=Presenter()

presenter_object.work()
presenter_object.speak()


"""
The MRO is:

    Presenter
    Writer
    Speaker
    object

Therefore:

    super().work()

finds Writer.work().
"""


# ============================================================
# 11. super() WITH A CHAIN OF CLASSES
# ============================================================

"""
One of the most useful features of super() appears when
multiple classes use super().

Consider:

        A
        |
        B
        |
        C

Each class can call super().

The call can continue through the MRO.
"""


class Base:

    def process(self):
        print("Base process")


class Middle(Base):

    def process(self):
        super().process()
        print("Middle process")


class Final(Middle):

    def process(self):
        super().process()
        print("Final process")


final_object=Final()

final_object.process()


"""
Output:

    Base process
    Middle process
    Final process

The process works through the inheritance chain.

The MRO is:

    Final
    Middle
    Base
    object

Each super() moves to the next class in that order.
"""


# ============================================================
# 12. super() IN THE DIAMOND STRUCTURE
# ============================================================

"""
super() becomes particularly useful in a diamond inheritance
structure.

Diagram:

              A
             / \
            B   C
             \ /
              D

The MRO may be:

    D
    B
    C
    A
    object

If B and C both use super(), Python can move through the MRO
instead of directly jumping to A.
"""


class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        super().show()
        print("B")


class C(A):

    def show(self):
        super().show()
        print("C")


class D(B, C):

    def show(self):
        super().show()
        print("D")


diamond_object=D()

diamond_object.show()

print(D.mro())


"""
The output is:

    A
    C
    B
    D

The MRO is:

    D
    B
    C
    A
    object

Notice something important.

D calls super():

    D → B

B calls super():

    B → C

C calls super():

    C → A

A reaches the end of the chain.

This is one of the main reasons super() is powerful in
multiple inheritance.
"""


# ============================================================
# 13. WHY DIRECT PARENT CALLS CAN BE PROBLEMATIC
# ============================================================

"""
You may sometimes see code like:

    ParentClass.method(self)

This directly calls a particular parent class.

Although this can work, it can cause problems with complex
multiple inheritance because it does not follow the MRO in the
same cooperative way that super() does.

Using:

    super().method()

allows Python to follow the MRO.
"""


class BaseWorker:

    def work(self):
        print("Base worker")


class OfficeWorker(BaseWorker):

    def work(self):
        print("Office worker")


class TeamMember(OfficeWorker):

    def work(self):
        super().work()
        print("Team member")


team_member_object=TeamMember()

team_member_object.work()


"""
Here super() follows the inheritance structure rather than
hard-coding the parent class name.
"""


# ============================================================
# 14. COMMON MISTAKE: FORGETTING super().__init__()
# ============================================================

"""
One of the most common mistakes occurs when a child class
overrides __init__() but forgets to call the parent's
__init__().

Consider this example.
"""


class Person:

    def __init__(self,name):
        self.name=name


class Student(Person):

    def __init__(self,grade):
        self.grade=grade


student_object=Student("A")

print("Grade:",student_object.grade)

# The following line would cause an AttributeError:
#
# print(student_object.name)


"""
Why?

The Student class has its own __init__().

Because it does not call:

    super().__init__(name)

the Person.__init__() method never runs.

Therefore:

    self.name

is never created.
"""


# ============================================================
# 15. CORRECTING THE MISTAKE
# ============================================================

"""
If the child needs the attributes created by the parent,
call the parent constructor using super().
"""


class Person:

    def __init__(self,name):
        self.name=name


class Student(Person):

    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade


student_object=Student("Sara","A")

print("Name:",student_object.name)
print("Grade:",student_object.grade)


"""
Now both attributes are initialized:

    self.name
    self.grade
"""


# ============================================================
# 16. ANOTHER COMMON MISTAKE
# ============================================================

"""
Consider a parent class that performs important setup.
"""


class Device:

    def __init__(self,brand):
        self.brand=brand
        print("Device setup completed.")


class Laptop(Device):

    def __init__(self,brand,memory):
        self.memory=memory


laptop_object=Laptop("Dell","16 GB")

print("Memory:",laptop_object.memory)

# The following line would cause an AttributeError:
#
# print(laptop_object.brand)


"""
The parent constructor was not called.

Therefore:

    self.brand

was never created.

The child only initialized:

    self.memory
"""


# ============================================================
# 17. CORRECT VERSION
# ============================================================

class Device:

    def __init__(self,brand):
        self.brand=brand
        print("Device setup completed.")


class Laptop(Device):

    def __init__(self,brand,memory):
        super().__init__(brand)
        self.memory=memory


laptop_object=Laptop("Lenovo","8 GB")

print("Brand:",laptop_object.brand)
print("Memory:",laptop_object.memory)


# ============================================================
# 18. super() WITH __init__() AND OTHER METHODS
# ============================================================

"""
A child class can use super() for both:

    - __init__()
    - regular methods

This is very common in object-oriented programs.
"""


class Person:

    def __init__(self,name):
        self.name=name

    def introduce(self):
        print("My name is",self.name)


class Teacher(Person):

    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject

    def introduce(self):
        super().introduce()
        print("I teach",self.subject)


teacher_object=Teacher("Nadia","Python")

teacher_object.introduce()


"""
Here:

    super().__init__(name)

calls the parent's constructor.

And:

    super().introduce()

calls the parent's introduce() method.
"""


# ============================================================
# 19. super() WITHOUT ARGUMENTS
# ============================================================

"""
In modern Python, inside an instance method, we normally write:

    super()

instead of:

    super(ClassName,self)

For example:

    super().show()

This is the recommended and easier-to-read form.
"""


class Parent:

    def greet(self):
        print("Hello from Parent.")


class Child(Parent):

    def greet(self):
        super().greet()
        print("Hello from Child.")


greeting_object=Child()

greeting_object.greet()


# ============================================================
# 20. super() AND THE CURRENT CLASS
# ============================================================

"""
It is important to understand that:

    super()

does not create a new object.

It gives access to the next class in the MRO.

For example:

    class Child(Parent):

        def show(self):
            super().show()

Here super() refers to the next class in Child's MRO.

It is used to access the inherited implementation.
"""


# ============================================================
# 21. CHECKING THE MRO
# ============================================================

"""
When you are unsure about what super() will call, check the
class's MRO.

Use:

    ClassName.mro()

or:

    ClassName.__mro__
"""


class Alpha:

    def display(self):
        print("Alpha")


class Beta(Alpha):

    def display(self):
        super().display()
        print("Beta")


print(Beta.mro())

beta_object=Beta()

beta_object.display()


"""
The MRO is:

    Beta
    Alpha
    object

Therefore:

    super().display()

calls Alpha.display().
"""


# ============================================================
# 22. PRACTICAL EXAMPLE
# ============================================================

"""
Imagine a notification system.

The parent class sends a basic notification.

A child class can use super() to perform the basic operation
and then add extra behavior.
"""


class Notification:

    def send(self):
        print("Sending notification.")


class EmailNotification(Notification):

    def send(self):
        super().send()
        print("Sending notification through email.")


email_object=EmailNotification()

email_object.send()


"""
The child does not need to rewrite the parent's notification
logic.

It simply reuses it with super() and adds its own behavior.
"""


# ============================================================
# 23. ANOTHER PRACTICAL EXAMPLE WITH __init__()
# ============================================================

"""
Suppose every product has a name and price.

A DigitalProduct also needs a file size.

The parent handles common attributes and the child handles
its additional attribute.
"""


class Product:

    def __init__(self,name,price):
        self.name=name
        self.price=price


class DigitalProduct(Product):

    def __init__(self,name,price,file_size):
        super().__init__(name,price)
        self.file_size=file_size


digital_product_object=DigitalProduct(
    "Python Course",
    49.99,
    "2 GB"
)

print("Name:",digital_product_object.name)
print("Price:",digital_product_object.price)
print("File Size:",digital_product_object.file_size)


# ============================================================
# 24. IMPORTANT RULE FOR MULTIPLE INHERITANCE
# ============================================================

"""
When using multiple inheritance, classes should generally be
designed to cooperate when using super().

For example:

    class A:
        def show(self):
            super().show()

    class B(A):
        def show(self):
            super().show()

This allows the method call to move through the MRO.

This is sometimes called cooperative multiple inheritance.

For beginners, the most important idea is:

    super() follows the MRO.

We will use this idea when working with multiple inheritance.
"""


# ============================================================
# 25. SUMMARY
# ============================================================

"""
Important points:

1. super() is used with inheritance.

2. super() provides access to the next class in the
   Method Resolution Order (MRO).

3. In simple inheritance, this is usually the parent class.

4. One common use is calling the parent constructor:

       super().__init__(arguments)

5. Another common use is calling a parent method:

       super().method_name()

6. super() allows a child class to reuse parent functionality
   instead of duplicating code.

7. A child can call the parent's method and then add its own
   behavior.

8. Example:

       class Child(Parent):

           def show(self):
               super().show()
               print("Child behavior")

9. super() is especially important in multiple inheritance.

10. In multiple inheritance, super() follows the MRO instead
    of simply referring to one specific parent class.

11. For example:

        class Child(ParentA, ParentB):
            pass

    super() follows the MRO calculated by Python.

12. The MRO can be checked using:

        Child.mro()

    or:

        Child.__mro__

13. A common mistake is overriding __init__() and forgetting
    to call super().__init__().

14. If the parent constructor creates important attributes,
    forgetting super().__init__() means those attributes may
    never be created.

15. Example of the problem:

        class Child(Parent):

            def __init__(self):
                self.child_data = ...

    If Parent.__init__() was responsible for creating
    self.parent_data, that data will not exist.

16. The solution is often:

        class Child(Parent):

            def __init__(self):
                super().__init__()
                self.child_data = ...

17. super() does not create a new object.

18. super() does not simply mean "call my parent."

19. A better mental model is:

        super() → move to the next class in the MRO.

Simple way to remember:

    super().__init__()
        → Call the next class's constructor.

    super().method()
        → Call the next class's version of a method.

    super()
        → Follow the MRO.

The main purpose of super() is to reuse inherited behavior
cleanly and make inheritance structures easier to maintain.

In the next chapter, we will learn about Polymorphism and
how the same interface or method call can produce different
behavior depending on the object.
"""