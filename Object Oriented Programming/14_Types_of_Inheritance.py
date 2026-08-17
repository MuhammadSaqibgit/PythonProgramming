"""
TYPES OF INHERITANCE
"""


# ============================================================
# 1. INTRODUCTION
# ============================================================

"""
Inheritance allows one class to acquire attributes and methods
from another class.

Python supports several common types of inheritance:

    1. Single Inheritance
    2. Multiple Inheritance
    3. Multilevel Inheritance
    4. Hierarchical Inheritance
    5. Hybrid Inheritance

The type of inheritance depends on the relationship between
the parent and child classes.

In this chapter, we will look at each type with a simple
diagram and example.
"""


# ============================================================
# 2. SINGLE INHERITANCE
# ============================================================

"""
Single inheritance means that one child class inherits from
one parent class.

Diagram:

        Parent
          |
          ↓
        Child

Example:

        Animal
          |
          ↓
          Dog

Dog inherits from Animal.
"""


class Animal:

    def eat(self):
        print("Animal is eating.")


class Dog(Animal):

    def bark(self):
        print("Dog is barking.")


dog_object=Dog()

dog_object.eat()
dog_object.bark()


"""
Here:

    Animal → Parent class
    Dog    → Child class

Dog inherits the eat() method from Animal and also has its
own bark() method.

This is called single inheritance because there is only one
parent class.
"""


# ============================================================
# 3. ANOTHER SINGLE INHERITANCE EXAMPLE
# ============================================================

"""
Diagram:

        Vehicle
           |
           ↓
          Car
"""


class Vehicle:

    def start(self):
        print("Vehicle has started.")


class Car(Vehicle):

    def drive(self):
        print("Car is driving.")


car_object=Car()

car_object.start()
car_object.drive()


# ============================================================
# 4. MULTIPLE INHERITANCE
# ============================================================

"""
Multiple inheritance means that one child class inherits from
more than one parent class.

Diagram:

        Parent A       Parent B
             \           /
              \         /
               ↓       ↓
                 Child

Example:

        Writer       Speaker
             \       /
              \     /
              Person

A class can inherit from multiple classes by writing the
parent classes inside the parentheses.

Syntax:

    class Child(ParentA, ParentB):
        pass
"""


class Writer:

    def write(self):
        print("Writing content.")


class Speaker:

    def speak(self):
        print("Speaking to the audience.")


class Presenter(Writer,Speaker):

    def present(self):
        print("Giving a presentation.")


presenter_object=Presenter()

presenter_object.write()
presenter_object.speak()
presenter_object.present()


"""
Here:

    Writer    → Parent class
    Speaker   → Parent class
    Presenter → Child class

Presenter inherits methods from both Writer and Speaker.

This is called multiple inheritance.
"""


# ============================================================
# 5. ANOTHER MULTIPLE INHERITANCE EXAMPLE
# ============================================================

"""
Diagram:

        Camera       GPS
           \         /
            \       /
             ↓     ↓
             Smartphone
"""


class Camera:

    def take_photo(self):
        print("Taking a photo.")


class GPS:

    def find_location(self):
        print("Finding current location.")


class Smartphone(Camera,GPS):

    def make_call(self):
        print("Making a phone call.")


phone_object=Smartphone()

phone_object.take_photo()
phone_object.find_location()
phone_object.make_call()


"""
The Smartphone class gets functionality from both Camera
and GPS.

Multiple inheritance is useful when a class genuinely needs
functionality from multiple parent classes.
"""


# ============================================================
# 6. MULTILEVEL INHERITANCE
# ============================================================

"""
Multilevel inheritance means that inheritance happens through
multiple levels.

A class inherits from another class, and a third class inherits
from that child class.

Diagram:

        Grandparent
             |
             ↓
          Parent
             |
             ↓
           Child

Example:

        Animal
           |
           ↓
        Mammal
           |
           ↓
           Dog
"""


class Animal:

    def eat(self):
        print("Animal is eating.")


class Mammal(Animal):

    def walk(self):
        print("Mammal is walking.")


class Dog(Mammal):

    def bark(self):
        print("Dog is barking.")


dog_object=Dog()

dog_object.eat()
dog_object.walk()
dog_object.bark()


"""
Dog inherits from Mammal.

Mammal inherits from Animal.

Therefore, Dog can access methods from both Mammal and
Animal.

The inheritance chain is:

    Animal
       ↓
    Mammal
       ↓
      Dog
"""


# ============================================================
# 7. ANOTHER MULTILEVEL INHERITANCE EXAMPLE
# ============================================================

"""
Diagram:

        Person
          |
          ↓
       Employee
          |
          ↓
       Manager
"""


class Person:

    def introduce(self):
        print("I am a person.")


class Employee(Person):

    def work(self):
        print("Employee is working.")


class Manager(Employee):

    def manage(self):
        print("Manager is managing the team.")


manager_object=Manager()

manager_object.introduce()
manager_object.work()
manager_object.manage()


"""
Manager gets:

    introduce() from Person
    work()      from Employee
    manage()    from Manager
"""


# ============================================================
# 8. HIERARCHICAL INHERITANCE
# ============================================================

"""
Hierarchical inheritance means that multiple child classes
inherit from the same parent class.

Diagram:

             Parent
            /      \
           /        \
       Child A     Child B

Example:

             Animal
             /    \
            /      \
          Dog      Cat
"""


class Animal:

    def eat(self):
        print("Animal is eating.")


class Dog(Animal):

    def bark(self):
        print("Dog is barking.")


class Cat(Animal):

    def meow(self):
        print("Cat is meowing.")


dog_object=Dog()
cat_object=Cat()

dog_object.eat()
dog_object.bark()

cat_object.eat()
cat_object.meow()


"""
Here:

    Animal → Parent
    Dog    → Child
    Cat    → Child

Both Dog and Cat inherit the common eat() method from Animal.

This is called hierarchical inheritance because one parent
has multiple child classes.
"""


# ============================================================
# 9. ANOTHER HIERARCHICAL INHERITANCE EXAMPLE
# ============================================================

"""
Diagram:

             Employee
            /        \
           /          \
      Developer      Designer
"""


class Employee:

    def clock_in(self):
        print("Employee clocked in.")


class Developer(Employee):

    def write_code(self):
        print("Developer is writing code.")


class Designer(Employee):

    def create_design(self):
        print("Designer is creating a design.")


developer_object=Developer()
designer_object=Designer()

developer_object.clock_in()
developer_object.write_code()

designer_object.clock_in()
designer_object.create_design()


"""
Both Developer and Designer inherit the common functionality
from Employee.

Each child can also define its own specific functionality.
"""


# ============================================================
# 10. HYBRID INHERITANCE
# ============================================================

"""
Hybrid inheritance is a combination of two or more types of
inheritance.

It can combine:

    - Multiple inheritance
    - Multilevel inheritance
    - Hierarchical inheritance
    - Single inheritance

There is no single fixed structure for hybrid inheritance.

The structure depends on how different inheritance patterns
are combined.

A simple example:

                 Person
                /      \
               /        \
          Student      Employee
               \        /
                \      /
                 ↓    ↓
               Intern

This structure combines hierarchical inheritance and
multiple inheritance.

Person is the parent of both Student and Employee.

Intern inherits from both Student and Employee.
"""


class Person:

    def introduce(self):
        print("I am a person.")


class Student(Person):

    def study(self):
        print("Student is studying.")


class Employee(Person):

    def work(self):
        print("Employee is working.")


class Intern(Student,Employee):

    def train(self):
        print("Intern is training.")


intern_object=Intern()

intern_object.introduce()
intern_object.study()
intern_object.work()
intern_object.train()


"""
The structure contains two inheritance patterns:

Hierarchical:

             Person
             /    \
            /      \
       Student    Employee

Multiple:

       Student     Employee
            \       /
             \     /
             Intern

Together, these form a hybrid inheritance structure.
"""


# ============================================================
# 11. HYBRID INHERITANCE - ANOTHER EXAMPLE
# ============================================================

"""
Let's look at another simple structure.

Diagram:

                  Device
                 /      \
                /        \
             Phone      Computer
                \        /
                 \      /
                SmartDevice

Device is the parent of Phone and Computer.

SmartDevice inherits from both Phone and Computer.

This combines hierarchical and multiple inheritance.
"""


class Device:

    def power_on(self):
        print("Device is powered on.")


class Phone(Device):

    def make_call(self):
        print("Making a phone call.")


class Computer(Device):

    def run_program(self):
        print("Running a program.")


class SmartDevice(Phone,Computer):

    def connect_to_internet(self):
        print("Connecting to the internet.")


smart_device_object=SmartDevice()

smart_device_object.power_on()
smart_device_object.make_call()
smart_device_object.run_program()
smart_device_object.connect_to_internet()


# ============================================================
# 12. COMPARING ALL TYPES
# ============================================================

"""
The five common types can be remembered using their diagrams.

1. SINGLE INHERITANCE

       Parent
          |
          ↓
        Child


2. MULTIPLE INHERITANCE

       Parent A     Parent B
            \         /
             \       /
              Child


3. MULTILEVEL INHERITANCE

       Grandparent
            |
            ↓
         Parent
            |
            ↓
          Child


4. HIERARCHICAL INHERITANCE

             Parent
             /    \
            /      \
        Child A   Child B


5. HYBRID INHERITANCE

       Combination of two or more
       inheritance patterns.
"""


# ============================================================
# 13. SINGLE INHERITANCE - QUICK EXAMPLE
# ============================================================

class Parent:

    def parent_method(self):
        print("Parent method.")


class Child(Parent):

    def child_method(self):
        print("Child method.")


child_object=Child()

child_object.parent_method()
child_object.child_method()


# ============================================================
# 14. MULTIPLE INHERITANCE - QUICK EXAMPLE
# ============================================================

class FirstParent:

    def first_method(self):
        print("First parent method.")


class SecondParent:

    def second_method(self):
        print("Second parent method.")


class MultipleChild(FirstParent,SecondParent):

    def child_method(self):
        print("Child method.")


multiple_child_object=MultipleChild()

multiple_child_object.first_method()
multiple_child_object.second_method()
multiple_child_object.child_method()


# ============================================================
# 15. MULTILEVEL INHERITANCE - QUICK EXAMPLE
# ============================================================

class GrandParent:

    def grandparent_method(self):
        print("Grandparent method.")


class ParentClass(GrandParent):

    def parent_method(self):
        print("Parent method.")


class ChildClass(ParentClass):

    def child_method(self):
        print("Child method.")


child_record=ChildClass()

child_record.grandparent_method()
child_record.parent_method()
child_record.child_method()


# ============================================================
# 16. HIERARCHICAL INHERITANCE - QUICK EXAMPLE
# ============================================================

class BaseVehicle:

    def start(self):
        print("Vehicle started.")


class Car(BaseVehicle):

    def drive(self):
        print("Car is driving.")


class Bike(BaseVehicle):

    def ride(self):
        print("Bike is being ridden.")


car_record=Car()
bike_record=Bike()

car_record.start()
car_record.drive()

bike_record.start()
bike_record.ride()


# ============================================================
# 17. HYBRID INHERITANCE - QUICK EXAMPLE
# ============================================================

class BasePerson:

    def introduce(self):
        print("Introducing myself.")


class Student(BasePerson):

    def study(self):
        print("Studying.")


class Worker(BasePerson):

    def work(self):
        print("Working.")


class WorkingStudent(Student,Worker):

    def attend_class(self):
        print("Attending class.")


working_student_object=WorkingStudent()

working_student_object.introduce()
working_student_object.study()
working_student_object.work()
working_student_object.attend_class()


# ============================================================
# 18. IMPORTANT NOTE ABOUT MULTIPLE INHERITANCE
# ============================================================

"""
Multiple inheritance can become more complicated when two
parent classes contain methods with the same name.

For example:

        Parent A      Parent B
             \          /
              \        /
               Child

What happens if both Parent A and Parent B define a method
with the same name?

Python needs a rule to decide which method should be used.

Python uses the Method Resolution Order (MRO) to determine
the order in which classes are searched.

We will study MRO in detail in the next chapter.
"""


class ParentA:

    def show(self):
        print("Parent A")


class ParentB:

    def show(self):
        print("Parent B")


class Child(ParentA,ParentB):
    pass


child_object=Child()

child_object.show()


"""
The method from ParentA is used here because ParentA appears
before ParentB in the inheritance list.

The exact rules used by Python are part of Method Resolution
Order, which will be covered in the next chapter.
"""


# ============================================================
# 19. SUMMARY
# ============================================================

"""
Important points:

1. Inheritance allows a class to reuse functionality from
   another class.

2. Python supports several common types of inheritance.

3. SINGLE INHERITANCE:

       One child inherits from one parent.

       Parent
          |
          ↓
        Child

4. MULTIPLE INHERITANCE:

       One child inherits from multiple parents.

       Parent A     Parent B
            \         /
             \       /
              Child

5. MULTILEVEL INHERITANCE:

       Inheritance occurs through multiple levels.

       Grandparent
            |
            ↓
         Parent
            |
            ↓
          Child

6. HIERARCHICAL INHERITANCE:

       Multiple children inherit from one parent.

             Parent
             /    \
            /      \
        Child A   Child B

7. HYBRID INHERITANCE:

       A combination of two or more inheritance types.

8. Single inheritance is the simplest form of inheritance.

9. Multiple inheritance allows one class to inherit from
   multiple parent classes.

10. Multilevel inheritance creates an inheritance chain.

11. Hierarchical inheritance allows multiple child classes
    to share one parent class.

12. Hybrid inheritance combines different inheritance
    structures.

13. Multiple inheritance can create situations where two
    parent classes provide methods with the same name.

14. Python uses Method Resolution Order (MRO) to determine
    which method should be used.

15. MRO will be studied in detail in the next chapter.

A simple way to remember:

    Single
        One parent → One child

    Multiple
        Multiple parents → One child

    Multilevel
        Parent → Child → Grandchild

    Hierarchical
        One parent → Multiple children

    Hybrid
        Combination of inheritance types

In the next chapter, we will learn about Method Resolution
Order (MRO) and how Python decides which method to use when
multiple classes are involved.
"""