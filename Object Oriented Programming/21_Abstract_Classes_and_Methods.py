"""
ABSTRACT CLASSES AND ABSTRACT METHODS
"""


# ============================================================
# 1. INTRODUCTION TO ABSTRACT CLASSES
# ============================================================

"""
In the previous chapter, we learned about abstraction.

Abstraction means:

    Hiding unnecessary implementation details and exposing
    only the essential functionality.

Python provides a formal way to implement abstraction using
the `abc` module.

The `abc` module stands for:

    Abstract Base Classes

It provides tools such as:

    ABC
    abstractmethod

These tools allow us to create abstract classes and abstract
methods.
"""


# ============================================================
# 2. IMPORTING ABC AND ABSTRACTMETHOD
# ============================================================

"""
To create an abstract class in Python, we commonly import:

    ABC
    abstractmethod

from the `abc` module.
"""


from abc import ABC,abstractmethod


"""
ABC is a class provided by Python.

We can inherit from ABC to make our class an abstract base
class.

`abstractmethod` is a decorator used to mark a method as
abstract.
"""


# ============================================================
# 3. WHAT IS AN ABSTRACT CLASS?
# ============================================================

"""
An abstract class is a class that is designed to be used as a
base class.

It is generally not created to make objects directly.

Instead, it provides a common structure that child classes
must follow.

For example, imagine we have different types of animals.

We know that every animal should be able to make a sound.

However, the exact sound depends on the animal.

A dog may bark.

A cat may meow.

A cow may moo.

So we can create an abstract class called Animal that says:

    Every animal must have a make_sound() method.

But the Animal class itself does not need to provide the
specific sound.
"""


# ============================================================
# 4. CREATING A SIMPLE ABSTRACT CLASS
# ============================================================

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


"""
Animal is an abstract class because it inherits from:

    ABC

make_sound() is an abstract method because it is decorated
with:

    @abstractmethod

The abstract method tells child classes:

    "You must provide an implementation for this method."
"""


# ============================================================
# 5. WHY CAN'T WE CREATE AN OBJECT OF AN ABSTRACT CLASS?
# ============================================================

"""
Because Animal has an abstract method, Python does not allow
us to directly create an object from Animal.

For example:

    animal_object=Animal()

would raise a TypeError.

We will not execute that line here because it would stop the
program.

The important idea is:

    Abstract class
          ↓
    Contains abstract method
          ↓
    Cannot be instantiated directly
"""


# ============================================================
# 6. ABSTRACT METHODS
# ============================================================

"""
An abstract method is a method that is declared in the parent
class but is expected to be implemented by child classes.

For example:
"""


class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass


"""
The class Vehicle defines the required behavior:

    start_engine()

But it does not provide a specific implementation.

Every concrete child class must implement it.
"""


# ============================================================
# 7. IMPLEMENTING AN ABSTRACT METHOD
# ============================================================

"""
Let's create a child class from Animal.

The Dog class must implement:

    make_sound()
"""


class Dog(Animal):

    def make_sound(self):
        print("Dog says: Woof!")


dog_object=Dog()

dog_object.make_sound()


"""
Dog is a concrete class because it provides an implementation
for the abstract method:

    make_sound()

Therefore, we can create a Dog object.
"""


# ============================================================
# 8. ANOTHER CHILD CLASS
# ============================================================

class Cat(Animal):

    def make_sound(self):
        print("Cat says: Meow!")


cat_object=Cat()

cat_object.make_sound()


"""
Cat also implements:

    make_sound()

So Cat can also be instantiated.

We now have:

        Animal
        /    \
      Dog    Cat

Animal defines what child classes must provide.

Dog and Cat define how that behavior works.
"""


# ============================================================
# 9. ABSTRACT CLASS AS A CONTRACT
# ============================================================

"""
An abstract class can be thought of as a contract.

For example:

    Animal

can say:

    "Every concrete animal class must provide
     make_sound()."

The child classes agree to follow this contract.

So:

        Animal
          |
          | requires
          ↓
      make_sound()
          |
       ┌──┴──┐
       ↓     ↓
      Dog   Cat
       |     |
       ↓     ↓
      Woof  Meow


The parent defines the required behavior.

The child provides the actual implementation.
"""


# ============================================================
# 10. WHAT HAPPENS IF A CHILD CLASS DOES NOT IMPLEMENT
#     THE ABSTRACT METHOD?
# ============================================================

"""
Suppose we create a child class but forget to implement
make_sound().
"""


class Bird(Animal):
    pass


"""
Bird inherits from Animal.

Animal requires:

    make_sound()

But Bird does not implement it.

Therefore, Bird is still considered abstract.

Trying to create:

    bird_object=Bird()

would raise a TypeError.

We will not execute that statement because it would stop the
program.

The important point is:

    A child class must implement all inherited abstract
    methods before it can be instantiated.
"""


# ============================================================
# 11. FIXING THE CHILD CLASS
# ============================================================

class Sparrow(Animal):

    def make_sound(self):
        print("Sparrow makes a chirping sound.")


sparrow_object=Sparrow()

sparrow_object.make_sound()


"""
Sparrow implements make_sound(), so it can be instantiated.
"""


# ============================================================
# 12. MULTIPLE CHILD CLASSES
# ============================================================

"""
An abstract class becomes especially useful when several child
classes should follow the same structure.
"""


class Payment(ABC):

    @abstractmethod
    def process_payment(self,amount):
        pass


class CreditCardPayment(Payment):

    def process_payment(self,amount):
        print("Processing credit card payment:",amount)


class CashPayment(Payment):

    def process_payment(self,amount):
        print("Processing cash payment:",amount)


class MobilePayment(Payment):

    def process_payment(self,amount):
        print("Processing mobile payment:",amount)


card_payment_object=CreditCardPayment()
cash_payment_object=CashPayment()
mobile_payment_object=MobilePayment()

card_payment_object.process_payment(1500)
cash_payment_object.process_payment(800)
mobile_payment_object.process_payment(2200)


"""
All three classes must provide:

    process_payment()

But each class can implement it differently.

This gives us a common structure with different behavior.
"""


# ============================================================
# 13. ABSTRACT CLASS CAN CONTAIN REGULAR METHODS
# ============================================================

"""
An important point is that an abstract class does not have to
contain only abstract methods.

It can contain:

    abstract methods
    regular methods
    instance variables
    constructors

For example:
"""


class Employee(ABC):

    def __init__(self,name):
        self.name=name

    @abstractmethod
    def calculate_salary(self):
        pass

    def introduce(self):
        print("Employee:",self.name)


class Developer(Employee):

    def calculate_salary(self):
        return 80000


developer_object=Developer("Ali")

developer_object.introduce()

print("Salary:",developer_object.calculate_salary())


"""
Employee contains:

    __init__()
    introduce()

as regular methods.

It also contains:

    calculate_salary()

as an abstract method.

The child class must implement calculate_salary().
"""


# ============================================================
# 14. ABSTRACT CLASS WITH SHARED BEHAVIOR
# ============================================================

"""
Abstract classes are useful when child classes have some common
behavior but also need to provide their own specific behavior.
"""


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print("This object represents a shape.")


class Rectangle(Shape):

    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width


rectangle_object=Rectangle(10,5)

rectangle_object.describe()

print("Area:",rectangle_object.area())


"""
Shape provides:

    describe()

as common behavior.

Shape requires:

    area()

as abstract behavior.

Rectangle provides its own implementation of area().
"""


# ============================================================
# 15. ABSTRACT METHODS CAN HAVE PARAMETERS
# ============================================================

"""
An abstract method can also accept parameters.

For example:
"""


class Notification(ABC):

    @abstractmethod
    def send(self,message):
        pass


class EmailNotification(Notification):

    def send(self,message):
        print("Email notification:",message)


class SMSNotification(Notification):

    def send(self,message):
        print("SMS notification:",message)


email_notification_object=EmailNotification()
sms_notification_object=SMSNotification()

email_notification_object.send("Your order has been shipped.")

sms_notification_object.send("Your OTP is 1234.")


"""
The abstract class defines the expected method structure:

    send(message)

Each child class decides how the message is sent.
"""


# ============================================================
# 16. ANIMAL EXAMPLE
# ============================================================

"""
Let's create the main example again in a more complete form.

The Animal class requires every child class to implement
make_sound().
"""


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):

    def make_sound(self):
        print("Dog: Woof!")


class Cat(Animal):

    def make_sound(self):
        print("Cat: Meow!")


class Cow(Animal):

    def make_sound(self):
        print("Cow: Moo!")


dog_object=Dog()
cat_object=Cat()
cow_object=Cow()

dog_object.make_sound()
cat_object.make_sound()
cow_object.make_sound()


"""
All three classes follow the contract defined by Animal.

Animal says:

    make_sound() must exist.

Dog says:

    A dog makes this sound.

Cat says:

    A cat makes this sound.

Cow says:

    A cow makes this sound.
"""


# ============================================================
# 17. ABSTRACT CLASSES AND POLYMORPHISM
# ============================================================

"""
Abstract classes work very well with polymorphism.

We can create a function that expects an Animal.

The function can call:

    make_sound()

without needing to know which concrete animal it received.
"""


def make_animal_sound(animal):
    animal.make_sound()


animals=[
    Dog(),
    Cat(),
    Cow()
]


for animal in animals:
    make_animal_sound(animal)


"""
The same function works with:

    Dog
    Cat
    Cow

because all of them follow the Animal contract.

This is polymorphism working together with abstraction.
"""


# ============================================================
# 18. ABSTRACT CLASS VS REGULAR INHERITANCE
# ============================================================

"""
Let's compare abstract classes with regular inheritance.

REGULAR INHERITANCE:

    A child class inherits functionality from a parent class.

The child may or may not override methods.

Example:
"""


class Person:

    def introduce(self):
        print("Hello, I am a person.")


class Student(Person):

    pass


student_object=Student()

student_object.introduce()


"""
Student inherits introduce() from Person.

There is no requirement for Student to implement anything.

This is regular inheritance.
"""


# ============================================================
# 19. ABSTRACT INHERITANCE
# ============================================================

"""
Now consider an abstract class.
"""


class Person(ABC):

    @abstractmethod
    def introduce(self):
        pass


class Student(Person):

    def introduce(self):
        print("Hello, I am a student.")


student_object=Student()

student_object.introduce()


"""
Here, Person does not simply provide optional functionality.

It defines a requirement:

    introduce()

Student must implement it before we can create a Student
object.
"""


# ============================================================
# 20. MAIN DIFFERENCE
# ============================================================

"""
The main difference is:

REGULAR INHERITANCE:

    "You can inherit this behavior."

ABSTRACT CLASS:

    "You must provide this behavior."

Regular inheritance is mainly about code reuse and creating
relationships between classes.

Abstract classes are useful when we want to define a common
structure or contract that subclasses must follow.
"""


# ============================================================
# 21. REGULAR INHERITANCE EXAMPLE
# ============================================================

class Vehicle:

    def move(self):
        print("Vehicle is moving.")


class Car(Vehicle):
    pass


car_object=Car()

car_object.move()


"""
Car automatically gets the implementation of move().

No method is required to be implemented by Car.

This is regular inheritance.
"""


# ============================================================
# 22. ABSTRACT INHERITANCE EXAMPLE
# ============================================================

class Vehicle(ABC):

    @abstractmethod
    def move(self):
        pass


class Bicycle(Vehicle):

    def move(self):
        print("Bicycle is moving.")


bicycle_object=Bicycle()

bicycle_object.move()


"""
Bicycle must implement move() because Vehicle marked it as an
abstract method.
"""


# ============================================================
# 23. ABSTRACT CLASS DEFINES WHAT, CHILD DEFINES HOW
# ============================================================

"""
A very useful way to understand abstract classes is:

    Abstract class:
        Defines WHAT must be done.

    Child class:
        Defines HOW it is done.

For example:

    Animal
        ↓
    make_sound()

Animal says:

    "Every concrete animal must make a sound."

Dog says:

    "I make a Woof sound."

Cat says:

    "I make a Meow sound."

This separation makes the design clear.
"""


# ============================================================
# 24. MULTIPLE ABSTRACT METHODS
# ============================================================

"""
An abstract class can contain more than one abstract method.

For example, a payment system might require:

    validate()
    pay()
    refund()
"""


class PaymentProcessor(ABC):

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def pay(self,amount):
        pass

    @abstractmethod
    def refund(self,amount):
        pass


"""
A concrete child class must implement all three methods before
it can be instantiated.
"""


class OnlinePaymentProcessor(PaymentProcessor):

    def validate(self):
        print("Payment details validated.")

    def pay(self,amount):
        print("Paid:",amount)

    def refund(self,amount):
        print("Refunded:",amount)


online_payment_object=OnlinePaymentProcessor()

online_payment_object.validate()
online_payment_object.pay(3000)
online_payment_object.refund(1000)


"""
OnlinePaymentProcessor provides implementations for all three
abstract methods.

Therefore, it can be instantiated.
"""


# ============================================================
# 25. FORGETTING ONE ABSTRACT METHOD
# ============================================================

"""
Suppose a child class implements only two of the three required
methods.

For example:

    validate()
    pay()

but forgets:

    refund()

The child class remains abstract.

Therefore, Python will not allow us to create its object.

This helps catch incomplete implementations early.
"""


class IncompletePayment(PaymentProcessor):

    def validate(self):
        print("Validated.")

    def pay(self,amount):
        print("Paid:",amount)

    # refund() is missing


"""
This class cannot be instantiated because refund() is still
abstract.

The following would raise a TypeError:

    payment_object=IncompletePayment()
"""


# ============================================================
# 26. WHY ABSTRACT CLASSES ARE USEFUL
# ============================================================

"""
Abstract classes are useful when:

1. Several classes should follow the same structure.

2. You want to enforce certain methods in child classes.

3. You want to prevent incomplete child implementations.

4. You want to provide common functionality to subclasses.

5. You want to create a clear design or contract.

For example:

    Animal
    Payment
    Shape
    Employee
    Vehicle

can all be good candidates for abstract base classes.
"""


# ============================================================
# 27. ABSTRACT CLASSES DO NOT ALWAYS PROVIDE IMPLEMENTATION
# ============================================================

"""
An abstract method can simply contain:

    pass

because its purpose is to define a requirement.

For example:
"""


class Appliance(ABC):

    @abstractmethod
    def turn_on(self):
        pass


"""
The parent class does not need to know exactly how every
appliance turns on.

It simply requires each concrete appliance to implement
turn_on().
"""


class Fan(Appliance):

    def turn_on(self):
        print("Fan is now running.")


class Television(Appliance):

    def turn_on(self):
        print("Television is now on.")


fan_object=Fan()
television_object=Television()

fan_object.turn_on()
television_object.turn_on()


"""
Both classes follow the same contract but have different
implementations.
"""


# ============================================================
# 28. ABSTRACT CLASS CAN HAVE A CONSTRUCTOR
# ============================================================

"""
An abstract class can also have a constructor.

For example:
"""


class Product(ABC):

    def __init__(self,name):
        self.name=name

    @abstractmethod
    def calculate_price(self):
        pass


class Book(Product):

    def calculate_price(self):
        return 500


book_object=Book("Python Programming")

print("Product:",book_object.name)
print("Price:",book_object.calculate_price())


"""
The abstract class provides common initialization.

The child class provides the required specific behavior.
"""


# ============================================================
# 29. ABSTRACT METHODS AND super()
# ============================================================

"""
An abstract class can also contain regular methods that child
classes can reuse.

For example:
"""


class Report(ABC):

    def __init__(self,title):
        self.title=title

    @abstractmethod
    def generate(self):
        pass

    def show_title(self):
        print("Report:",self.title)


class SalesReport(Report):

    def generate(self):
        print("Generating sales report.")


sales_report_object=SalesReport("Monthly Sales")

sales_report_object.show_title()
sales_report_object.generate()


"""
The child class inherits the regular method:

    show_title()

and implements the abstract method:

    generate()

This combination is very common in real-world designs.
"""


# ============================================================
# 30. ABSTRACT CLASS VS CONCRETE CLASS
# ============================================================

"""
A CONCRETE CLASS is a class that can be instantiated.

Example:

    class Dog:
        ...

    dog_object=Dog()

An ABSTRACT CLASS contains one or more abstract methods and
cannot be instantiated until all abstract requirements are
implemented.
"""


# ============================================================
# 31. CONCRETE CLASS EXAMPLE
# ============================================================

class Laptop:

    def start(self):
        print("Laptop started.")


laptop_object=Laptop()

laptop_object.start()


"""
Laptop is a concrete class.

It can directly create objects.
"""


# ============================================================
# 32. ABSTRACT CLASS EXAMPLE
# ============================================================

class Computer(ABC):

    @abstractmethod
    def start(self):
        pass


class Desktop(Computer):

    def start(self):
        print("Desktop computer started.")


desktop_object=Desktop()

desktop_object.start()


"""
Computer is abstract.

Desktop is concrete because it implements start().
"""


# ============================================================
# 33. THE abc MODULE
# ============================================================

"""
The `abc` module is part of Python's standard library.

We commonly import:

    from abc import ABC,abstractmethod

ABC provides the base class used for creating abstract base
classes.

abstractmethod is used as a decorator to mark methods that
subclasses must implement.

The basic pattern is:

    from abc import ABC,abstractmethod


    class Parent(ABC):

        @abstractmethod
        def some_method(self):
            pass


    class Child(Parent):

        def some_method(self):
            ...
"""


# ============================================================
# 34. BASIC ABSTRACT CLASS TEMPLATE
# ============================================================

"""
The general structure looks like this:

    from abc import ABC, abstractmethod


    class Parent(ABC):

        @abstractmethod
        def required_method(self):
            pass


    class Child(Parent):

        def required_method(self):
            # implementation
            pass

The parent defines the requirement.

The child provides the implementation.
"""


# ============================================================
# 35. A PRACTICAL EXAMPLE: SHAPES
# ============================================================

"""
Let's create a slightly more realistic example.

Every shape should be able to calculate its area.

However, the formula depends on the shape.

So we can create an abstract Shape class.
"""


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14159*self.radius*self.radius


class Rectangle(Shape):

    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width


circle_object=Circle(5)
rectangle_object=Rectangle(10,4)

print("Circle area:",circle_object.area())
print("Rectangle area:",rectangle_object.area())


"""
Shape requires:

    area()

Circle and Rectangle provide different implementations.

This is a very common use case for abstract classes.
"""


# ============================================================
# 36. ABSTRACTION + INHERITANCE + POLYMORPHISM
# ============================================================

"""
Abstract classes bring several OOP concepts together.

ABSTRACTION:

    We define the required behavior without specifying every
    implementation detail.

INHERITANCE:

    Child classes inherit from the abstract parent.

POLYMORPHISM:

    Different child classes provide different implementations
    of the same method.

For example:

        Shape
          |
       area()
       /    \
      /      \
   Circle  Rectangle
     |         |
    area()    area()

Each class implements area() differently.
"""


# ============================================================
# 37. ABSTRACT CLASSES PROVIDE A CONTRACT
# ============================================================

"""
The most important concept to remember is that an abstract
class acts like a contract.

For example:

    class Animal(ABC):

        @abstractmethod
        def make_sound(self):
            pass

This means:

    "Any concrete class that inherits from Animal must provide
     make_sound()."

This creates a clear expectation for developers.
"""


# ============================================================
# 38. WHY NOT JUST USE REGULAR INHERITANCE?
# ============================================================

"""
You might wonder:

    "Why do we need abstract classes?
     Why not just use normal inheritance?"

With normal inheritance, a child class can simply inherit a
method from the parent.

There is no requirement that the child provide its own
implementation.

With an abstract class, we can explicitly enforce a rule.

For example:

    Every payment processor must implement pay().

If a developer creates a new payment processor and forgets
pay(), Python will prevent the class from being instantiated.

This can catch design mistakes early.
"""


# ============================================================
# 39. REGULAR INHERITANCE VS ABSTRACT CLASS
# ============================================================

"""
REGULAR INHERITANCE:

    Parent
      |
      ↓
    Child

The child can reuse parent methods.

There is no automatic requirement to implement specific
methods.

ABSTRACT INHERITANCE:

    Abstract Parent
          |
          ↓
        Child

The child inherits the abstract contract.

The child must implement all required abstract methods before
it can be instantiated.
"""


# ============================================================
# 40. ANIMAL EXAMPLE: COMPLETE VERSION
# ============================================================

"""
Let's finish with the main example from this chapter.
"""


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

    def sleep(self):
        print("Animal is sleeping.")


class Dog(Animal):

    def make_sound(self):
        print("Dog says: Woof!")


class Cat(Animal):

    def make_sound(self):
        print("Cat says: Meow!")


class Cow(Animal):

    def make_sound(self):
        print("Cow says: Moo!")


dog_object=Dog()
cat_object=Cat()
cow_object=Cow()

dog_object.make_sound()
dog_object.sleep()

cat_object.make_sound()
cat_object.sleep()

cow_object.make_sound()
cow_object.sleep()


"""
Notice that Animal contains:

    make_sound()

as an abstract method.

It also contains:

    sleep()

as a regular method.

Therefore:

    Dog
    Cat
    Cow

must implement make_sound(), but they automatically inherit
sleep().

This demonstrates that an abstract class can contain both
required behavior and shared behavior.
"""


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. Python provides the `abc` module for creating Abstract Base
   Classes.

2. We commonly import:

       from abc import ABC, abstractmethod

3. ABC is used as the base class for an abstract class.

4. abstractmethod is a decorator used to mark a method as
   abstract.

5. An abstract class is designed to act as a base class.

6. An abstract class containing abstract methods cannot be
   instantiated directly.

7. For example:

       class Animal(ABC):

           @abstractmethod
           def make_sound(self):
               pass

8. Animal defines a requirement:

       make_sound()

9. A concrete child class must implement every inherited
   abstract method before it can be instantiated.

10. Example:

        class Dog(Animal):

            def make_sound(self):
                print("Woof!")

11. If a child class does not implement an abstract method,
    that child class remains abstract.

12. Python will raise a TypeError if we try to instantiate
    that incomplete child class.

13. Abstract classes can contain both:

        abstract methods
        regular methods

14. Regular methods in an abstract class can provide shared
    functionality to child classes.

15. Abstract methods define behavior that child classes are
    required to provide.

16. An abstract class can contain a constructor and instance
    variables.

17. An abstract class can contain multiple abstract methods.

18. A child class must implement all required abstract
    methods before it can become a concrete class.

19. Abstract classes can be thought of as contracts.

20. The parent class defines WHAT a child class must provide.

21. The child class defines HOW that behavior works.

22. Abstract classes work very well with polymorphism.

23. For example:

        Animal
        /    \
       Dog   Cat

    Both classes implement:

        make_sound()

    but each class provides different behavior.

24. Regular inheritance mainly provides code reuse and class
    relationships.

25. Abstract inheritance adds requirements that child classes
    must follow.

26. Regular inheritance:

        "You can inherit this behavior."

27. Abstract inheritance:

        "You must provide this behavior."

28. Abstract classes are useful when several related classes
    should follow the same structure.

29. A common pattern is:

       from abc import ABC, abstractmethod


       class Parent(ABC):

           @abstractmethod
           def required_method(self):
               pass


       class Child(Parent):

           def required_method(self):
               ...

30. Abstract classes are a formal way of implementing
    abstraction in Python.

The main idea to remember is:

    Abstract class
          ↓
    Defines a common contract
          ↓
    Abstract methods
          ↓
    Child classes must implement them
          ↓
    Concrete child objects can be created

In the next chapter, we will learn about Magic Methods
(special methods such as __str__, __len__, __eq__, and others)
and how Python uses them to give objects special behavior.
"""