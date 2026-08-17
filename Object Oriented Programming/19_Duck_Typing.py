"""
DUCK TYPING
"""


# ============================================================
# 1. INTRODUCTION TO DUCK TYPING
# ============================================================

"""
Duck Typing is an important concept in Python.

The idea comes from the famous saying:

    "If it walks like a duck and quacks like a duck,
    then it is a duck."

In programming, this means:

    We often care about what an object can do,
    rather than what class the object belongs to.

For example, suppose a function needs an object that can
speak.

Instead of asking:

    "Is this object a Dog?"

we can simply use:

    object.speak()

If the object has a speak() method, our function can use it.

This is called Duck Typing.
"""


# ============================================================
# 2. A SIMPLE DUCK TYPING EXAMPLE
# ============================================================

"""
Suppose we have two completely different classes:

    Dog
    Robot

They do not have to be related through inheritance.

However, both classes provide a speak() method.

A function can work with either object.
"""


class Dog:

    def speak(self):
        print("Dog says: Woof!")


class Robot:

    def speak(self):
        print("Robot says: Hello!")


def make_it_speak(thing):
    thing.speak()


dog_object=Dog()
robot_object=Robot()

make_it_speak(dog_object)
make_it_speak(robot_object)


"""
Notice that Dog and Robot do not inherit from the same parent
class.

The function:

    make_it_speak()

does not care about their classes.

It only cares that the object has:

    speak()

This is Duck Typing.
"""


# ============================================================
# 3. THE "DUCK" IDEA
# ============================================================

"""
Let's understand the famous saying in programming terms.

Imagine we have a function:

    make_it_speak(thing)

The function does not ask:

    "Are you a duck?"

It simply says:

    "Can you speak?"

If the object can perform:

    speak()

then the function can use it.

So the important question is not:

    What are you?

but:

    What can you do?

This is the basic philosophy behind Duck Typing.
"""


# ============================================================
# 4. DUCK TYPING DOES NOT REQUIRE INHERITANCE
# ============================================================

"""
In traditional inheritance-based programming, we might create
a common parent class.

For example:

        Animal
        /    \
       Dog   Cat

Both Dog and Cat inherit from Animal.

But Duck Typing does not require this relationship.

Two unrelated classes can still work with the same function
as long as they provide the required behavior.
"""


class Teacher:

    def speak(self):
        print("Teacher is explaining the lesson.")


class Parrot:

    def speak(self):
        print("Parrot is talking.")


def start_conversation(speaker):
    speaker.speak()


teacher_object=Teacher()
parrot_object=Parrot()

start_conversation(teacher_object)
start_conversation(parrot_object)


"""
Teacher and Parrot have no inheritance relationship.

However, both provide:

    speak()

Therefore, both can be passed to:

    start_conversation()

This is Duck Typing.
"""


# ============================================================
# 5. PYTHON'S DYNAMIC TYPING
# ============================================================

"""
Python is dynamically typed.

This means that a variable does not have to be permanently
associated with one specific data type.

For example:
"""


value=100

print(value)

value="Python"

print(value)

value=[10,20,30]

print(value)


"""
The same variable name can refer to objects of different types
at different times.

Python determines the type of the object at runtime.

This dynamic nature of Python works naturally with Duck Typing.

Instead of requiring a variable to have a specific declared
type, Python can simply try to use the operation or method
needed by the program.
"""


# ============================================================
# 6. DYNAMIC TYPING VS DUCK TYPING
# ============================================================

"""
Dynamic typing and Duck Typing are related, but they are not
the same thing.

DYNAMIC TYPING:

    Python determines the type of an object at runtime.

DUCK TYPING:

    Python code often focuses on whether an object supports
    the required behavior instead of checking its exact type.

For example:

    number=50
    number="Hello"

is an example of dynamic typing.

While:

    object.speak()

without checking whether object is specifically a Dog is an
example of Duck Typing.
"""


# ============================================================
# 7. DUCK TYPING WITH DIFFERENT CLASSES
# ============================================================

"""
Let's create several unrelated classes that all have a
speak() method.
"""


class Human:

    def speak(self):
        print("Human is speaking.")


class Parrot:

    def speak(self):
        print("Parrot is speaking.")


class Computer:

    def speak(self):
        print("Computer is producing speech.")


def speak_now(speaker):
    speaker.speak()


human_object=Human()
parrot_object=Parrot()
computer_object=Computer()

speak_now(human_object)
speak_now(parrot_object)
speak_now(computer_object)


"""
The function does not check the class.

It simply uses:

    speaker.speak()

As long as the object provides speak(), the function can use it.
"""


# ============================================================
# 8. WHAT IF AN OBJECT DOES NOT HAVE THE REQUIRED METHOD?
# ============================================================

"""
Duck Typing does not mean that every object will work.

The object must provide the behavior that the code expects.

For example, our function expects:

    speak()

Let's create an object that does not have speak().
"""


class Car:

    def drive(self):
        print("Car is driving.")


car_object=Car()

# This would raise an AttributeError:
#
# speak_now(car_object)


"""
Why?

Because Car does not have:

    speak()

Python tries to execute:

    car_object.speak()

but that method does not exist.

The error would be similar to:

    AttributeError:
    'Car' object has no attribute 'speak'

This is normal behavior in Duck Typing.
"""


# ============================================================
# 9. DUCK TYPING IS ABOUT BEHAVIOR
# ============================================================

"""
The important thing is the behavior that an object provides.

For example, suppose we have:

    play_music(device)

The function only needs an object that can:

    play_music()

It does not necessarily matter whether the object is:

    Phone
    Computer
    MusicPlayer
    SmartSpeaker

If the required method exists, the object can be used.
"""


class Phone:

    def play_music(self):
        print("Phone is playing music.")


class Laptop:

    def play_music(self):
        print("Laptop is playing music.")


class SmartSpeaker:

    def play_music(self):
        print("Smart speaker is playing music.")


def start_music(device):
    device.play_music()


phone_object=Phone()
laptop_object=Laptop()
speaker_object=SmartSpeaker()

start_music(phone_object)
start_music(laptop_object)
start_music(speaker_object)


"""
The function only cares about:

    play_music()

This is Duck Typing.
"""


# ============================================================
# 10. DUCK TYPING VS TRADITIONAL INTERFACE-BASED POLYMORPHISM
# ============================================================

"""
In languages such as Java or C++, programmers often use
interfaces or explicit inheritance to define a common
structure.

For example, conceptually:

        Speaker
        /     \
       Dog    Robot

The classes may be required to implement a common interface.

Python can also use inheritance and abstract classes, but
Duck Typing provides another approach.

Instead of saying:

    "You must inherit from Speaker."

we can simply say:

    "You must provide speak()."

This makes the code more flexible.
"""


# ============================================================
# 11. TRADITIONAL APPROACH
# ============================================================

"""
A traditional interface-based design might look conceptually
like this:

        Speaker
        /     \
      Dog    Robot

Both classes implement the Speaker interface.

The exact syntax differs between programming languages.

The important idea is:

    The relationship is explicitly declared.
"""


# ============================================================
# 12. PYTHON DUCK TYPING APPROACH
# ============================================================

"""
With Duck Typing, we can simply write:
"""


def announce(speaker):
    speaker.speak()


"""
There is no requirement that speaker must inherit from a
specific class.

Any object that provides:

    speak()

can be used.

For example:
"""


class NewsReporter:

    def speak(self):
        print("Reporter is giving the news.")


class PodcastHost:

    def speak(self):
        print("Host is recording a podcast.")


reporter_object=NewsReporter()
host_object=PodcastHost()

announce(reporter_object)
announce(host_object)


"""
Neither class needs to inherit from a Speaker class.

They simply provide the required behavior.
"""


# ============================================================
# 13. DUCK TYPING AND POLYMORPHISM
# ============================================================

"""
Duck Typing is closely related to polymorphism.

Polymorphism allows the same operation or method call to work
with different objects.

Duck Typing is one way Python achieves this flexibility.

For example:

    speaker.speak()

can work with:

    Dog
    Human
    Robot
    Parrot

as long as they provide:

    speak()

So we can think of it as:

    Polymorphism
        +
    Focus on behavior
        =
    Duck Typing style
"""


# ============================================================
# 14. DUCK TYPING WITH A LIST
# ============================================================

"""
Different objects can be stored in the same list.

The objects do not have to belong to the same class hierarchy.
"""


class Dog:

    def speak(self):
        print("Dog: Woof!")


class Cat:

    def speak(self):
        print("Cat: Meow!")


class Robot:

    def speak(self):
        print("Robot: Beep!")


speakers = [
    Dog(),
    Cat(),
    Robot()
]


for speaker in speakers:
    speaker.speak()


"""
The loop does not check the class of each object.

It simply calls:

    speaker.speak()

Each object provides its own implementation.
"""


# ============================================================
# 15. A REAL-WORLD EXAMPLE: FILE-LIKE OBJECTS
# ============================================================

"""
Duck Typing is commonly useful when working with objects that
provide similar behavior.

For example, Python code can often work with different
file-like objects if they provide methods such as:

    read()
    write()

The object might be an actual file, an in-memory object, or
another object that provides the same methods.

The code can focus on what the object can do.
"""


class TextDocument:

    def read(self):
        print("Reading text document.")


class MemoryStorage:

    def read(self):
        print("Reading data from memory.")


def read_data(source):
    source.read()


document_object=TextDocument()
memory_object=MemoryStorage()

read_data(document_object)
read_data(memory_object)


"""
Both objects provide:

    read()

Therefore, read_data() can work with both.
"""


# ============================================================
# 16. DUCK TYPING WITH MULTIPLE REQUIRED METHODS
# ============================================================

"""
Sometimes a function needs an object to provide more than one
method.

For example, suppose we have a function that needs:

    open()
    close()
"""


class FileResource:

    def open(self):
        print("File opened.")

    def close(self):
        print("File closed.")


class DatabaseResource:

    def open(self):
        print("Database connection opened.")

    def close(self):
        print("Database connection closed.")


def use_resource(resource):
    resource.open()
    print("Using resource...")
    resource.close()


file_object=FileResource()
database_object=DatabaseResource()

use_resource(file_object)
use_resource(database_object)


"""
The function does not need to know whether the resource is a
file or database.

It only requires two behaviors:

    open()
    close()

This is a practical example of Duck Typing.
"""


# ============================================================
# 17. WHAT DUCK TYPING DOES NOT MEAN
# ============================================================

"""
Duck Typing does NOT mean:

    "Python never cares about types."

Python still knows the type of every object.

For example:
"""


value=25

print(type(value))


"""
Python knows that value is an int.

Duck Typing simply means that code often does not need to
explicitly check the exact type before using an object.
"""


# ============================================================
# 18. TYPE CHECKING VS DUCK TYPING
# ============================================================

"""
Consider two approaches.

APPROACH 1: Explicit type checking

    if isinstance(animal, Dog):
        animal.speak()

This checks whether the object is a Dog.

APPROACH 2: Duck Typing

    animal.speak()

The second approach focuses on what the object can do.
"""


class Dog:

    def speak(self):
        print("Dog says Woof.")


class Cat:

    def speak(self):
        print("Cat says Meow.")


def speak_with_type_check(animal):

    if(isinstance(animal,Dog)):
        animal.speak()
    elif(isinstance(animal,Cat)):
        animal.speak()


def speak_with_duck_typing(animal):

    animal.speak()


dog_object=Dog()
cat_object=Cat()

speak_with_type_check(dog_object)
speak_with_type_check(cat_object)

speak_with_duck_typing(dog_object)
speak_with_duck_typing(cat_object)


"""
The Duck Typing version is usually simpler.

It does not need to know all the possible classes that can
speak.
"""


# ============================================================
# 19. WHY TYPE CHECKING CAN BECOME A PROBLEM
# ============================================================

"""
Imagine we have:

    Dog
    Cat
    Bird
    Robot
    Human
    Alien

and all of them have:

    speak()

If we explicitly check every type, the code can become long:

    if(Dog):
        ...
    elif(Cat):
        ...
    elif(Bird):
        ...
    elif(Robot):
        ...
    ...

With Duck Typing, we can simply write:

    object.speak()

New classes can often be added without changing the existing
function.
"""


# ============================================================
# 20. ADDING A NEW CLASS
# ============================================================

"""
Suppose our existing function is:
"""


def make_announcement(speaker):
    speaker.speak()


"""
Now we create a completely new class.
"""


class Alien:

    def speak(self):
        print("Alien is speaking.")


alien_object=Alien()

make_announcement(alien_object)


"""
We did not change make_announcement().

It automatically works with the new class because Alien
provides:

    speak()

This is one of the major advantages of Duck Typing.
"""


# ============================================================
# 21. DUCK TYPING AND "WHAT CAN YOU DO?"
# ============================================================

"""
A useful way to remember Duck Typing is:

    Don't ask:
        "What type are you?"

    Ask:
        "What can you do?"

For example:

    object.speak()

means that the important requirement is:

    "This object can speak."

The exact class may not matter.
"""


# ============================================================
# 22. DUCK TYPING AND "PYTHONIC" CODE
# ============================================================

"""
Duck Typing is considered Pythonic because it fits Python's
general philosophy of writing simple, flexible, and readable
code.

Instead of unnecessarily checking an object's exact type,
Python code often focuses on the behavior that is actually
needed.

For example:

    def print_message(printer):
        printer.print_data()

This function clearly communicates what it needs:

    An object that can print_data()

It does not need to know the object's exact class.
"""


# ============================================================
# 23. DUCK TYPING CAN REDUCE COUPLING
# ============================================================

"""
Duck Typing can reduce the dependency between different
parts of a program.

Suppose a function requires a specific class:

    def process(document: PDFDocument):
        ...

Now the function is closely connected to PDFDocument.

With Duck Typing:

    def process(document):
        document.read()

The function only depends on the behavior it needs:

    read()

This can make code more flexible.
"""


# ============================================================
# 24. DUCK TYPING DOES NOT ALWAYS MEAN "NO TYPE HINTS"
# ============================================================

"""
Python also supports type hints.

For example, you may see:

    def process(data: SomeType):
        ...

Type hints can improve readability, editor support, and
static analysis.

Duck Typing is about how the code behaves at runtime.

Type hints are a separate feature that can communicate
expected types to developers and tools.

So using type hints does not automatically mean that Duck
Typing cannot be used.
"""


# ============================================================
# 25. DUCK TYPING WITH A SIMPLE PAYMENT EXAMPLE
# ============================================================

"""
Let's create a practical example.

Different payment systems can provide:

    pay()

The processing function does not need to know the exact
payment class.
"""


class CreditCard:

    def pay(self,amount):
        print("Paid",amount,"using credit card.")


class BankTransfer:

    def pay(self,amount):
        print("Paid",amount,"using bank transfer.")


class DigitalWallet:

    def pay(self,amount):
        print("Paid",amount,"using digital wallet.")


def process_payment(payment_method,amount):
    payment_method.pay(amount)


card_object=CreditCard()
transfer_object=BankTransfer()
wallet_object=DigitalWallet()

process_payment(card_object,1500)
process_payment(transfer_object,2200)
process_payment(wallet_object,800)


"""
The classes do not need to inherit from a common Payment
class.

They simply provide:

    pay()

The function uses the behavior it needs.
"""


# ============================================================
# 26. DUCK TYPING VS INHERITANCE
# ============================================================

"""
Inheritance says:

    "This class is a type of that class."

For example:

    Dog is an Animal.

Duck Typing says:

    "I don't necessarily care what type this object is.
     I care whether it provides the behavior I need."

For example:

    "Can this object speak?"

If yes, we can call:

    object.speak()

Both approaches are useful.

Inheritance is useful when classes genuinely share a
parent-child relationship.

Duck Typing is useful when we mainly care about common
behavior.
"""


# ============================================================
# 27. DUCK TYPING VS ABSTRACT INTERFACES
# ============================================================

"""
An abstract interface can explicitly define what methods a
class should provide.

For example, conceptually:

    Speaker
        ↓
    speak()

Classes can then implement that interface.

Duck Typing does not require this explicit relationship.

Instead, Python can simply use:

    object.speak()

if the method exists.

So:

    Interface-based approach
        → Explicit relationship

    Duck Typing
        → Expected behavior
"""


# ============================================================
# 28. WHEN DUCK TYPING IS A GOOD CHOICE
# ============================================================

"""
Duck Typing is useful when:

1. Different objects provide the same behavior.

2. You do not need to know the exact class.

3. You want functions to work with many different objects.

4. You want to reduce unnecessary type checking.

5. You want code that is easy to extend with new classes.

For example:

    def save_data(storage):
        storage.save()

Any suitable object that provides save() can potentially be
used.
"""


class FileStorage:

    def save(self):
        print("Data saved to file.")


class CloudStorage:

    def save(self):
        print("Data saved to cloud.")


def save_data(storage):
    storage.save()


file_storage_object=FileStorage()
cloud_storage_object=CloudStorage()

save_data(file_storage_object)
save_data(cloud_storage_object)


# ============================================================
# 29. WHEN EXPLICIT TYPE CHECKING MAY BE USEFUL
# ============================================================

"""
Duck Typing is useful, but it is not a rule that says:

    "Never check types."

Sometimes the exact type matters.

For example, if different types require completely different
logic, explicit type checking may be appropriate.

Also, some APIs or validation systems may require specific
types.

The important idea is:

    Don't perform type checks unnecessarily.

Choose the approach that makes the code clearer and safer.
"""


# ============================================================
# 30. A COMPLETE EXAMPLE
# ============================================================

"""
Let's combine everything into one example.

We will create several objects that can speak.
They are unrelated classes.

Our function only expects the speak() behavior.
"""


class Teacher:

    def speak(self):
        print("Teacher: Welcome to today's lesson.")


class Student:

    def speak(self):
        print("Student: I have a question.")


class Robot:

    def speak(self):
        print("Robot: System is ready.")


class Parrot:

    def speak(self):
        print("Parrot: Hello!")


def let_them_speak(speaker):
    speaker.speak()


speakers=[
    Teacher(),
    Student(),
    Robot(),
    Parrot()
]


for speaker in speakers:
    let_them_speak(speaker)


"""
Notice the important point:

    Teacher
    Student
    Robot
    Parrot

are different classes.

They do not need to share a parent class.

The only requirement is:

    speak()

This is Duck Typing in a simple and practical form.
"""


# ============================================================
# 31. DUCK TYPING IN ONE SENTENCE
# ============================================================

"""
Duck Typing can be summarized as:

    "If an object supports the behavior your code needs,
    you can use that object."

Or even more simply:

    "Focus on what an object can do, not just what it is."
"""


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. Duck Typing is a Python programming concept based on
   behavior.

2. The famous idea is:

       "If it walks like a duck and quacks like a duck,
       then it is a duck."

3. In programming, this means:

       If an object provides the required behavior,
       we can often use it regardless of its exact class.

4. For example, if a function needs:

       speak()

   it can work with any object that provides speak().

5. The classes do not necessarily need to inherit from a
   common parent.

6. Example:

       class Dog:

           def speak(self):
               ...

       class Robot:

           def speak(self):
               ...

   Both can be used with:

       def make_it_speak(thing):
           thing.speak()

7. Duck Typing is closely related to polymorphism.

8. Polymorphism allows the same operation to work with
   different objects.

9. Duck Typing focuses on the behavior required from those
   objects.

10. Python is dynamically typed, meaning that types are
    determined at runtime.

11. Dynamic typing and Duck Typing are related but are not
    the same thing.

12. Dynamic typing is about when Python determines the type.

13. Duck Typing is about focusing on what an object can do.

14. Traditional interface-based programming often requires
    an explicit relationship between classes.

15. Duck Typing does not require that explicit relationship.

16. Traditional approach:

        "You must implement this interface."

17. Duck Typing approach:

        "If you provide the required behavior, I can use you."

18. Duck Typing can reduce unnecessary type checking.

19. Instead of writing:

        if(isinstance(object, SomeClass)):
            ...

    we can often simply write:

        object.some_method()

20. If the required method does not exist, Python will raise
    an AttributeError when the code tries to call it.

21. Duck Typing can make code more flexible because new
    classes can often be added without changing existing
    functions.

22. Duck Typing is considered Pythonic because it encourages
    simple, flexible, behavior-focused code.

23. A useful mental model is:

        Don't ask:
            "What are you?"

        Ask:
            "What can you do?"

24. Duck Typing does not mean Python does not know object
    types.

25. Python still knows the type of every object.

26. Duck Typing simply means that we often do not need to
    explicitly check the exact type before using an object.

27. Duck Typing and inheritance are both useful, but they
    solve slightly different problems.

        Inheritance:
            Defines a class relationship.

        Duck Typing:
            Focuses on required behavior.

28. Duck Typing is especially useful when several unrelated
    classes provide the same behavior.

The main idea to remember is:

    Same required behavior
            ↓
    Different possible classes
            ↓
    One function can work with them

This is one of the features that makes Python flexible and
expressive.

In the next chapter, we will learn about Abstraction and how
we can focus on what an object should do while hiding the
details of how that behavior is implemented.
"""