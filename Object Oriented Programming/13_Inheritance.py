"""
INHERITANCE
"""


# ============================================================
# 1. INTRODUCTION TO INHERITANCE
# ============================================================

"""
Inheritance is an important concept in Object-Oriented
Programming.

Inheritance allows one class to acquire the attributes and
methods of another class.

The class that provides the existing functionality is called
the parent class, base class, or super class.

The class that inherits from it is called the child class,
derived class, or sub class.

In simple words:

    Parent class
          ↓
    Child class

The child class can reuse functionality from the parent class
and can also add its own functionality.

Inheritance is mainly useful for:

    - Code reuse
    - Extending existing classes
    - Creating relationships between classes
"""


# ============================================================
# 2. WHY DO WE NEED INHERITANCE?
# ============================================================

"""
Suppose we have two classes:

    Dog
    Cat

Both animals can have:

    name
    age

Both animals can also perform an action such as:

    eat()

If we create everything separately, we may have to write the
same code in both classes.

Inheritance allows us to put common functionality in a
parent class and reuse it in child classes.
"""


# ============================================================
# 3. WITHOUT INHERITANCE
# ============================================================

"""
Here is an example without inheritance.

Notice that both classes contain similar code.
"""


class Dog:

    def __init__(self,name):
        self.name=name

    def eat(self):
        print(self.name,"is eating.")


class Cat:

    def __init__(self,name):
        self.name=name

    def eat(self):
        print(self.name,"is eating.")


dog_object=Dog("Buddy")
cat_object=Cat("Luna")

dog_object.eat()
cat_object.eat()


"""
The code works, but the same functionality has been repeated.

Inheritance can help us place the common functionality in
one parent class.
"""


# ============================================================
# 4. PARENT AND CHILD CLASSES
# ============================================================

"""
Let's create an Animal class.

Animal will contain functionality common to animals.

Dog and Cat can then inherit from Animal.

Animal:
    Parent class

Dog:
    Child class

Cat:
    Child class
"""


class Animal:

    def eat(self):
        print("The animal is eating.")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog_object=Dog()
cat_object=Cat()

dog_object.eat()
cat_object.eat()


# ============================================================
# 5. BASIC INHERITANCE SYNTAX
# ============================================================

"""
The basic syntax for inheritance is:

    class Child(Parent):
        # child class body

For example:

    class Dog(Animal):
        pass

This means:

    Dog inherits from Animal.

The child class can use functionality provided by the parent
class.
"""


class Vehicle:

    def start(self):
        print("Vehicle has started.")


class Car(Vehicle):
    pass


car_object=Car()

car_object.start()


# ============================================================
# 6. PARENT CLASS
# ============================================================

"""
The parent class contains common attributes and methods that
can be reused by its child classes.

A parent class can also be called:

    Base class
    Super class

All three terms refer to the class being inherited from.
"""


class Person:

    def introduce(self):
        print("Hello, I am a person.")


class Student(Person):
    pass


student_object=Student()

student_object.introduce()


# ============================================================
# 7. CHILD CLASS
# ============================================================

"""
The child class inherits from the parent class.

A child class can also be called:

    Derived class
    Sub class

The child class can use inherited attributes and methods
without defining them again.
"""


class Employee(Person):

    def work(self):
        print("The employee is working.")


employee_object=Employee()

employee_object.introduce()
employee_object.work()


# ============================================================
# 8. ACCESSING PARENT CLASS METHODS
# ============================================================

"""
A child object can directly call a method inherited from its
parent class.

For example:

    employee_object.introduce()

The introduce() method is defined in Person, not Employee.

Python searches the child class first.

If it does not find the method there, it looks in the parent
class.
"""


class Teacher:

    def teach(self):
        print("Teacher is teaching.")


class MathTeacher(Teacher):

    def solve_problem(self):
        print("Math teacher is solving a problem.")


math_teacher=MathTeacher()

math_teacher.teach()
math_teacher.solve_problem()


# ============================================================
# 9. INHERITING ATTRIBUTES
# ============================================================

"""
A child class can also inherit attributes created by the
parent class.

The parent class can define common data that every child
object should have.
"""


class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_person(self):
        print("Name:",self.name)
        print("Age:",self.age)


class Student(Person):
    pass


student_record=Student("Ayesha",20)

student_record.show_person()


# ============================================================
# 10. ADDING NEW ATTRIBUTES IN THE CHILD CLASS
# ============================================================

"""
A child class is not limited to the functionality of the
parent class.

It can add new attributes and methods of its own.

This is one of the important benefits of inheritance.

The child gets existing functionality from the parent and
can add new functionality when needed.
"""


class Person:

    def __init__(self,name):
        self.name=name

    def introduce(self):
        print("My name is",self.name)


class Student(Person):

    def study(self):
        print(self.name,"is studying.")


student_object=Student("Hassan")

student_object.introduce()
student_object.study()


# ============================================================
# 11. ADDING NEW METHODS IN A CHILD CLASS
# ============================================================

"""
A child class can add methods that do not exist in the parent
class.

This is called extending the parent class.

The child class reuses existing functionality and adds
something new.
"""


class Employee:

    def work(self):
        print("Employee is working.")


class Developer(Employee):

    def write_code(self):
        print("Developer is writing code.")


developer_object=Developer()

developer_object.work()
developer_object.write_code()


# ============================================================
# 12. EXTENDING A PARENT CLASS
# ============================================================

"""
Extending means adding new functionality to the child class
while keeping the functionality inherited from the parent.

For example:

Parent:
    work()

Child:
    work()
    write_code()

The child has more functionality than the parent.
"""


class Worker:

    def work(self):
        print("Worker is working.")


class Programmer(Worker):

    def write_program(self):
        print("Programmer is writing a program.")


programmer_object=Programmer()

programmer_object.work()
programmer_object.write_program()


# ============================================================
# 13. OVERRIDING A METHOD
# ============================================================

"""
A child class can define a method with the same name as a
method in the parent class.

This is called method overriding.

When the method is called using the child object, Python uses
the child class's version of the method.
"""


class Animal:

    def make_sound(self):
        print("Animal makes a sound.")


class Dog(Animal):

    def make_sound(self):
        print("Dog barks.")


animal_object=Animal()
dog_object=Dog()

animal_object.make_sound()
dog_object.make_sound()


# ============================================================
# 14. OVERRIDING VS EXTENDING
# ============================================================

"""
Overriding:

The child replaces the behavior of a parent method by
providing its own implementation.

Example:

    Parent:
        make_sound()

    Child:
        make_sound()

Both methods have the same name.

Extending:

The child keeps the inherited functionality and adds new
functionality.

Example:

    Parent:
        eat()

    Child:
        eat()
        play()

Both concepts are useful in inheritance.
"""


# ============================================================
# 15. OVERRIDING WITH A DIFFERENT IMPLEMENTATION
# ============================================================

class Vehicle:

    def move(self):
        print("Vehicle is moving.")


class Bicycle(Vehicle):

    def move(self):
        print("Bicycle is moving using pedals.")


class Boat(Vehicle):

    def move(self):
        print("Boat is moving through water.")


bicycle_object=Bicycle()
boat_object=Boat()

bicycle_object.move()
boat_object.move()


# ============================================================
# 16. USING PARENT CLASS __init__()
# ============================================================

"""
When a child class has its own __init__() method, the parent's
__init__() method is not automatically called.

If we want to initialize the parent class's attributes, we
need to call the parent constructor.

One common way is to use:

    super()

We will study super() in detail in a later chapter.

For now, we only need the basic idea.
"""


class Person:

    def __init__(self,name):
        self.name=name


class Student(Person):

    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade


student_record=Student("Noor","A")

print("Name:",student_record.name)
print("Grade:",student_record.grade)


# ============================================================
# 17. ACCESSING PARENT ATTRIBUTES
# ============================================================

"""
If the parent class creates an attribute, the child object can
normally access that attribute.

For example:

Person creates:

    self.name

Student inherits from Person.

Therefore:

    student_object.name

is available.
"""


class Person:

    def __init__(self,name):
        self.name=name


class Teacher(Person):

    def show_name(self):
        print("Teacher Name:",self.name)


teacher_object=Teacher("Mariam")

teacher_object.show_name()


# ============================================================
# 18. ACCESSING PARENT METHODS THROUGH THE CHILD
# ============================================================

"""
A child object can use inherited methods exactly like methods
defined in the child class.

This is one of the main reasons inheritance is useful.

We define common behavior once in the parent class and reuse
it in multiple child classes.
"""


class Animal:

    def eat(self):
        print("Eating food.")

    def sleep(self):
        print("Sleeping.")


class Dog(Animal):

    def bark(self):
        print("Barking.")


dog_object=Dog()

dog_object.eat()
dog_object.sleep()
dog_object.bark()


# ============================================================
# 19. MULTIPLE CHILD CLASSES
# ============================================================

"""
A single parent class can have many child classes.

For example:

            Animal
           /      \
         Dog      Cat

Both Dog and Cat can reuse common functionality from Animal.
"""


class Animal:

    def eat(self):
        print("Eating.")


class Dog(Animal):

    def bark(self):
        print("Barking.")


class Cat(Animal):

    def meow(self):
        print("Meowing.")


dog_object=Dog()
cat_object=Cat()

dog_object.eat()
dog_object.bark()

cat_object.eat()
cat_object.meow()


# ============================================================
# 20. CODE REUSE
# ============================================================

"""
One of the main benefits of inheritance is code reuse.

Suppose five different classes need the same method.

Instead of writing the same method five times, we can put it
in a parent class and let the child classes inherit it.

This can reduce duplicated code.
"""


class Employee:

    def clock_in(self):
        print("Employee clocked in.")

    def clock_out(self):
        print("Employee clocked out.")


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


# ============================================================
# 21. isinstance()
# ============================================================

"""
The isinstance() function checks whether an object is an
instance of a particular class.

Syntax:

    isinstance(object,ClassName)

It returns:

    True
    or
    False
"""


class Animal:
    pass


class Dog(Animal):
    pass


dog_object=Dog()

print(isinstance(dog_object,Dog))
print(isinstance(dog_object,Animal))


"""
Both results are True.

Why?

dog_object is directly an instance of Dog.

Because Dog inherits from Animal, dog_object is also considered
an instance of Animal.
"""


# ============================================================
# 22. isinstance() WITH DIFFERENT OBJECTS
# ============================================================

class Vehicle:
    pass


class Car(Vehicle):
    pass


class Bicycle(Vehicle):
    pass


car_object=Car()
bicycle_object=Bicycle()

print(isinstance(car_object,Car))
print(isinstance(car_object,Vehicle))

print(isinstance(bicycle_object,Bicycle))
print(isinstance(bicycle_object,Vehicle))

print(isinstance(car_object,Bicycle))


# ============================================================
# 23. issubclass()
# ============================================================

"""
The issubclass() function checks whether one class is a
subclass of another class.

Syntax:

    issubclass(ChildClass,ParentClass)

It returns:

    True
    or
    False
"""


class Animal:
    pass


class Dog(Animal):
    pass


print(issubclass(Dog,Animal))
print(issubclass(Animal,Dog))


"""
The first result is True because Dog inherits from Animal.

The second result is False because Animal does not inherit
from Dog.
"""


# ============================================================
# 24. isinstance() VS issubclass()
# ============================================================

"""
isinstance():

    Checks an object.

Example:

    isinstance(dog_object,Dog)

issubclass():

    Checks classes.

Example:

    issubclass(Dog,Animal)

Simple way to remember:

    isinstance()
        → object

    issubclass()
        → class
"""


class Person:
    pass


class Student(Person):
    pass


student_object=Student()

print(isinstance(student_object,Student))
print(isinstance(student_object,Person))

print(issubclass(Student,Person))
print(issubclass(Student,object))


# ============================================================
# 25. EVERY CLASS ULTIMATELY INHERITS FROM object
# ============================================================

"""
In Python, classes ultimately inherit from the built-in
object class.

For example:

    class Student:
        pass

is conceptually related to object.

Therefore:

    issubclass(Student,object)

returns True.
"""


class Student:
    pass


print(issubclass(Student,object))


# ============================================================
# 26. SIMPLE REAL-WORLD EXAMPLE
# ============================================================

"""
Consider a company.

Different employees may have common information:

    name
    employee_id

They may also have common behavior:

    show_details()

A Developer and a Manager can inherit these common features
from an Employee class.

Then each child class can add its own behavior.
"""


class Employee:

    def __init__(self,name,employee_id):
        self.name=name
        self.employee_id=employee_id

    def show_details(self):
        print("Name:",self.name)
        print("Employee ID:",self.employee_id)


class Developer(Employee):

    def write_code(self):
        print(self.name,"is writing code.")


class Manager(Employee):

    def manage_team(self):
        print(self.name,"is managing the team.")


developer_record=Developer("Ali",101)
manager_record=Manager("Sara",102)

developer_record.show_details()
developer_record.write_code()

print()

manager_record.show_details()
manager_record.manage_team()


# ============================================================
# 27. INHERITANCE RELATIONSHIP
# ============================================================

"""
Inheritance represents an "is-a" relationship.

For example:

    Dog is an Animal.
    Car is a Vehicle.
    Student is a Person.
    Developer is an Employee.

If the statement makes sense, inheritance may be appropriate.

This is an important idea when deciding whether one class
should inherit from another.
"""


class Animal:
    pass


class Dog(Animal):
    pass


dog_object=Dog()

print(
    "Dog is an Animal:",
    isinstance(dog_object,Animal)
)


# ============================================================
# 28. EXTENDING A PARENT CLASS
# ============================================================

"""
A child class can inherit existing functionality and add new
functionality.

This is called extending the parent class.

The child does not need to rewrite the inherited methods.
"""


class Person:

    def introduce(self):
        print("Hello, my name is a person.")


class Student(Person):

    def study(self):
        print("I am studying.")


student_object=Student()

student_object.introduce()
student_object.study()


# ============================================================
# 29. OVERRIDING A PARENT METHOD
# ============================================================

"""
A child class can also replace the behavior of an inherited
method by defining a method with the same name.
"""


class Animal:

    def move(self):
        print("Animal is moving.")


class Fish(Animal):

    def move(self):
        print("Fish is swimming.")


fish_object=Fish()

fish_object.move()


# ============================================================
# 30. A CHILD CAN BOTH OVERRIDE AND EXTEND
# ============================================================

"""
A child class can override an inherited method and also add
completely new methods.

For example:

Parent:
    introduce()

Child:
    introduce()     → overridden
    study()         → new method
"""


class Person:

    def introduce(self):
        print("I am a person.")


class Student(Person):

    def introduce(self):
        print("I am a student.")

    def study(self):
        print("I am studying Python.")


student_object=Student()

student_object.introduce()
student_object.study()


# ============================================================
# 31. INHERITANCE DOES NOT MEAN COPYING CODE
# ============================================================

"""
Inheritance does not simply copy the parent's source code into
the child class.

Instead, Python creates a relationship between the classes.

When an attribute or method is requested, Python searches
through the class hierarchy to find it.

This allows the child class to use functionality defined in
its parent.
"""


class Parent:

    def greet(self):
        print("Hello from Parent.")


class Child(Parent):
    pass


child_object=Child()

child_object.greet()


# ============================================================
# 32. BASIC CLASS HIERARCHY
# ============================================================

"""
A simple inheritance hierarchy can look like this:

                Animal
               /      \
             Dog      Cat

Animal contains common behavior.

Dog and Cat inherit that behavior.

Dog and Cat can also have their own behavior.
"""


class Animal:

    def eat(self):
        print("Eating.")


class Dog(Animal):

    def bark(self):
        print("Barking.")


class Cat(Animal):

    def meow(self):
        print("Meowing.")


dog_object=Dog()
cat_object=Cat()

dog_object.eat()
dog_object.bark()

cat_object.eat()
cat_object.meow()


# ============================================================
# 33. AVOIDING UNNECESSARY DUPLICATION
# ============================================================

"""
Inheritance can help avoid repeating common code.

Instead of:

    class Dog:
        def eat(self):
            ...

    class Cat:
        def eat(self):
            ...

we can write:

    class Animal:
        def eat(self):
            ...

    class Dog(Animal):
        ...

    class Cat(Animal):
        ...

The common behavior exists in one place.
"""


# ============================================================
# 34. IMPORTANT LIMITATION
# ============================================================

"""
Inheritance should not be used only to reuse a few lines of
code.

There should usually be a meaningful relationship between
the parent and child classes.

For example:

    Dog is an Animal

makes sense.

But:

    Computer is a Fruit

does not make sense.

Inheritance should represent a meaningful "is-a" relationship.
"""


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. Inheritance allows one class to acquire attributes and
   methods from another class.

2. The class being inherited from is called the:

       Parent class
       Base class
       Super class

3. The class that inherits is called the:

       Child class
       Derived class
       Sub class

4. Basic syntax:

       class Child(Parent):
           pass

5. Inheritance is useful for:

       - Code reuse
       - Extending existing classes
       - Creating relationships between classes

6. A child class can use methods inherited from its parent.

7. A child class can add its own attributes and methods.

8. Adding new functionality to a child class is called
   extending the parent class.

9. A child class can replace a parent method by defining
   a method with the same name.

10. Replacing a parent method is called method overriding.

11. A child class can both override inherited methods and
    add new methods.

12. If a child class defines its own __init__(), the parent
    __init__() is not automatically called.

13. Parent initialization can be called using super().
    We will study super() in detail later.

14. isinstance() checks whether an object is an instance
    of a class.

       isinstance(object, ClassName)

15. issubclass() checks whether one class is a subclass
    of another class.

       issubclass(ChildClass, ParentClass)

16. A child object can also be considered an instance of
    its parent class.

17. Inheritance commonly represents an "is-a" relationship.

    Dog is an Animal.
    Car is a Vehicle.
    Student is a Person.

18. Inheritance should be used when there is a meaningful
    relationship between the classes.

Simple way to remember:

    Parent
       ↓
    Child

    Child gets existing functionality
    +
    Child can add new functionality
    +
    Child can override existing behavior
"""