"""
METHOD RESOLUTION ORDER (MRO)
"""


# ============================================================
# 1. INTRODUCTION TO MRO
# ============================================================

"""
Method Resolution Order, commonly called MRO, is the order in
which Python searches classes when it needs to find a method or
attribute.

MRO becomes especially important when inheritance is involved,
particularly with multiple inheritance.

For example, suppose a class inherits from two parent classes:

    class Child(ParentA,ParentB):
        pass

If both ParentA and ParentB contain a method with the same
name, Python needs a clear rule to decide which method should
be used.

MRO provides that rule.

In simple words:

    MRO=The order in which Python searches classes.


We will first look at the problem that MRO solves.
"""


# ============================================================
# 2. A SIMPLE INHERITANCE EXAMPLE
# ============================================================

"""
Consider the following inheritance:

        Animal
          |
          ↓
         Dog

If we call:

    dog_object.eat()

Python first checks the Dog class.

If eat() is not found there, Python checks Animal.

The search order is:

    Dog → Animal → object

This search order is the MRO.
"""


class Animal:

    def eat(self):
        print("Animal is eating.")


class Dog(Animal):
    pass


dog_object=Dog()

dog_object.eat()

print(Dog.__mro__)


# ============================================================
# 3. WHY DO WE NEED MRO?
# ============================================================

"""
With simple inheritance, finding a method is usually easy.

The situation becomes more interesting with multiple
inheritance.

Suppose:

        Parent A       Parent B
             \           /
              \         /
               ↓       ↓
                 Child

Both Parent A and Parent B may contain a method with the same
name.

For example:

    ParentA.show()
    ParentB.show()

Now Python needs to decide:

    Which show() should Child use?

MRO defines the search order that Python follows.
"""


class ParentA:

    def show(self):
        print("show() from ParentA")


class ParentB:

    def show(self):
        print("show() from ParentB")


class Child(ParentA,ParentB):
    pass


child_object=Child()

child_object.show()


"""
ParentA is searched before ParentB because ParentA appears
first in:

    class Child(ParentA,ParentB)

Therefore:

    ParentA.show()

is used.
"""


# ============================================================
# 4. VIEWING THE MRO WITH __mro__
# ============================================================

"""
Python provides the __mro__ attribute to see the Method
Resolution Order of a class.

Syntax:

    ClassName.__mro__

It returns a tuple containing the classes in the order Python
will search them.
"""


print(Child.__mro__)


"""
The result will look similar to:

    (
        <class '__main__.Child'>,
        <class '__main__.ParentA'>,
        <class '__main__.ParentB'>,
        <class 'object'>
    )

The exact module name may vary.

The important part is the order:

    Child
      ↓
    ParentA
      ↓
    ParentB
      ↓
    object
"""


# ============================================================
# 5. USING mro()
# ============================================================

"""
Python also provides the mro() class method.

Syntax:

    ClassName.mro()

It returns the MRO as a list.
"""


print(Child.mro())


"""
Both of these can be used to inspect the MRO:

    Child.__mro__
    Child.mro()

The main difference is that:

    __mro__ → returns a tuple
    mro()   → returns a list
"""


# ============================================================
# 6. __mro__ VS mro()
# ============================================================

class Vehicle:

    def start(self):
        print("Vehicle started.")


class Car(Vehicle):
    pass


print(Car.__mro__)
print(Car.mro())


"""
Both show the same class resolution order.

The important order is:

    Car
      ↓
    Vehicle
      ↓
    object
"""


# ============================================================
# 7. THE DIAMOND PROBLEM
# ============================================================

"""
One of the most important situations where MRO becomes useful
is the diamond problem.

Consider this structure:

              A
             / \
            /   \
           B     C
            \   /
             \ /
              D

Here:

    B inherits from A
    C inherits from A
    D inherits from both B and C

This creates a diamond-shaped inheritance structure.

This is called the Diamond Problem.
"""


class A:

    def show(self):
        print("Method from A")


class B(A):
    pass


class C(A):
    pass


class D(B,C):
    pass


diamond_object=D()

diamond_object.show()


# ============================================================
# 8. WHY IS THE DIAMOND PROBLEM INTERESTING?
# ============================================================

"""
The class D has two parents:

    B
    C

Both B and C inherit from A.

So the inheritance structure is:

              A
             / \
            B   C
             \ /
              D

When D calls:

    show()

Python needs to decide which path should be followed.

Should it search:

    D → B → A → C

or:

    D → C → A → B

or something else?

Python's MRO provides a consistent answer.
"""


# ============================================================
# 9. CHECKING THE MRO OF THE DIAMOND
# ============================================================

print(D.__mro__)

print(D.mro())


"""
The MRO will be similar to:

    D
    B
    C
    A
    object

So Python searches in this order:

    D → B → C → A → object

Notice that A appears only once.

This is an important property of Python's MRO.
"""


# ============================================================
# 10. WHY DOES A APPEAR ONLY ONCE?
# ============================================================

"""
Although both B and C inherit from A, Python does not simply
visit A twice.

The MRO algorithm creates a consistent order that avoids
unnecessary repetition.

Therefore, the search order is:

    D
    ↓
    B
    ↓
    C
    ↓
    A
    ↓
    object

A appears only once.
"""


# ============================================================
# 11. ADDING METHODS TO THE DIAMOND
# ============================================================

"""
Let's give each class a method with the same name.

This makes it easier to understand which method Python selects.
"""


class Base:

    def identify(self):
        print("Base")


class Left(Base):

    def identify(self):
        print("Left")


class Right(Base):

    def identify(self):
        print("Right")


class Final(Left,Right):

    pass


final_object=Final()

final_object.identify()


"""
The output is:

    Left

Why?

Because the MRO is:

    Final
    Left
    Right
    Base
    object

Python finds identify() in Left first.
"""


# ============================================================
# 12. CHANGING THE PARENT ORDER
# ============================================================

"""
The order of parent classes in the class definition matters.

Compare:

    class Final(Left,Right):
        pass

with:

    class AnotherFinal(Right,Left):
        pass

The parent order changes the MRO.
"""


class AnotherFinal(Right,Left):
    pass


another_final_object=AnotherFinal()

another_final_object.identify()

print(AnotherFinal.__mro__)


"""
The MRO is now:

    AnotherFinal
    Right
    Left
    Base
    object

Therefore, Right.identify() is used first.
"""


# ============================================================
# 13. HOW PYTHON SEARCHES FOR A METHOD
# ============================================================

"""
When we write:

    final_object.identify()

Python follows the MRO.

For:

    Final(Left,Right)

the MRO is:

    Final
    Left
    Right
    Base
    object

Python checks:

    1. Final
    2. Left
    3. Right
    4. Base
    5. object

The first class containing identify() provides the method.
"""


class Root:

    def display(self):
        print("Root display")


class First(Root):

    pass


class Second(First):

    def display(self):
        print("Second display")


class Third(Second):

    pass


third_object=Third()

third_object.display()


"""
The MRO is:

    Third
    Second
    First
    Root
    object

Third does not define display().

Second does define display().

Therefore, Python stops searching at Second.
"""


# ============================================================
# 14. MRO AND ATTRIBUTES
# ============================================================

"""
MRO is not only used for methods.

It also affects how Python searches for class attributes.

If an attribute is not found in the current class, Python
continues searching according to the MRO.
"""


class Parent:

    category="Parent"


class Child(Parent):
    pass


child_object=Child()

print(child_object.category)


"""
Child does not define category.

Python therefore searches Parent and finds:

    category="Parent"
"""


# ============================================================
# 15. MRO IN MULTIPLE INHERITANCE
# ============================================================

"""
Let's look at a simple multiple inheritance example.

Diagram:

        Writer      Speaker
            \        /
             \      /
             Presenter
"""


class Writer:

    def action(self):
        print("Writer action")


class Speaker:

    def action(self):
        print("Speaker action")


class Presenter(Writer,Speaker):
    pass


presenter_object=Presenter()

presenter_object.action()

print(Presenter.__mro__)


"""
The MRO is:

    Presenter
    Writer
    Speaker
    object

Therefore, Writer.action() is selected.
"""


# ============================================================
# 16. THE ORDER OF PARENT CLASSES MATTERS
# ============================================================

"""
If we reverse the parent order:

    class NewPresenter(Speaker, Writer):
        pass

the MRO changes.

Therefore, Speaker.action() will be found first.
"""


class NewPresenter(Speaker,Writer):
    pass


new_presenter_object=NewPresenter()

new_presenter_object.action()

print(NewPresenter.__mro__)


# ============================================================
# 17. WHAT IS C3 LINEARIZATION?
# ============================================================

"""
Python uses an algorithm called C3 Linearization to calculate
the Method Resolution Order.

You do not need to understand the mathematical details of C3
Linearization at this stage.

The important idea is:

    C3 Linearization creates a consistent MRO.

It helps Python:

    - Preserve the order of parent classes.
    - Avoid visiting the same class more than necessary.
    - Maintain a consistent inheritance order.
    - Handle complex multiple inheritance structures.

In simple words:

    C3 Linearization is the algorithm Python uses to build
    the MRO of a class.

The result is the order shown by:

    ClassName.__mro__

or:

    ClassName.mro()
"""


# ============================================================
# 18. C3 LINEARIZATION - CONCEPTUAL EXAMPLE
# ============================================================

"""
Consider:

              A
             / \
            B   C
             \ /
              D

Python needs an order that respects the relationships.

The resulting MRO is:

    D
    B
    C
    A
    object

This order is produced using C3 Linearization.

For this chapter, you only need to understand the result,
not the mathematical algorithm used to calculate it.
"""


class A:

    pass


class B(A):

    pass


class C(A):

    pass


class D(B,C):

    pass


print(D.mro())


# ============================================================
# 19. MRO WITH OBJECT
# ============================================================

"""
Every normal Python class ultimately has object at the end
of its MRO.

For example:

    class Animal:
        pass

The MRO is:

    Animal
    object

For multiple inheritance, object still appears at the end.
"""


class Animal:
    pass


print(Animal.__mro__)


# ============================================================
# 20. MRO IN MULTILEVEL INHERITANCE
# ============================================================

"""
MRO is also used with multilevel inheritance.

Diagram:

    Animal
       |
       ↓
    Mammal
       |
       ↓
      Dog

The MRO is:

    Dog
    Mammal
    Animal
    object
"""


class Animal:

    def eat(self):
        print("Animal eating")


class Mammal(Animal):

    def walk(self):
        print("Mammal walking")


class Dog(Mammal):

    def bark(self):
        print("Dog barking")


print(Dog.mro())


dog_object=Dog()

dog_object.eat()
dog_object.walk()
dog_object.bark()


# ============================================================
# 21. MRO CAN BE USED TO DEBUG INHERITANCE
# ============================================================

"""
When working with complex inheritance, it may not be obvious
which class provides a particular method.

Printing the MRO can help us understand Python's search order.

For example:

    print(MyClass.mro())

This is especially useful when working with multiple
inheritance.
"""


class Alpha:

    def run(self):
        print("Alpha")


class Beta(Alpha):

    pass


class Gamma(Alpha):

    def run(self):
        print("Gamma")


class Delta(Beta,Gamma):

    pass


print(Delta.mro())

delta_object=Delta()

delta_object.run()


"""
The MRO determines which run() method Python finds first.

The order is:

    Delta
    Beta
    Gamma
    Alpha
    object

Beta does not define run().

Gamma does define run().

Therefore, Gamma.run() is used.
"""


# ============================================================
# 22. ANOTHER DIAMOND EXAMPLE
# ============================================================

"""
Let's create a more practical example.

Diagram:

                 Employee
                /        \
               /          \
          Developer      Designer
               \          /
                \        /
                 \      /
                 Intern

Intern inherits from both Developer and Designer.

This creates a diamond-shaped structure.
"""


class Employee:

    def work(self):
        print("Employee is working.")


class Developer(Employee):

    def write_code(self):
        print("Developer is writing code.")


class Designer(Employee):

    def create_design(self):
        print("Designer is creating a design.")


class Intern(Developer,Designer):

    def learn(self):
        print("Intern is learning.")


intern_object=Intern()

intern_object.work()
intern_object.write_code()
intern_object.create_design()
intern_object.learn()

print(Intern.mro())


"""
The MRO is similar to:

    Intern
    Developer
    Designer
    Employee
    object

Employee appears only once even though both Developer and
Designer inherit from Employee.
"""


# ============================================================
# 23. WHAT IF BOTH PARENTS DEFINE THE SAME METHOD?
# ============================================================

"""
Now suppose Developer and Designer both define work().

Which one should Intern use?

The MRO decides.
"""


class Employee:

    def work(self):
        print("Employee is working.")


class Developer(Employee):

    def work(self):
        print("Developer is working.")


class Designer(Employee):

    def work(self):
        print("Designer is working.")


class Intern(Developer,Designer):

    pass


intern_object=Intern()

intern_object.work()

print(Intern.mro())


"""
The MRO is:

    Intern
    Developer
    Designer
    Employee
    object

Python finds work() in Developer first.

Therefore:

    Developer.work()

is called.
"""


# ============================================================
# 24. HOW TO PREDICT WHICH METHOD WILL RUN
# ============================================================

"""
To determine which method Python will call:

Step 1:
    Look at the class of the object.

Step 2:
    Check the class's MRO.

Step 3:
    Follow the MRO from left to right.

Step 4:
    The first class that contains the requested method
    provides the method.

For example:

    class Child(ParentA,ParentB):
        pass

If:

    ParentA.show()
    ParentB.show()

both exist, Python checks:

    Child
    ParentA
    ParentB
    object

ParentA.show() is therefore selected.
"""


# ============================================================
# 25. A SIMPLE MENTAL MODEL
# ============================================================

"""
Think of MRO as a search list.

For example:

    Child
    ParentA
    ParentB
    object

When Python needs a method:

    show()

it searches:

    Child      → Does it have show()?
       ↓
    ParentA    → Does it have show()?
       ↓
    ParentB    → Does it have show()?
       ↓
    object     → Does it have show()?

The first match wins.
"""


# ============================================================
# 26. SUMMARY
# ============================================================

"""
Important points:

1. MRO stands for Method Resolution Order.

2. MRO defines the order in which Python searches classes
   for methods and attributes.

3. MRO is especially important when multiple inheritance
   is used.

4. If multiple parent classes have a method with the same
   name, MRO helps Python decide which method to use.

5. You can view the MRO using:

       ClassName.__mro__

6. You can also view it using:

       ClassName.mro()

7. __mro__ normally returns a tuple.

8. mro() returns a list.

9. The first class in the MRO is the class itself.

10. object normally appears at the end of the MRO.

11. Python searches the MRO from left to right.

12. The first class containing the requested method is used.

13. The order of parent classes can affect the MRO.

14. For example:

       class Child(ParentA,ParentB):
           pass

    ParentA is searched before ParentB.

15. The Diamond Problem occurs when a class structure looks
    like:

              A
             / \
            B   C
             \ /
              D

16. Python's MRO prevents the common parent from being
    unnecessarily visited more than once.

17. Python uses C3 Linearization to calculate the MRO.

18. You do not need to know the mathematical details of
    C3 Linearization at this stage.

19. C3 Linearization helps produce a consistent and
    predictable MRO.

20. MRO is useful for understanding and debugging complex
    inheritance structures.

Simple way to remember:

    MRO = Search Order

When Python needs a method:

    1. Start with the object's class.
    2. Follow the MRO.
    3. Search from left to right.
    4. Stop at the first class containing the method.

For example:

    class Child(ParentA,ParentB):
        pass

The search order is generally:

    Child
      ↓
    ParentA
      ↓
    ParentB
      ↓
    object

In the next chapter, we will learn about Method Overriding
and how a child class can provide its own implementation of
a method inherited from its parent.
"""