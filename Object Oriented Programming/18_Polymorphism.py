"""
POLYMORPHISM
"""

# ============================================================
# 1. INTRODUCTION TO POLYMORPHISM
# ============================================================

"""
Polymorphism is one of the important concepts of Object-Oriented
Programming.

The word "polymorphism" comes from two Greek words:

    poly   → many
    morph  → forms

So, polymorphism means:

    "Many forms"

In programming, polymorphism means that the same method name,
function, or operation can behave differently depending on the
object or data it is working with.

For example, different classes can have a method called:

    make_sound()

A Dog may bark, while a Cat may meow.

The method name is the same:

    make_sound()

but the behavior is different.

This is polymorphism.
"""


# ============================================================
# 2. A SIMPLE REAL-WORLD ANALOGY
# ============================================================

"""
Think about the word "move".

Different things can move in different ways:

    Car       → drives
    Bird      → flies
    Fish      → swims

The action is:

    move()

but its actual behavior depends on the object.

So we can think of:

    move()
       ↓
    many forms

This is the basic idea behind polymorphism.
"""


# ============================================================
# 3. POLYMORPHISM WITH DIFFERENT CLASSES
# ============================================================

"""
Let's create different classes with the same method name.

Each class will provide its own implementation.
"""


class Dog:

    def make_sound(self):
        print("Dog barks.")


class Cat:

    def make_sound(self):
        print("Cat meows.")


class Cow:

    def make_sound(self):
        print("Cow moos.")


dog_object=Dog()
cat_object=Cat()
cow_object=Cow()

dog_object.make_sound()
cat_object.make_sound()
cow_object.make_sound()


"""
All three classes have:

    make_sound()

But each class provides different behavior.

    Dog → bark
    Cat → meow
    Cow → moo

The same method name has different forms of behavior.
"""


# ============================================================
# 4. POLYMORPHISM WITH A FUNCTION
# ============================================================

"""
Polymorphism becomes especially useful when we create a
function that works with different objects.

The function does not need to know the exact class of the
object.

It only needs to know that the object provides the required
method.
"""


class Dog:

    def make_sound(self):
        print("Dog barks.")


class Cat:

    def make_sound(self):
        print("Cat meows.")


def make_animal_sound(animal):
    animal.make_sound()


dog_object=Dog()
cat_object=Cat()

make_animal_sound(dog_object)
make_animal_sound(cat_object)


"""
The function:

    make_animal_sound()

works with both Dog and Cat objects.

It calls:

    animal.make_sound()

For a Dog object:

    Dog.make_sound()

is used.

For a Cat object:

    Cat.make_sound()

is used.

The function does not need separate versions such as:

    make_dog_sound()
    make_cat_sound()

This makes the code simpler and more flexible.
"""


# ============================================================
# 5. THE FUNCTION DOES NOT NEED TO KNOW THE CLASS
# ============================================================

"""
Notice that the function:

    make_animal_sound(animal)

does not check:

    if animal is a Dog:
        ...

or:

    if animal is a Cat:
        ...

It simply calls:

    animal.make_sound()

Python determines which implementation should be used based
on the object.

This is one of the important benefits of polymorphism.
"""


class Bird:

    def make_sound(self):
        print("Bird chirps.")


class Lion:

    def make_sound(self):
        print("Lion roars.")


def play_sound(creature):
    creature.make_sound()


bird_object=Bird()
lion_object=Lion()

play_sound(bird_object)
play_sound(lion_object)


# ============================================================
# 6. POLYMORPHISM WITH METHOD OVERRIDING
# ============================================================

"""
Method overriding is one of the most common ways to achieve
polymorphism in Object-Oriented Programming.

A parent class defines a method.

Child classes override that method with their own
implementations.

For example:

        Animal
        /    \
       /      \
     Dog      Cat

Animal can define:

    make_sound()

Dog and Cat can override it.
"""


class Animal:

    def make_sound(self):
        print("Animal makes a sound.")


class Dog(Animal):

    def make_sound(self):
        print("Dog barks.")


class Cat(Animal):

    def make_sound(self):
        print("Cat meows.")


dog_object=Dog()
cat_object=Cat()

dog_object.make_sound()
cat_object.make_sound()


"""
Both Dog and Cat inherit from Animal.

Both override:

    make_sound()

The method call:

    object.make_sound()

produces different behavior depending on the object.

This is polymorphism through method overriding.
"""


# ============================================================
# 7. ONE FUNCTION, MANY OBJECTS
# ============================================================

"""
We can take the previous example one step further.

We can create one function that works with all Animal
subclasses.
"""


class Animal:

    def make_sound(self):
        print("Animal makes a sound.")


class Dog(Animal):

    def make_sound(self):
        print("Dog barks.")


class Cat(Animal):

    def make_sound(self):
        print("Cat meows.")


class Cow(Animal):

    def make_sound(self):
        print("Cow moos.")


def make_sound(animal):
    animal.make_sound()


dog_object=Dog()
cat_object=Cat()
cow_object=Cow()

make_sound(dog_object)
make_sound(cat_object)
make_sound(cow_object)


"""
The same function:

    make_sound()

works with three different objects.

The function does not need to know whether it received:

    Dog
    Cat
    Cow

It simply expects the object to provide:

    make_sound()

This is a powerful use of polymorphism.
"""


# ============================================================
# 8. POLYMORPHISM WITH A LIST OF OBJECTS
# ============================================================

"""
Polymorphism becomes even more useful when different objects
are stored together in a collection.

We can put different Animal objects inside the same list.
"""


class Dog:

    def make_sound(self):
        print("Dog barks.")


class Cat:

    def make_sound(self):
        print("Cat meows.")


class Cow:

    def make_sound(self):
        print("Cow moos.")


animals=[
    Dog(),
    Cat(),
    Cow()
]


for animal in animals:
    animal.make_sound()


"""
The loop uses the same code:

    animal.make_sound()

But the result changes depending on the current object.

    Dog object → Dog barks
    Cat object → Cat meows
    Cow object → Cow moos

This is a simple and practical example of polymorphism.
"""


# ============================================================
# 9. POLYMORPHISM WITH CLASS METHODS
# ============================================================

"""
Polymorphism can also be seen when child classes override
methods inherited from a parent class.

Consider a payment system.

Different payment classes can have the same method:

    pay()

but each class can implement it differently.
"""


class Payment:

    def pay(self):
        print("Processing payment.")


class CreditCardPayment(Payment):

    def pay(self):
        print("Processing credit card payment.")


class CashPayment(Payment):

    def pay(self):
        print("Processing cash payment.")


class OnlinePayment(Payment):

    def pay(self):
        print("Processing online payment.")


payments=[
    CreditCardPayment(),
    CashPayment(),
    OnlinePayment()
]


for payment in payments:
    payment.pay()


"""
The same method call:

    payment.pay()

produces different behavior.

    CreditCardPayment → credit card payment
    CashPayment       → cash payment
    OnlinePayment     → online payment

This is polymorphism through method overriding.
"""


# ============================================================
# 10. POLYMORPHISM WITH FUNCTIONS
# ============================================================

"""
Polymorphism is not limited to classes.

Python functions can also behave polymorphically because a
function can accept different types of objects or values.

For example, the built-in len() function works with many
different types.
"""


# String
message="Python"

print(len(message))


# List
numbers=[10,20,30,40]

print(len(numbers))


# Dictionary
student_data={
    "name":"Ali",
    "age":20,
    "grade":"A"
}

print(len(student_data))


"""
The same function:

    len()

works with:

    String
    List
    Dictionary

But it calculates the length according to the type of object.

For a string:

    len() → number of characters

For a list:

    len() → number of elements

For a dictionary:

    len() → number of key-value pairs

The same function has different behavior for different
objects.

This is another example of polymorphism.
"""


# ============================================================
# 11. len() WITH DIFFERENT BUILT-IN TYPES
# ============================================================

"""
Let's look at a few more examples.
"""


word="Programming"
items=["Python","Java","C++"]
scores=(85,90,95,80)
unique_numbers={10,20,30}
profile={
    "name":"Hassan",
    "city":"Lahore"
}

print(len(word))
print(len(items))
print(len(scores))
print(len(unique_numbers))
print(len(profile))


"""
The same function:

    len()

works with different built-in objects.

Python knows how to calculate the length for each supported
object.
"""


# ============================================================
# 12. POLYMORPHISM WITH THE + OPERATOR
# ============================================================

"""
The + operator also demonstrates polymorphism.

With numbers, + performs addition.

With strings, + performs concatenation.

The operation is the same:

    +

but the behavior depends on the data type.
"""


first_number=10
second_number=20

print(first_number+second_number)


first_word="Hello"
second_word=" Python"

print(first_word+second_word)


"""
For integers:

    10+20

means:

    addition

For strings:

    "Hello"+" Python"

means:

    concatenation

The same operator behaves differently depending on the
objects involved.
"""


# ============================================================
# 13. POLYMORPHISM WITH print()
# ============================================================

"""
Built-in functions such as print() can also work with many
different types of objects.

For example:
"""


number_value=100
text_value="Python"
list_value=[1,2,3]

print(number_value)
print(text_value)
print(list_value)


"""
print() can work with different types of values.

Python uses the appropriate representation of each object.
"""


# ============================================================
# 14. REAL-WORLD EXAMPLE: SHAPE
# ============================================================

"""
Now let's look at a more practical Object-Oriented example.

Suppose we are building a program that works with shapes.

Different shapes have different formulas for calculating
their area.

For example:

    Rectangle:
        area=length*width

    Circle:
        area= π*radius²

    Triangle:
        area=1/2*base*height

We can define a common method:

    area()

Each shape can then provide its own implementation.
"""


class Shape:

    def area(self):
        print("Calculating area of a shape.")


class Rectangle(Shape):

    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width


class Circle(Shape):

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14159*self.radius*self.radius


class Triangle(Shape):

    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        return 0.5*self.base*self.height


rectangle_object=Rectangle(10,5)
circle_object=Circle(4)
triangle_object=Triangle(8,6)

print("Rectangle area:",rectangle_object.area())
print("Circle area:",circle_object.area())
print("Triangle area:",triangle_object.area())


"""
All three classes have:

    area()

But the calculation is different for each class.

    Rectangle → length*width
    Circle    → π*radius²
    Triangle  → 1/2*base*height

The same method name has different forms.
"""


# ============================================================
# 15. SHAPE POLYMORPHISM WITH A FUNCTION
# ============================================================

"""
We can create a function that works with any shape that
provides an area() method.
"""


def show_area(shape):
    print("Area:",shape.area())


rectangle_object=Rectangle(12,4)
circle_object=Circle(5)
triangle_object=Triangle(10,3)

show_area(rectangle_object)
show_area(circle_object)
show_area(triangle_object)


"""
The show_area() function does not need to know the exact type
of shape.

It simply calls:

    shape.area()

Each object provides its own implementation.

This is a very practical example of polymorphism.
"""


# ============================================================
# 16. SHAPE POLYMORPHISM WITH A LIST
# ============================================================

"""
Different shape objects can also be stored in the same list.
"""


shapes=[
    Rectangle(10,5),
    Circle(3),
    Triangle(8,4)
]


for shape in shapes:
    print("Area:",shape.area())


"""
The same code works for every object:

    shape.area()

Python calls the appropriate implementation based on the
actual object.
"""


# ============================================================
# 17. THE SAME INTERFACE, DIFFERENT IMPLEMENTATION
# ============================================================

"""
A useful way to understand polymorphism is:

    Same interface
        +
    Different implementation

In our Shape example, the common interface is:

    area()

But each class implements it differently.

    Rectangle.area()
    Circle.area()
    Triangle.area()

The code using these objects does not need to know how the
calculation is implemented internally.
"""


# ============================================================
# 18. POLYMORPHISM WITHOUT INHERITANCE
# ============================================================

"""
In Python, polymorphism does not always require inheritance.

Two completely unrelated classes can provide the same method,
and a function can work with both.

For example:
"""


class Email:

    def send(self):
        print("Sending email.")


class SMS:

    def send(self):
        print("Sending SMS.")


def send_message(message):
    message.send()


email_object=Email()
sms_object=SMS()

send_message(email_object)
send_message(sms_object)


"""
Email and SMS do not inherit from a common parent.

However, both provide:

    send()

The function only needs an object that supports send().

This style of polymorphism is closely related to Duck Typing,
which we will study in the next chapter.
"""


# ============================================================
# 19. POLYMORPHISM AND DUCK TYPING
# ============================================================

"""
Python follows a flexible approach to polymorphism.

A famous idea in Python is:

    "If it walks like a duck and quacks like a duck,
     it is a duck."

The idea is that Python often cares about what an object can
do rather than what its exact class is.

For example, if an object has:

    send()

then a function that calls send() can use that object.

We will study this concept in detail in the next chapter.
"""


class Printer:

    def print_data(self):
        print("Printer is printing.")


class Screen:

    def print_data(self):
        print("Screen is displaying data.")


def display_data(device):
    device.print_data()


printer_object=Printer()
screen_object=Screen()

display_data(printer_object)
display_data(screen_object)


# ============================================================
# 20. POLYMORPHISM WITH ANIMAL CLASSES
# ============================================================

"""
Let's look at another complete example.

Every animal can move, but different animals move differently.
"""


class Animal:

    def move(self):
        print("Animal is moving.")


class Bird(Animal):

    def move(self):
        print("Bird is flying.")


class Fish(Animal):

    def move(self):
        print("Fish is swimming.")


class Horse(Animal):

    def move(self):
        print("Horse is running.")


animals=[
    Bird(),
    Fish(),
    Horse()
]


for animal in animals:
    animal.move()


"""
The same method call:

    animal.move()

produces different behavior.

This is polymorphism.
"""


# ============================================================
# 21. WHY POLYMORPHISM IS USEFUL
# ============================================================

"""
Polymorphism provides several benefits.

1. Code becomes more flexible.

2. One function can work with different objects.

3. We can add new classes without changing much existing code.

4. Code becomes easier to maintain.

5. We can write code based on common behavior instead of
   checking every specific class.

For example, our show_area() function works with any object
that provides area().

If we later create a Square class with area(), the same
function can work with it.
"""


class Square(Shape):

    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side*self.side


square_object=Square(6)

show_area(square_object)


"""
We did not need to modify show_area().

It already knows how to work with an object that provides:

    area()

This is one of the major advantages of polymorphism.
"""


# ============================================================
# 22. POLYMORPHISM MAKES CODE EASIER TO EXTEND
# ============================================================

"""
Suppose our program initially supports:

    Rectangle
    Circle
    Triangle

Later, we add:

    Square

We only need to implement area() in Square.

Existing code such as:

    show_area(square_object)

continues to work.

This makes the program easier to extend.
"""


class Square(Shape):

    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side**2


square_object=Square(7)

print("Square area:",square_object.area())


# ============================================================
# 23. POLYMORPHISM VS METHOD OVERRIDING
# ============================================================

"""
Method overriding and polymorphism are closely related, but
they are not exactly the same thing.

METHOD OVERRIDING:

A child class provides a new implementation of a method
inherited from a parent class.

Example:

    class Dog(Animal):

        def make_sound(self):
            ...


POLYMORPHISM:

The same method call can work with different objects and
produce different behavior.

Example:

    animal.make_sound()

Depending on the object, this may call:

    Dog.make_sound()
    Cat.make_sound()
    Cow.make_sound()

So method overriding can be used as a tool to achieve
polymorphic behavior.
"""


# ============================================================
# 24. A COMPLETE POLYMORPHISM EXAMPLE
# ============================================================

"""
Let's combine the concepts into one example.

Different payment methods have the same pay() method.
"""


class Payment:

    def pay(self,amount):
        print("Processing payment of",amount)


class CardPayment(Payment):

    def pay(self,amount):
        print("Paid",amount,"using a credit card.")


class CashPayment(Payment):

    def pay(self,amount):
        print("Paid",amount,"using cash.")


class MobilePayment(Payment):

    def pay(self,amount):
        print("Paid",amount,"using mobile payment.")


def process_payment(payment_method,amount):
    payment_method.pay(amount)


card_object=CardPayment()
cash_object=CashPayment()
mobile_object=MobilePayment()

process_payment(card_object,1000)
process_payment(cash_object,500)
process_payment(mobile_object,750)


"""
The function:

    process_payment()

does not need separate code for:

    CardPayment
    CashPayment
    MobilePayment

It simply calls:

    payment_method.pay(amount)

The actual behavior depends on the object.
"""


# ============================================================
# 25. IMPORTANT IDEA: DON'T CHECK THE TYPE UNNECESSARILY
# ============================================================

"""
Without polymorphism, a programmer might write code like:

    if(type(payment)==CardPayment):
        ...
    elif(type(payment)==CashPayment):
        ...
    elif(type(payment)==MobilePayment):
        ...

This becomes difficult to maintain when more classes are
added.

With polymorphism, we can simply write:

    payment.pay()

Each class handles its own behavior.
"""


# ============================================================
# 26. POLYMORPHISM WITH BUILT-IN FUNCTIONS
# ============================================================

"""
Python's built-in functions are designed to work with many
different types of objects.

This is another place where polymorphism can be observed.

For example:

    len()
    str()
    sum()
    max()
    min()

can work with different objects depending on what those
objects support.
"""


# len() with different objects

name="Python"

numbers=[10, 20, 30]

student={
    "name":"Omar",
    "age":21
}

print(len(name))
print(len(numbers))
print(len(student))


# ============================================================
# 27. str() WITH DIFFERENT OBJECTS
# ============================================================

"""
The str() function can convert different values to their
string representation.
"""


number_value=250
price_value=99.99
items=["Python","OOP","Programming"]

print(str(number_value))
print(str(price_value))
print(str(items))


"""
The same built-in function works with different types of
objects.
"""


# ============================================================
# 28. POLYMORPHISM WITH USER-DEFINED CLASSES
# ============================================================

"""
We can also make our own classes work naturally with Python's
built-in functions by defining appropriate special methods.

For example, __len__() allows an object to work with len().

We will study these special methods in detail later.
"""


class Team:

    def __init__(self,members):
        self.members=members

    def __len__(self):
        return len(self.members)


team_object=Team([
    "Ali",
    "Sara",
    "Hamza",
    "Ayesha"
])

print(len(team_object))


"""
Because Team defines:

    __len__()

Python knows how to calculate:

    len(team_object)

This shows how Python's built-in functions can work with
user-defined objects too.
"""


# ============================================================
# 29. POLYMORPHISM IN A SINGLE LOOP
# ============================================================

"""
One of the simplest ways to recognize polymorphism is to look
for code like this:

    for object in objects:
        object.some_method()

The objects may be different classes, but they provide the
same method.
"""


class PDFReport:

    def generate(self):
        print("Generating PDF report.")


class ExcelReport:

    def generate(self):
        print("Generating Excel report.")


class HTMLReport:

    def generate(self):
        print("Generating HTML report.")


reports=[
    PDFReport(),
    ExcelReport(),
    HTMLReport()
]


for report in reports:
    report.generate()


"""
The loop does not need to know the specific report type.

It only needs each object to provide:

    generate()
"""


# ============================================================
# 30. IMPORTANT POINTS TO REMEMBER
# ============================================================

"""
Polymorphism can appear in several forms:

    1. Different classes having the same method name.

    2. A parent method being overridden by child classes.

    3. One function working with different objects.

    4. Built-in functions working with different data types.

    5. Operators behaving differently depending on the
       objects involved.

The common idea is:

    Same interface
        +
    Different behavior
"""


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. Polymorphism means "many forms."

2. In programming, polymorphism means that the same method,
   function, or operation can behave differently depending
   on the object or data.

3. Different classes can define the same method name with
   different implementations.

4. Example:

       Dog.make_sound()
       Cat.make_sound()

   Both use:

       make_sound()

   but their behavior is different.

5. A function can work with different objects if those objects
   provide the required method.

6. Example:

       def make_sound(animal):
           animal.make_sound()

7. Method overriding is a common way to achieve polymorphic
   behavior.

8. Child classes can override a method inherited from a
   parent class.

9. A single function can work with objects of different
   classes.

10. Polymorphism can also be seen in Python's built-in
    functions.

11. For example, len() works with:

        strings
        lists
        tuples
        sets
        dictionaries
        many user-defined objects

12. The + operator also behaves differently depending on the
    objects involved.

13. For numbers:

        10+20

    performs addition.

14. For strings:

        "Hello"+" Python"

    performs concatenation.

15. A real-world example is a Shape hierarchy.

16. Different shapes can provide the same method:

        area()

17. Rectangle.area() calculates a rectangle's area.

18. Circle.area() calculates a circle's area.

19. Triangle.area() calculates a triangle's area.

20. A function such as:

        def show_area(shape):
            print(shape.area())

    can work with all of them.

21. Polymorphism reduces the need for repeated type checking.

22. Polymorphism makes code more flexible and easier to extend.

23. A useful mental model is:

        Same method call
               ↓
        Different objects
               ↓
        Different behavior

24. Another useful way to remember it is:

        Same interface
             +
        Different implementation
             =
        Polymorphic behavior

25. Python can also support polymorphism without inheritance.
    If different objects provide the same required behavior,
    the same function can often work with all of them.

This last idea leads naturally to Duck Typing.

In the next chapter, we will learn about Duck Typing and
understand Python's approach of focusing on what an object can
do rather than only checking what class the object belongs to.
"""