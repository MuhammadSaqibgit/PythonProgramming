"""
COMPOSITION VS INHERITANCE
"""


# ============================================================
# 1. INTRODUCTION
# ============================================================

"""
In the previous chapters, we learned about inheritance.

Inheritance allows one class to receive attributes and methods
from another class.

For example:

    class Animal:
        ...

    class Dog(Animal):
        ...

Here, Dog "is an" Animal.

This is called an "is-a" relationship.

However, not every relationship between objects should be
represented using inheritance.

Sometimes one object simply contains another object.

For example:

    A Car has an Engine.

A Car is not an Engine.

Instead, a Car contains an Engine.

This is called composition.

Composition represents a "has-a" relationship.
"""


# ============================================================
# 2. WHAT IS COMPOSITION?
# ============================================================

"""
Composition means building a complex object by combining
simpler objects.

In other words:

    One class contains an object of another class.

For example:

    Car
      |
      └── Engine

The Car object has an Engine object.

We can create the Engine separately and then give it to the
Car.
"""


# ============================================================
# 3. SIMPLE COMPOSITION EXAMPLE
# ============================================================

class Engine:

    def start(self):
        print("Engine started.")


class Car:

    def __init__(self):
        self.engine=Engine()


my_car=Car()

my_car.engine.start()


"""
The Car class contains an Engine object.

The statement:

    self.engine=Engine()

creates an Engine object and stores it inside the Car object.

Therefore:

    Car has an Engine.

This is composition.
"""


# ============================================================
# 4. UNDERSTANDING THE "HAS-A" RELATIONSHIP
# ============================================================

"""
Composition is commonly described as a "has-a" relationship.

Examples:

    Car has an Engine.
    Computer has a Processor.
    House has a Room.
    Library has Books.
    Order has Products.

These relationships can often be represented using composition.

For example:

    Car
      |
      └── Engine

The Car does not become an Engine.

Instead, the Car uses an Engine.
"""


# ============================================================
# 5. WHY NOT USE INHERITANCE FOR CAR AND ENGINE?
# ============================================================

"""
We might incorrectly try to write:

    class Engine:
        ...

    class Car(Engine):
        ...

This means:

    Car is an Engine.

But this statement does not make logical sense.

A car and an engine are different things.

A Car uses an Engine.

Therefore, composition is a better relationship here.
"""


# ============================================================
# 6. COMPOSITION WITH A SEPARATE ENGINE OBJECT
# ============================================================

"""
Instead of creating the Engine directly inside Car, we can
create an Engine object separately and pass it to the Car.

This gives us more flexibility.
"""


class Engine:

    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")


class Car:

    def __init__(self,engine):
        self.engine=engine

    def start_car(self):
        self.engine.start()
        print("Car is ready to move.")

    def stop_car(self):
        self.engine.stop()
        print("Car has stopped.")


car_engine=Engine()

family_car=Car(car_engine)

family_car.start_car()
family_car.stop_car()


"""
Here:

    car_engine

is an Engine object.

We pass it to:

    Car(car_engine)

The Car stores the Engine object in:

    self.engine

This is composition.

The Car object now uses another object to perform part of its
work.
"""


# ============================================================
# 7. ONE OBJECT USING ANOTHER OBJECT
# ============================================================

"""
Composition often means that one object delegates some work
to another object.

For example:

    Car.start_car()

asks the Engine to start:

    self.engine.start()

The Car does not need to know exactly how the Engine starts.

It simply uses the Engine's public behavior.

This creates a clean separation between the two classes.
"""


# ============================================================
# 8. COMPOSITION WITH MULTIPLE COMPONENTS
# ============================================================

"""
A complex object can contain several smaller objects.

For example, a Computer can contain:

    Processor
    Memory
    Storage

We can represent this using composition.
"""


class Processor:

    def process(self):
        print("Processor is processing data.")


class Memory:

    def load(self):
        print("Memory is loading data.")


class Storage:

    def save(self):
        print("Storage is saving data.")


class Computer:

    def __init__(self,processor,memory,storage):
        self.processor=processor
        self.memory=memory
        self.storage=storage

    def run_program(self):
        self.storage.save()
        self.memory.load()
        self.processor.process()

        print("Program is running.")


computer_processor=Processor()
computer_memory=Memory()
computer_storage=Storage()

office_computer=Computer(
    computer_processor,
    computer_memory,
    computer_storage
)

office_computer.run_program()


"""
The Computer is built by combining three smaller objects:

    Computer
       |
       ├── Processor
       ├── Memory
       └── Storage

This is a good example of composition.

Instead of putting everything inside one large class, we
separate responsibilities into smaller classes.
"""


# ============================================================
# 9. BENEFIT: SEPARATION OF RESPONSIBILITIES
# ============================================================

"""
Composition allows each class to focus on one responsibility.

For example:

    Processor
        → handles processing

    Memory
        → handles memory operations

    Storage
        → handles storage

    Computer
        → coordinates these components

This makes the program easier to understand and maintain.
"""


# ============================================================
# 10. WHAT IS INHERITANCE?
# ============================================================

"""
Inheritance creates a relationship between a parent class and
a child class.

For example:
"""


class Animal:

    def eat(self):
        print("Animal is eating.")


class Dog(Animal):

    def bark(self):
        print("Dog is barking.")


pet_dog=Dog()

pet_dog.eat()
pet_dog.bark()


"""
Dog inherits from Animal.

The relationship is:

    Dog is an Animal.

This is an "is-a" relationship.

Inheritance is useful when the child genuinely represents a
specialized version of the parent.
"""


# ============================================================
# 11. IS-A VS HAS-A
# ============================================================

"""
One of the easiest ways to understand the difference is:

    Inheritance → "is-a"
    Composition → "has-a"

Inheritance examples:

    Dog is an Animal.
    Car is a Vehicle.
    Manager is an Employee.

Composition examples:

    Car has an Engine.
    Computer has a Processor.
    House has a Room.

If the relationship is naturally "is-a", inheritance may be
appropriate.

If the relationship is naturally "has-a", composition is often
more appropriate.
"""


# ============================================================
# 12. COMPOSITION EXAMPLE: CAR AND ENGINE
# ============================================================

"""
Let's compare the two approaches.

Incorrect relationship:

    Car inherits from Engine

This says:

    Car is an Engine.

Correct relationship:

    Car contains an Engine.

This says:

    Car has an Engine.
"""


class Engine:

    def start(self):
        print("Engine is running.")


class Vehicle:

    def move(self):
        print("Vehicle is moving.")


class SportsCar(Vehicle):

    def __init__(self,engine):
        self.engine=engine

    def start(self):
        self.engine.start()
        print("Sports car started.")


sports_engine=Engine()

race_car=SportsCar(sports_engine)

race_car.start()
race_car.move()


"""
SportsCar inherits from Vehicle because:

    SportsCar is a Vehicle.

SportsCar contains an Engine because:

    SportsCar has an Engine.

This example uses both inheritance and composition where each
relationship makes sense.
"""


# ============================================================
# 13. COMPOSITION DOES NOT MEAN NO INHERITANCE
# ============================================================

"""
Composition and inheritance are not mutually exclusive.

A class can use inheritance and composition at the same time.

For example:

    SportsCar is a Vehicle
    SportsCar has an Engine

So we can have:

    class SportsCar(Vehicle):

        def __init__(self,engine):
            self.engine=engine

Inheritance handles the "is-a" relationship.

Composition handles the "has-a" relationship.
"""


# ============================================================
# 14. COMPOSITION MAKES COMPONENTS REPLACEABLE
# ============================================================

"""
One major advantage of composition is that we can replace a
component without changing the main class.

For example, imagine that we have two engine classes:

    PetrolEngine
    ElectricEngine

Both can provide a start() method.
"""


class PetrolEngine:

    def start(self):
        print("Petrol engine started.")


class ElectricEngine:

    def start(self):
        print("Electric motor started.")


class Vehicle:

    def __init__(self,engine):
        self.engine=engine

    def start(self):
        self.engine.start()


petrol_vehicle=Vehicle(PetrolEngine())
electric_vehicle=Vehicle(ElectricEngine())

petrol_vehicle.start()
electric_vehicle.start()


"""
The Vehicle class does not need to know whether it contains a
PetrolEngine or an ElectricEngine.

It simply calls:

    self.engine.start()

This makes the design flexible.
"""


# ============================================================
# 15. CHANGING A COMPONENT
# ============================================================

"""
Because the Engine is a separate object, we can replace it.

For example:
"""


class BasicEngine:

    def start(self):
        print("Basic engine started.")


class PowerfulEngine:

    def start(self):
        print("Powerful engine started.")


class Machine:

    def __init__(self,engine):
        self.engine=engine

    def start(self):
        self.engine.start()


machine_engine=BasicEngine()

machine=Machine(machine_engine)

machine.start()

machine.engine=PowerfulEngine()

machine.start()


"""
The Machine class did not need to be rewritten.

We simply replaced the component.

This is one of the strengths of composition.
"""


# ============================================================
# 16. COMPOSITION AND FLEXIBILITY
# ============================================================

"""
Composition allows us to change the internal components of an
object without changing the object's overall interface.

For example:

    Vehicle
       |
       └── Engine

The Vehicle can work with different engine implementations.

This can make a program easier to extend.
"""


# ============================================================
# 17. INHERITANCE CAN CREATE TIGHT COUPLING
# ============================================================

"""
Inheritance creates a strong relationship between a child and
its parent.

For example:

    class Child(Parent):
        ...

The child depends on the structure and behavior of the parent.

If the parent changes, the child can sometimes be affected.

This is called tight coupling.

Composition can often reduce this dependency by allowing
components to be replaced independently.
"""


# ============================================================
# 18. SIMPLE EXAMPLE OF TIGHT COUPLING
# ============================================================

"""
Suppose we create a class hierarchy:
"""


class BasicPrinter:

    def print_document(self):
        print("Printing document.")


class OfficeComputer(BasicPrinter):

    def work(self):
        self.print_document()
        print("Computer is working.")


office_machine=OfficeComputer()

office_machine.work()


"""
OfficeComputer now depends directly on BasicPrinter through
inheritance.

If the design later requires a different printing system,
changing the parent relationship may become inconvenient.
"""


# ============================================================
# 19. THE COMPOSITION ALTERNATIVE
# ============================================================

"""
We can instead make the printer a separate component.
"""


class Printer:

    def print_document(self):
        print("Printing document.")


class Workstation:

    def __init__(self,printer):
        self.printer=printer

    def work(self):
        self.printer.print_document()
        print("Computer is working.")


office_printer=Printer()

work_computer=Workstation(office_printer)

work_computer.work()


"""
Now Workstation has a Printer.

It does not inherit from Printer.

This makes the relationship clearer:

    Workstation has a Printer.
"""


# ============================================================
# 20. COMPOSITION AND DELEGATION
# ============================================================

"""
In the previous example:

    self.printer.print_document()

the Workstation asks the Printer object to perform the printing.

This is called delegation.

The Workstation delegates printing responsibility to the
Printer object.

Composition and delegation are often used together.
"""


# ============================================================
# 21. ANOTHER REAL-WORLD EXAMPLE
# ============================================================

"""
Consider a Smartphone.

A Smartphone may contain:

    Battery
    Camera
    Speaker

The Smartphone is not a Battery.

The Smartphone is not a Camera.

The Smartphone is not a Speaker.

Instead:

    Smartphone has a Battery.
    Smartphone has a Camera.
    Smartphone has a Speaker.

Therefore composition is a natural choice.
"""


class Battery:

    def charge(self):
        print("Battery is charging.")


class Camera:

    def take_photo(self):
        print("Photo captured.")


class Speaker:

    def play_sound(self):
        print("Playing sound.")


class Smartphone:

    def __init__(self,battery,camera,speaker):
        self.battery=battery
        self.camera=camera
        self.speaker=speaker

    def take_picture(self):
        self.camera.take_photo()

    def play_music(self):
        self.speaker.play_sound()

    def charge_phone(self):
        self.battery.charge()


phone_battery=Battery()
phone_camera=Camera()
phone_speaker=Speaker()

my_phone=Smartphone(
    phone_battery,
    phone_camera,
    phone_speaker
)

my_phone.take_picture()
my_phone.play_music()
my_phone.charge_phone()


"""
The Smartphone combines several independent objects.

Each component has its own responsibility.
"""


# ============================================================
# 22. INHERITANCE EXAMPLE
# ============================================================

"""
Inheritance is useful when classes have a genuine "is-a"
relationship.

For example:

    Animal
       |
       ├── Dog
       └── Cat

Both Dog and Cat are Animals.
"""


class Animal:

    def eat(self):
        print("Animal is eating.")


class Cat(Animal):

    def meow(self):
        print("Cat says meow.")


class Dog(Animal):

    def bark(self):
        print("Dog says woof.")


cat_object=Cat()
dog_object=Dog()

cat_object.eat()
cat_object.meow()

dog_object.eat()
dog_object.bark()


"""
Here inheritance makes sense because:

    Cat is an Animal.
    Dog is an Animal.

This is a natural "is-a" relationship.
"""


# ============================================================
# 23. COMPOSITION EXAMPLE
# ============================================================

"""
Now consider a Dog and a Collar.

A Dog is not a Collar.

A Dog has a Collar.

So composition is appropriate.
"""


class Collar:

    def __init__(self,color):
        self.color=color

    def show_color(self):
        print(f"Collar color: {self.color}")


class PetDog:

    def __init__(self,collar):
        self.collar=collar

    def show_collar(self):
        self.collar.show_color()


red_collar=Collar("Red")

my_pet=PetDog(red_collar)

my_pet.show_collar()


"""
The relationship is:

    PetDog has a Collar.

Therefore composition is appropriate.
"""


# ============================================================
# 24. WHEN SHOULD YOU CHOOSE INHERITANCE?
# ============================================================

"""
Inheritance is often a good choice when:

1. There is a clear "is-a" relationship.

2. The child is genuinely a specialized version of the parent.

3. The child should share a common interface with the parent.

4. Polymorphism through a common base class is useful.

For example:

    Animal
       |
       ├── Dog
       ├── Cat
       └── Bird

Each child is an Animal.

This is a natural use of inheritance.
"""


# ============================================================
# 25. WHEN SHOULD YOU CHOOSE COMPOSITION?
# ============================================================

"""
Composition is often a good choice when:

1. There is a "has-a" relationship.

2. You want to combine several independent components.

3. Components may need to be replaced.

4. You want to reduce dependency between classes.

5. You want each class to have a focused responsibility.

6. You want greater flexibility in changing behavior.
"""


# ============================================================
# 26. COMPOSITION VS INHERITANCE
# ============================================================

"""
Let's summarize the main differences.

Inheritance:

    Represents an "is-a" relationship.

Composition:

    Represents a "has-a" relationship.

Inheritance:

    Child depends on parent.

Composition:

    Main object contains another object.

Inheritance:

    Useful for creating class hierarchies.

Composition:

    Useful for assembling objects from components.

Inheritance:

    Can create tighter coupling.

Composition:

    Often provides more flexibility.
"""


# ============================================================
# 27. SIMPLE COMPARISON TABLE
# ============================================================

"""
                    INHERITANCE          COMPOSITION

Relationship        Is-a                Has-a

Example             Dog is an Animal    Car has an Engine

Structure            Parent/Child        Object contains
                                        another object

Main purpose         Specialization      Combining components

Coupling              Usually tighter    Often looser

Flexibility           Can be lower       Often higher

Code reuse            Through inheritance
                                         Through delegation
                                         and reusable objects
"""


# ============================================================
# 28. "FAVOR COMPOSITION OVER INHERITANCE"
# ============================================================

"""
You may often hear this principle:

    "Favor composition over inheritance."

This does NOT mean:

    "Never use inheritance."

It means:

    "When both approaches could reasonably solve the problem,
     composition is often the more flexible choice."

Composition allows us to build objects from smaller components
without creating a deep inheritance hierarchy.
"""


# ============================================================
# 29. WHY FAVOR COMPOSITION?
# ============================================================

"""
Consider a large inheritance hierarchy:

    Vehicle
       |
       └── Car
            |
            └── SportsCar
                 |
                 └── RacingSportsCar

As the hierarchy grows, relationships between classes can
become difficult to understand and maintain.

With composition, we can instead combine components:

    RacingCar
       |
       ├── Engine
       ├── Transmission
       ├── Brakes
       └── NavigationSystem

Each component can be developed and changed independently.

This can result in a more flexible design.
"""


# ============================================================
# 30. COMPOSITION DOES NOT ALWAYS REPLACE INHERITANCE
# ============================================================

"""
There are situations where inheritance is exactly the right
choice.

For example:

    Animal
       |
       ├── Dog
       ├── Cat
       └── Bird

This hierarchy naturally represents an "is-a" relationship.

Trying to replace every inheritance relationship with
composition would also be poor design.

The goal is not to avoid inheritance.

The goal is to choose the relationship that best represents
the problem.
"""


# ============================================================
# 31. COMPOSITION WITH DIFFERENT BEHAVIORS
# ============================================================

"""
Composition becomes especially useful when we want to change
behavior by replacing a component.

For example, a notification system could use different
notification services.
"""


class EmailService:

    def send(self,message):
        print(f"Email:{message}")


class SMSService:

    def send(self,message):
        print(f"SMS:{message}")


class Notification:

    def __init__(self,service):
        self.service=service

    def notify(self,message):
        self.service.send(message)


email_notification=Notification(EmailService())

email_notification.notify("Your order is ready.")


sms_notification=Notification(SMSService())

sms_notification.notify("Your order is ready.")


"""
The Notification class does not need to inherit from
EmailService or SMSService.

Instead, it contains a service object.

We can change the behavior simply by supplying a different
service.

This is a powerful use of composition.
"""


# ============================================================
# 32. COMPOSITION AND LOOSE COUPLING
# ============================================================

"""
In the previous example, Notification only expects the service
to provide:

    send()

It does not need to know the internal details of the service.

This reduces coupling.

The Notification class can work with different service
objects as long as they provide the required behavior.

This idea connects directly with duck typing, which we studied
earlier.
"""


# ============================================================
# 33. COMPOSITION WITH DUCK TYPING
# ============================================================

"""
Python's duck typing makes composition particularly flexible.

The Notification class does not necessarily need a specific
parent class.

It simply needs an object with a:

    send()

method.

For example:
"""


class PushService:

    def send(self,message):
        print(f"Push notification: {message}")


push_notification=Notification(PushService())

push_notification.notify("You have a new message.")


"""
PushService does not inherit from EmailService or SMSService.

It simply provides the behavior Notification needs.

This is another reason composition works very naturally in
Python.
"""


# ============================================================
# 34. A COMMON BEGINNER MISTAKE
# ============================================================

"""
A common mistake is choosing inheritance simply because one
class needs to reuse code from another class.

For example:

    class Car(Engine):
        ...

A beginner might think:

    "Car needs Engine's start() method, so Car should inherit
     from Engine."

But inheritance is not primarily about sharing code.

The relationship should make sense.

Car and Engine are different concepts.

A better design is:

    class Car:

        def __init__(self,engine):
            self.engine=engine

        def start(self):
            self.engine.start()

This represents the actual relationship.
"""


# ============================================================
# 35. CODE REUSE: INHERITANCE VS COMPOSITION
# ============================================================

"""
Both inheritance and composition can help us reuse code.

Inheritance reuses behavior through a parent class.

Composition reuses behavior by using another object.

Inheritance:

    class Dog(Animal):
        ...

Composition:

    class Car:

        def __init__(self, engine):
            self.engine = engine

Both approaches can be useful.

The important question is not:

    "Which one gives me code reuse?"

The better question is:

    "What relationship exists between these objects?"
"""


# ============================================================
# 36. PRACTICAL DESIGN EXAMPLE
# ============================================================

"""
Suppose we are building a restaurant application.

We may have:

    Restaurant
    Chef
    Menu
    PaymentSystem

A Restaurant has a Chef.

A Restaurant has a Menu.

A Restaurant has a PaymentSystem.

These are "has-a" relationships, so composition can be useful.
"""


class Chef:

    def cook(self):
        print("Chef is preparing the food.")


class Menu:

    def show(self):
        print("Showing restaurant menu.")


class PaymentSystem:

    def process_payment(self):
        print("Payment processed.")


class Restaurant:

    def __init__(self,chef,menu,payment_system):
        self.chef=chef
        self.menu=menu
        self.payment_system=payment_system

    def serve_customer(self):
        self.menu.show()
        self.chef.cook()
        self.payment_system.process_payment()


restaurant_chef=Chef()
restaurant_menu=Menu()
restaurant_payment=PaymentSystem()

local_restaurant=Restaurant(
    restaurant_chef,
    restaurant_menu,
    restaurant_payment
)

local_restaurant.serve_customer()


"""
The Restaurant is built from several smaller components.

This is composition.
"""


# ============================================================
# 37. A USEFUL DECISION PROCESS
# ============================================================

"""
When deciding between inheritance and composition, ask:

Question 1:

    "Is the child genuinely a type of the parent?"

If yes, inheritance may be appropriate.

Example:

    Dog is an Animal.


Question 2:

    "Does the object contain or use another object?"

If yes, composition may be appropriate.

Example:

    Car has an Engine.


Question 3:

    "Do I need to replace the component later?"

If yes, composition can be a good choice.


Question 4:

    "Am I creating inheritance mainly to reuse a few methods?"

If yes, consider composition instead.


Question 5:

    "Would the inheritance relationship sound strange in
     plain English?"

If yes, composition may be a better design.
"""


# ============================================================
# 38. FINAL COMPARISON EXAMPLE
# ============================================================

"""
Let's look at both relationships together.
"""


class Employee:

    def work(self):
        print("Employee is working.")


class Developer(Employee):

    def write_code(self):
        print("Developer is writing code.")


class Computer:

    def start(self):
        print("Computer started.")


class DeveloperWithComputer(Employee):

    def __init__(self,computer):
        self.computer=computer

    def write_code(self):
        self.computer.start()
        print("Developer is writing code.")


"""
Developer:

    Developer is an Employee.

Therefore:

    Inheritance

DeveloperWithComputer:

    DeveloperWithComputer has a Computer.

Therefore:

    Composition

One class can use both concepts when necessary.
"""


developer=Developer()

developer.work()
developer.write_code()


developer_computer=Computer()

developer_with_computer=DeveloperWithComputer(developer_computer)

developer_with_computer.work()
developer_with_computer.write_code()


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. Composition means building a complex object by combining
   simpler objects.

2. Composition represents a "has-a" relationship.

3. For example:

       Car has an Engine.

4. A Car should not inherit from Engine because:

       Car is not an Engine.

5. Instead, Car can contain an Engine object.

6. Example:

       class Car:

           def __init__(self,engine):
               self.engine=engine

7. Inheritance represents an "is-a" relationship.

8. For example:

       Dog is an Animal.

9. Inheritance is useful when a child is genuinely a
   specialized version of its parent.

10. Composition is useful when an object contains or uses
    another object.

11. Composition allows complex objects to be built from smaller
    components.

12. A class can contain multiple objects.

13. For example:

        Computer
           |
           ├── Processor
           ├── Memory
           └── Storage

14. Composition encourages separation of responsibilities.

15. Each component can focus on a specific task.

16. Composition can make components replaceable.

17. For example, a Vehicle can work with different Engine
    objects.

18. Composition often reduces coupling between classes.

19. Composition commonly works together with delegation.

20. Delegation means allowing another object to perform a
    particular task.

21. Python's duck typing makes composition especially flexible.

22. A class can often work with any object that provides the
    required behavior.

23. Inheritance and composition can be used together.

24. For example:

        SportsCar is a Vehicle.
        SportsCar has an Engine.

25. Both relationships can be correct in the same design.

26. "Favor composition over inheritance" does not mean
    inheritance is bad.

27. It means that when both approaches are possible,
    composition is often more flexible.

28. Do not use inheritance only because you want to reuse a few
    methods.

29. First identify the relationship between the objects.

30. Ask:

        Is-a?
            → Consider inheritance.

        Has-a?
            → Consider composition.

31. Good inheritance represents a natural hierarchy.

32. Good composition represents objects working together.

33. Composition is especially useful when behavior or
    components may need to be changed independently.

34. The most important idea is:

        Inheritance → "is-a"

        Composition → "has-a"

35. A useful design principle is:

        "Favor composition over inheritance."

    Use inheritance when the relationship is truly a natural
    "is-a" relationship. Otherwise, consider composition.

In the next chapter, we will learn about Association and
Aggregation and understand how these relationships differ from
composition.
"""