"""
CLASSES AND OBJECTS
"""


# ============================================================
# 1. INTRODUCTION TO CLASSES AND OBJECTS
# ============================================================

"""
Classes and objects are the foundation of Object-Oriented
Programming in Python.

A class is a blueprint or template used to create objects.

An object is an instance of a class.

For example:

Class:
    Car

Objects:
    car_one
    car_two
    car_three

The class defines the structure of objects, while objects are
the actual instances created from that class.
"""


# ============================================================
# 2. WHAT IS A CLASS?
# ============================================================

"""
A class is a blueprint or template for creating objects.

A class can define:

1. Data - information that an object stores.
2. Behavior - actions that an object can perform.

For example, a Car class can describe the common structure
and behavior of cars.

The class itself is not a specific car.

It is a blueprint that can be used to create specific car
objects.
"""


# ============================================================
# 3. CLASS SYNTAX
# ============================================================

"""
The basic syntax for creating a class is:

class ClassName:
    pass

The keyword 'class' is used to create a class.

ClassName is the name of the class.

The colon ':' starts the class body.

The 'pass' statement means that the class currently has
no code inside it.
"""


class ClassName:
    pass


# ============================================================
# 4. CREATING YOUR FIRST EMPTY CLASS
# ============================================================

"""
We can create an empty class when we want to define the class
first and add its features later.

The 'pass' statement allows Python to accept an empty class.
"""


class Notebook:
    pass


print("Notebook class created successfully.")


# ============================================================
# 5. WHAT IS AN OBJECT?
# ============================================================

"""
An object is an instance of a class.

After creating a class, we can create objects from that class.

Syntax:

object_name = ClassName()

The parentheses () are used to create an object from the class.

For example:

class Camera:
    pass

camera_item = Camera()

Here:

Camera
    is the class.

camera_item
    is the object.
"""


class Camera:
    pass


camera_item = Camera()

print("Camera object:", camera_item)


# ============================================================
# 6. CREATING AN OBJECT FROM A CLASS
# ============================================================

"""
Let's create a simple class called Laptop.

We can then create an object from the Laptop class.

The class is the blueprint.

The object is the actual instance created from that blueprint.
"""


class Laptop:
    pass


office_laptop = Laptop()

print("Laptop object:", office_laptop)


# ============================================================
# 7. CLASS VS OBJECT
# ============================================================

"""
A class and an object are related, but they are not the same.

Class:
    A blueprint or template.

Object:
    An actual instance created from the class.

For example:

Class:
    Book

Objects:
    science_book
    history_book

The Book class is the blueprint.

The two objects are separate instances created from that
blueprint.
"""


class Book:
    pass


science_book = Book()
history_book = Book()

print("Science book:", science_book)
print("History book:", history_book)


# ============================================================
# 8. CREATING MULTIPLE OBJECTS FROM THE SAME CLASS
# ============================================================

"""
One class can be used to create many objects.

Each object is a separate instance of that class.

For example, we can create multiple Employee objects from
the same Employee class.

All objects belong to the same class, but each object has
its own identity.
"""


class Employee:
    pass


employee_one = Employee()
employee_two = Employee()
employee_three = Employee()

print("Employee One:", employee_one)
print("Employee Two:", employee_two)
print("Employee Three:", employee_three)


# ============================================================
# 9. OBJECTS ARE SEPARATE INSTANCES
# ============================================================

"""
Objects created from the same class are separate instances.

Creating two objects from the same class does not mean that
both variables refer to the same object.

Each object is an independent instance.
"""


class Player:
    pass


player_alpha = Player()
player_beta = Player()

print("Player Alpha:", player_alpha)
print("Player Beta:", player_beta)

print("Are both objects the same?", player_alpha is player_beta)


# ============================================================
# 10. USING type() WITH OBJECTS
# ============================================================

"""
Python provides the built-in type() function.

The type() function tells us the type or class of an object.

Syntax:

type(object)

For example:

type(device)

If device is an object created from the Device class,
type(device) tells us that the object belongs to the
Device class.
"""


class Device:
    pass


smart_device = Device()

print("Object:", smart_device)
print("Object type:", type(smart_device))


# ============================================================
# 11. CONFIRMING AN OBJECT'S CLASS
# ============================================================

"""
We can use type() to confirm which class was used to create
an object.

For example, if an object was created using the Student class,
type() will show that the object belongs to the Student class.
"""


class Student:
    pass


student_record = Student()

print("Student object:", student_record)
print("Student object type:", type(student_record))


# ============================================================
# 12. MULTIPLE OBJECTS AND type()
# ============================================================

"""
We can also use type() with multiple objects.

Objects created from the same class will have the same class
type.
"""


class Vehicle:
    pass


vehicle_one = Vehicle()
vehicle_two = Vehicle()
vehicle_three = Vehicle()

print("Vehicle One type:", type(vehicle_one))
print("Vehicle Two type:", type(vehicle_two))
print("Vehicle Three type:", type(vehicle_three))


# ============================================================
# 13. REAL-WORLD ANALOGY: COOKIE CUTTER
# ============================================================

"""
A simple way to understand classes and objects is to think
about a cookie cutter.

Cookie cutter = Class

Cookie = Object

A cookie cutter is a tool or template used to create cookies.

The cutter itself is not a cookie.

Similarly, a class is a blueprint used to create objects.

One cookie cutter can create many cookies.

Likewise, one class can create many objects.

For example:

Class:
    CookieCutter

Objects:
    cookie_one
    cookie_two
    cookie_three
"""


class CookieCutter:
    pass


cookie_one = CookieCutter()
cookie_two = CookieCutter()
cookie_three = CookieCutter()

print("Cookie One:", cookie_one)
print("Cookie Two:", cookie_two)
print("Cookie Three:", cookie_three)


# ============================================================
# 14. COOKIE CUTTER ANALOGY IN DETAIL
# ============================================================

"""
Imagine that we have a star-shaped cookie cutter.

The cookie cutter represents the design or blueprint.

Every cookie produced from the cutter follows the same
basic structure.

However, each cookie is still a separate object.

In the same way:

Class = Blueprint

Object = Instance created from the blueprint

One class can therefore be used to create many independent
objects.
"""


class StarCookie:
    pass


first_cookie = StarCookie()
second_cookie = StarCookie()
third_cookie = StarCookie()

print("First cookie:", first_cookie)
print("Second cookie:", second_cookie)
print("Third cookie:", third_cookie)

print("First cookie type:", type(first_cookie))


# ============================================================
# 15. CLASS NAME AND OBJECT NAME
# ============================================================

"""
It is important to understand the difference between a class
name and an object name.

The class name identifies the blueprint.

The object name identifies a particular instance.

For example:

class Television:
    pass

living_room_tv = Television()

Here:

Television
    is the class.

living_room_tv
    is the object.

The object is created by calling the class.
"""


class Television:
    pass


living_room_tv = Television()

print("Class:", Television)
print("Object:", living_room_tv)
print("Object type:", type(living_room_tv))


# ============================================================
# 16. ONE CLASS, MANY OBJECTS
# ============================================================

"""
A major advantage of classes is that we do not need to create
a separate class for every similar object.

Instead, we create one class and then create multiple objects
from it.

For example, instead of creating:

RedCar
BlueCar
GreenCar

we can create one Car class and then create multiple Car
objects.

This makes our programs more organized and reusable.
"""


class Car:
    pass


red_car = Car()
blue_car = Car()
green_car = Car()

print("Red car:", red_car)
print("Blue car:", blue_car)
print("Green car:", green_car)


# ============================================================
# 17. CHECKING OBJECT IDENTITY
# ============================================================

"""
Every object is a separate instance.

Python provides the id() function to get the identity of
an object.

Syntax:

id(object)

Two different objects created from the same class normally
have different identities.
"""


class Backpack:
    pass


travel_bag = Backpack()
school_bag = Backpack()

print("Travel bag ID:", id(travel_bag))
print("School bag ID:", id(school_bag))

print("Are they the same object?", travel_bag is school_bag)


# ============================================================
# 18. BASIC CLASS AND OBJECT EXAMPLE
# ============================================================

"""
Let's combine the concepts we have learned so far.

We will:

1. Create a class.
2. Create multiple objects from that class.
3. Display the objects.
4. Use type() to check their class.
5. Use 'is' to check whether two objects are the same object.
"""


class Animal:
    pass


animal_one = Animal()
animal_two = Animal()

print("Animal One:", animal_one)
print("Animal Two:", animal_two)

print("Animal One type:", type(animal_one))
print("Animal Two type:", type(animal_two))

print("Are they the same object?", animal_one is animal_two)


# ============================================================
# 19. CLASS VS OBJECT: FINAL COMPARISON
# ============================================================

"""
Remember this simple difference:

Class:
    A blueprint or template.

Object:
    An actual instance created from the class.

Example:

class House:
    pass

my_house = House()

Here:

House
    is the class.

my_house
    is the object.

The class describes the type of object we want to create.

The object is the actual instance created from that class.
"""


class House:
    pass


my_house = House()

print("Class:", House)
print("Object:", my_house)
print("Object type:", type(my_house))


# ============================================================
# 20. WHY CLASSES AND OBJECTS ARE IMPORTANT
# ============================================================

"""
Classes and objects are the foundation of Object-Oriented
Programming.

With classes, we can define a common structure.

With objects, we can create multiple instances of that
structure.

In the upcoming chapters, we will add more features to our
classes.

Objects will be able to:

1. Store their own data.
2. Perform actions.
3. Use methods.
4. Interact with other objects.

For example, a Car object could eventually store:

- Brand
- Model
- Color
- Speed

And it could perform:

- Start
- Accelerate
- Brake
- Stop

These concepts will be introduced in the upcoming chapters.
"""


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. A class is a blueprint or template for creating objects.
2. An object is an instance of a class.
3. Classes are created using the 'class' keyword.
4. The basic class syntax is:

   class ClassName:
       pass

5. The 'pass' statement can be used to create an empty class.
6. An object can be created by calling the class:

   object_name = ClassName()

7. One class can be used to create multiple objects.
8. Objects created from the same class are separate instances.
9. The type() function can be used to check an object's class.
10. The id() function can be used to check an object's identity.
11. The 'is' operator can be used to check whether two names
    refer to the same object.
12. A class is like a cookie cutter.
13. An object is like a cookie created using that cookie cutter.
14. One class can be used to create many objects.
15. Classes provide the blueprint, while objects are the actual
    instances created from that blueprint.

In the next chapter, we will learn about the self parameter
and how objects can store their own data.
"""