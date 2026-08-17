"""
METHOD OVERRIDING
"""


# ============================================================
# 1. INTRODUCTION TO METHOD OVERRIDING
# ============================================================

"""
Method overriding is an important concept in inheritance.

Method overriding happens when a child class provides its own
implementation of a method that is already defined in its
parent class.

In simple words:

    Parent class
        ↓
    defines a method
        ↓
    Child class
        ↓
    defines the same method again

The child class's version replaces the inherited behavior when
the method is called through a child object.

Method overriding is useful when the child class needs behavior
that is different from the behavior provided by the parent.
"""


# ============================================================
# 2. SIMPLE EXAMPLE OF METHOD OVERRIDING
# ============================================================

"""
Suppose an Animal class has a make_sound() method.

A Dog is an Animal, but a dog makes a specific sound.

We can override make_sound() inside the Dog class.
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


"""
The output is:

    Animal makes a sound.
    Dog barks.

The Dog class has overridden the make_sound() method inherited
from Animal.

When we call:

    dog_object.make_sound()

Python uses the method defined inside Dog.
"""


# ============================================================
# 3. HOW METHOD OVERRIDING WORKS
# ============================================================

"""
When a method is called on an object, Python searches for the
method according to the class's Method Resolution Order (MRO).

For:

    class Dog(Animal):

the MRO is approximately:

    Dog
    Animal
    object

Python first checks Dog.

If Dog contains make_sound(), Python uses it.

If Dog does not contain make_sound(), Python continues to
Animal.

This is why defining the same method in the child class
overrides the parent's version.
"""


class Vehicle:

    def move(self):
        print("Vehicle is moving.")


class Bicycle(Vehicle):

    def move(self):
        print("Bicycle is moving using pedals.")


bicycle_object=Bicycle()

bicycle_object.move()


# ============================================================
# 4. REDEFINING A PARENT METHOD
# ============================================================

"""
To override a method, the child class defines a method with
the same name as the method in the parent class.

The method name and its purpose are the same, but the child
provides different behavior.
"""


class Employee:

    def work(self):
        print("Employee is working.")


class Developer(Employee):

    def work(self):
        print("Developer is writing code.")


developer_object=Developer()

developer_object.work()


"""
The work() method exists in both classes.

Employee:

    work()
        → Employee is working.

Developer:

    work()
        → Developer is writing code.

The Developer version is used for a Developer object.
"""


# ============================================================
# 5. WHY DO WE OVERRIDE METHODS?
# ============================================================

"""
We override a method when the child class needs behavior that
is more specific than the behavior provided by the parent.

For example:

    Parent:
        Vehicle → move()

Different vehicles may move differently:

    Car       → drives on roads
    Boat      → moves through water
    Airplane  → flies through the air

Instead of creating completely unrelated classes, we can
define common behavior in Vehicle and override it in the
child classes.
"""


class Vehicle:

    def move(self):
        print("Vehicle is moving.")


class Car(Vehicle):

    def move(self):
        print("Car is driving on the road.")


class Boat(Vehicle):

    def move(self):
        print("Boat is moving through the water.")


class Airplane(Vehicle):

    def move(self):
        print("Airplane is flying through the air.")


car_object=Car()
boat_object=Boat()
airplane_object=Airplane()

car_object.move()
boat_object.move()
airplane_object.move()


# ============================================================
# 6. OVERRIDING DOES NOT CHANGE THE PARENT CLASS
# ============================================================

"""
Overriding a method in a child class does not modify the
method in the parent class.

The parent still has its original implementation.

Only objects of the child class use the overridden version
when the child provides that method.
"""


class Animal:

    def eat(self):
        print("Animal is eating.")


class Dog(Animal):

    def eat(self):
        print("Dog is eating dog food.")


animal_object=Animal()
dog_object=Dog()

animal_object.eat()
dog_object.eat()


"""
Animal still uses:

    Animal.eat()

Dog uses:

    Dog.eat()

The parent method has not been changed.
"""


# ============================================================
# 7. OVERRIDING VS EXTENDING
# ============================================================

"""
These two concepts are different.

OVERRIDING:

The child provides a new implementation of an existing
parent method.

Example:

    Parent:
        move()

    Child:
        move()

The child replaces the inherited behavior.

EXTENDING:

The child keeps the inherited methods and adds new methods.

Example:

    Parent:
        move()

    Child:
        move()
        stop()

The child gets move() from the parent and adds stop().

We have already seen extending in the previous inheritance
chapter.
"""


class Vehicle:

    def start(self):
        print("Vehicle started.")


class Car(Vehicle):

    def stop(self):
        print("Car stopped.")


car_object=Car()

car_object.start()
car_object.stop()


# ============================================================
# 8. EXAMPLE OF BOTH OVERRIDING AND EXTENDING
# ============================================================

class Person:

    def introduce(self):
        print("I am a person.")


class Student(Person):

    def introduce(self):
        print("I am a student.")

    def study(self):
        print("Student is studying.")


student_object=Student()

student_object.introduce()
student_object.study()


"""
Here:

    introduce()
        → overridden from Person

    study()
        → new method added by Student

Therefore, the child class can override existing behavior
and extend the parent class with new functionality.
"""


# ============================================================
# 9. CALLING THE PARENT'S VERSION OF AN OVERRIDDEN METHOD
# ============================================================

"""
Sometimes we do not want to completely replace the parent's
behavior.

Instead, we may want to:

    1. Keep the parent's behavior.
    2. Add some additional behavior in the child.

For this situation, we can call the parent's method from
inside the overridden method.

Python provides the super() function for this purpose.

For now, we only need a basic understanding of super().

We will study super() in detail in the next chapter.
"""


class Animal:

    def eat(self):
        print("Animal is eating.")


class Dog(Animal):

    def eat(self):
        super().eat()
        print("Dog is eating its food.")


dog_object=Dog()

dog_object.eat()


"""
Output:

    Animal is eating.
    Dog is eating its food.

The line:

    super().eat()

calls the parent class's version of eat().

After that, the child class performs its additional behavior.
"""


# ============================================================
# 10. WHY USE super()?
# ============================================================

"""
Suppose the parent method already contains useful functionality.

If we completely replace the method, we would lose that
functionality.

Instead, we can use:

    super().method_name()

to call the parent implementation and then add child-specific
behavior.
"""


class Employee:

    def work(self):
        print("Employee starts working.")


class Developer(Employee):

    def work(self):
        super().work()
        print("Developer starts writing code.")


developer_object=Developer()

developer_object.work()


"""
The Developer class keeps the behavior of Employee and adds
its own behavior.

This is sometimes described as:

    Parent behavior
        +
    Child behavior
"""


# ============================================================
# 11. ANOTHER super() EXAMPLE
# ============================================================

class Vehicle:

    def start(self):
        print("Vehicle engine started.")


class Car(Vehicle):

    def start(self):
        super().start()
        print("Car is ready to drive.")


car_object=Car()

car_object.start()


# ============================================================
# 12. OVERRIDING __init__()
# ============================================================

"""
The __init__() method can also be overridden.

Remember that __init__() is used to initialize an object.

A parent class may define an __init__() method.

If the child class defines its own __init__(), the child's
version overrides the parent's __init__().
"""


class Person:

    def __init__(self,name):
        self.name=name


class Student(Person):

    def __init__(self,name):
        self.name=name
        print("Student object has been created.")


student_object=Student("Amina")

print("Name:",student_object.name)


"""
Student has its own __init__() method.

Therefore, the Person version is not automatically called.

The Student version is used when a Student object is created.
"""


# ============================================================
# 13. OVERRIDING __init__() WITH ADDITIONAL DATA
# ============================================================

"""
A common reason for overriding __init__() is that the child
class needs additional attributes.

For example:

Person needs:

    name

Student needs:

    name
    grade
"""


class Person:

    def __init__(self,name):
        self.name=name


class Student(Person):

    def __init__(self,name,grade):
        self.name=name
        self.grade=grade


student_record=Student("Hina", "A")

print("Name:",student_record.name)
print("Grade:",student_record.grade)


"""
The Student class has its own initialization logic because it
needs the additional grade attribute.
"""


# ============================================================
# 14. USING super() WITH __init__()
# ============================================================

"""
Instead of repeating the parent's initialization code, we can
call the parent's __init__() using super().

This is often the preferred approach when the child needs to
keep the parent's initialization and add more attributes.
"""


class Person:

    def __init__(self,name):
        self.name=name


class Student(Person):

    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade


student_record=Student("Usman","B")

print("Name:",student_record.name)
print("Grade:",student_record.grade)


"""
Here:

    super().__init__(name)

calls:

    Person.__init__(name)

The parent creates:

    self.name

Then the child creates:

    self.grade

So the child gets both pieces of initialization.
"""


# ============================================================
# 15. WHY super() IS BETTER THAN REPEATING CODE
# ============================================================

"""
Consider this example:

    class Student(Person):

        def __init__(self,name,grade):
            self.name=name
            self.grade=grade

The child repeats the code used by the parent to create name.

If the parent class later changes its initialization logic,
the child may also need to be changed.

Using:

    super().__init__(name)

allows the parent class to handle its own initialization.

Then the child only handles its additional data.
"""


class Person:

    def __init__(self,name):
        self.name=name
        print("Person initialization completed.")


class Student(Person):

    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
        print("Student initialization completed.")


student_object=Student("Bilal","A")


# ============================================================
# 16. OVERRIDING __init__() DOES NOT REQUIRE super()
# ============================================================

"""
Calling super() is not mandatory.

A child can completely replace the parent's __init__() if
that is what the design requires.

However, if the parent has important initialization that the
child also needs, super() is usually useful.
"""


class Account:

    def __init__(self,owner):
        self.owner=owner


class SavingsAccount(Account):

    def __init__(self,owner,interest_rate):
        self.owner=owner
        self.interest_rate=interest_rate


savings_object=SavingsAccount("Zain",4.5)

print("Owner:",savings_object.owner)
print("Interest Rate:",savings_object.interest_rate)


"""
This works, but the child has repeated:

    self.owner=owner

A cleaner approach can be:

    super().__init__(owner)

when the parent initialization should be reused.
"""


# ============================================================
# 17. METHOD OVERRIDING WITH DIFFERENT PARAMETERS
# ============================================================

"""
A child method can accept different parameters from the parent
method, but this should be done carefully.

The important concept in method overriding is that the child
provides a replacement implementation for the inherited
method.

For beginner-level code, it is usually easier to keep the
method's purpose and expected usage consistent.
"""


class Printer:

    def print_document(self,document):
        print("Printing:",document)


class ColorPrinter(Printer):

    def print_document(self,document):
        print("Printing in color:",document)


printer_object=Printer()
color_printer_object=ColorPrinter()

printer_object.print_document("Report")
color_printer_object.print_document("Report")


# ============================================================
# 18. OVERRIDING A METHOD IN A REAL-WORLD EXAMPLE
# ============================================================

"""
Imagine an application that has different types of users.

Every user can log in.

An Admin user may need additional behavior when logging in.

We can override the login() method in the Admin class.
"""


class User:

    def login(self):
        print("User logged in.")


class Admin(User):

    def login(self):
        print("Admin logged in.")
        print("Admin dashboard opened.")


user_object=User()
admin_object=Admin()

user_object.login()

print()

admin_object.login()


# ============================================================
# 19. PARENT METHOD + CHILD METHOD
# ============================================================

"""
Using super(), the child can keep the parent's behavior and
add its own behavior.

This is useful when the child does not want to completely
replace the parent's method.
"""


class User:

    def login(self):
        print("Checking user credentials.")
        print("User logged in.")


class Admin(User):

    def login(self):
        super().login()
        print("Admin permissions checked.")


admin_object=Admin()

admin_object.login()


# ============================================================
# 20. OVERRIDING AND MRO
# ============================================================

"""
Method overriding works together with Method Resolution Order.

Suppose:

    class Dog(Animal):

If both Dog and Animal contain make_sound(), the MRO is:

    Dog
    Animal
    object

Python finds make_sound() in Dog first.

Therefore, Dog's implementation is used.
"""


class Animal:

    def make_sound(self):
        print("Animal sound.")


class Dog(Animal):

    def make_sound(self):
        print("Dog sound.")


print(Dog.mro())

dog_object=Dog()

dog_object.make_sound()


# ============================================================
# 21. OVERRIDING IN MULTILEVEL INHERITANCE
# ============================================================

"""
Method overriding can also happen in multilevel inheritance.

Diagram:

        Animal
           |
           ↓
        Mammal
           |
           ↓
          Dog

If Mammal overrides a method from Animal, Dog inherits the
Mammal version unless Dog overrides it again.
"""


class Animal:

    def move(self):
        print("Animal is moving.")


class Mammal(Animal):

    def move(self):
        print("Mammal is walking.")


class Dog(Mammal):

    pass


dog_object=Dog()

dog_object.move()


"""
Dog does not define move().

Python searches:

    Dog
    Mammal
    Animal
    object

It finds move() in Mammal first.

Therefore, Mammal.move() is used.
"""


# ============================================================
# 22. OVERRIDING AT MULTIPLE LEVELS
# ============================================================

"""
A method can be overridden again at another level.

Diagram:

        Animal
           |
           ↓
        Mammal
           |
           ↓
          Dog

All three classes can provide their own version of move().
"""


class Animal:

    def move(self):
        print("Animal is moving.")


class Mammal(Animal):

    def move(self):
        print("Mammal is walking.")


class Dog(Mammal):

    def move(self):
        print("Dog is running.")


dog_object=Dog()

dog_object.move()


"""
Dog provides its own move().

Therefore, Dog.move() is used.
"""


# ============================================================
# 23. CALLING THE PARENT'S OVERRIDDEN METHOD
# ============================================================

"""
If Dog overrides Mammal's move() method, Dog can still call
the parent version using:

    super().move()
"""


class Animal:

    def move(self):
        print("Animal is moving.")


class Mammal(Animal):

    def move(self):
        print("Mammal is walking.")


class Dog(Mammal):

    def move(self):
        super().move()
        print("Dog is running.")


dog_object=Dog()

dog_object.move()


"""
The output is:

    Mammal is walking.
    Dog is running.

Here:

    super().move()

calls Mammal.move(), because Mammal is the parent class of Dog.
"""


# ============================================================
# 24. OVERRIDING __str__() - A SMALL PREVIEW
# ============================================================

"""
Python also has special methods that can be overridden.

For example, __str__() controls the string representation of
an object.

We will study magic methods in detail later.

For now, this is only a small example of overriding a special
method.
"""


class Product:

    def __str__(self):
        return "Product object"


class Book(Product):

    def __str__(self):
        return "Book object"


book_object=Book()

print(book_object)


"""
Book overrides the __str__() method inherited from Product.
"""


# ============================================================
# 25. IMPORTANT POINTS ABOUT METHOD OVERRIDING
# ============================================================

"""
Method overriding requires inheritance.

For example:

    class Parent:
        def show(self):
            ...


    class Child(Parent):
        def show(self):
            ...

The child method replaces the inherited behavior when called
through a Child object.

Important points:

    - The child uses the same method name.
    - The child provides its own implementation.
    - The parent method still exists.
    - Parent objects still use the parent's implementation.
    - Child objects use the child's implementation.
    - super() can be used to call the parent's implementation.
"""


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. Method overriding occurs when a child class defines a
   method with the same name as a method in its parent class.

2. The child class provides its own implementation of the
   inherited method.

3. Method overriding is used when a child needs behavior
   that is different or more specific than the parent.

4. Example:

       class Parent:

           def show(self):
               print("Parent")


       class Child(Parent):

           def show(self):
               print("Child")

5. When a Child object calls show(), Python uses Child.show().

6. Overriding does not modify the parent class.

7. Parent objects continue to use the parent's implementation.

8. Child objects use the overridden implementation.

9. A child can also extend the parent's behavior instead of
   completely replacing it.

10. The super() function can be used to call the parent's
    implementation.

11. Example:

       class Child(Parent):

           def show(self):
               super().show()
               print("Additional child behavior.")

12. The __init__() method can also be overridden.

13. If a child class defines its own __init__(), the parent's
    __init__() is not automatically called.

14. The child can call the parent's __init__() using:

       super().__init__()

15. Using super().__init__() is useful when the child needs
    to keep the parent's initialization and add its own
    attributes.

16. Method overriding works with the Method Resolution Order
    because Python searches the child class before its parent.

Simple way to remember:

    Parent:
        Provides default behavior

           ↓

    Child:
        Can override that behavior

           ↓

    Child object:
        Uses the child's version

If the child still needs the parent's behavior:

    super().method_name()

Use method overriding when a child class is a specialized
version of its parent and needs to behave differently.

In the next chapter, we will learn about the super() function
in more detail and understand how it works with inheritance
and multiple inheritance.
"""