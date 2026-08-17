"""
ABSTRACTION
"""


# ============================================================
# 1. INTRODUCTION TO ABSTRACTION
# ============================================================

"""
Abstraction is one of the important concepts of
Object-Oriented Programming.

Abstraction means:

    Hiding unnecessary implementation details and exposing
    only the essential features that the user needs.

In simple words:

    Show what an object can do.
    Hide how the object does it.

For example, when you use a car, you know how to:

    start the car
    accelerate
    apply brakes
    turn the steering wheel

But you do not need to know all the internal details of:

    the engine
    fuel injection system
    transmission
    braking mechanism
    electrical system

You simply use the controls provided by the car.

This is the basic idea of abstraction.
"""


# ============================================================
# 2. REAL-WORLD ANALOGY: DRIVING A CAR
# ============================================================

"""
Consider driving a car.

As a driver, you interact with:

    steering wheel
    accelerator
    brake
    gear selector

You do not normally need to understand exactly how the engine
converts fuel into mechanical energy every time you press the
accelerator.

The car provides a simple interface:

    accelerator → increase speed
    brake      → reduce speed
    steering   → change direction

The complicated implementation is hidden.

This is abstraction.

We interact with the important features while the internal
details remain hidden from us.
"""


# ============================================================
# 3. ABSTRACTION IN PROGRAMMING
# ============================================================

"""
The same idea can be applied to programming.

Suppose we have a function:

    calculate_total()

The user of the function only needs to know:

    "Give me the required values and I will get the total."

The user does not necessarily need to know every calculation
performed inside the function.
"""


def calculate_total(price,quantity):
    subtotal=price*quantity
    tax=subtotal*0.05
    total=subtotal+tax

    return total


bill_total=calculate_total(100,3)

print("Total:",bill_total)


"""
The person using calculate_total() only needs to know:

    calculate_total(price,quantity)

The internal steps:

    subtotal=...
    tax=...
    total=...

are implementation details.

The function provides a simple interface while hiding the
calculation details.

This is a basic form of abstraction.
"""


# ============================================================
# 4. WHY DO WE NEED ABSTRACTION?
# ============================================================

"""
Without abstraction, users of our code may have to understand
many unnecessary details.

Imagine using a banking application.

You may want to:

    withdraw money
    deposit money
    check your balance

You do not need to understand:

    database queries
    encryption
    network communication
    transaction processing
    server-side validation

The application provides simple operations and hides the
complex implementation.

Abstraction makes complicated systems easier to use.
"""


# ============================================================
# 5. ABSTRACTION WITH A CLASS
# ============================================================

"""
Let's create a simple class that represents a coffee machine.

The user only needs to call:

    make_coffee()

The internal steps can be handled inside the class.
"""


class CoffeeMachine:

    def make_coffee(self):
        self._grind_beans()
        self._heat_water()
        self._brew_coffee()

        print("Coffee is ready.")

    def _grind_beans(self):
        print("Grinding coffee beans.")

    def _heat_water(self):
        print("Heating water.")

    def _brew_coffee(self):
        print("Brewing coffee.")


coffee_machine=CoffeeMachine()

coffee_machine.make_coffee()


"""
The user only needs:

    coffee_machine.make_coffee()

The user does not need to manually call:

    _grind_beans()
    _heat_water()
    _brew_coffee()

The class provides a simple interface:

    make_coffee()

while hiding the internal steps.

This is a simple example of abstraction.
"""


# ============================================================
# 6. SIMPLE INTERFACE VS COMPLEX IMPLEMENTATION
# ============================================================

"""
A useful way to understand abstraction is:

        SIMPLE INTERFACE
              ↓
        COMPLEX IMPLEMENTATION
              ↓
        HIDDEN FROM USER

For example:

    make_coffee()

may internally perform:

    grind beans
        ↓
    heat water
        ↓
    brew coffee
        ↓
    prepare coffee

The user only interacts with the simple operation.
"""


# ============================================================
# 7. ABSTRACTION AND ENCAPSULATION
# ============================================================

"""
Abstraction and Encapsulation are related concepts, but they
solve different problems.

ENCAPSULATION:

    Encapsulation focuses on bundling data and methods together
    and controlling access to the internal state of an object.

ABSTRACTION:

    Abstraction focuses on hiding unnecessary implementation
    details and exposing only the essential functionality.

A simple way to remember:

    Encapsulation:
        "Protect the internal data."

    Abstraction:
        "Hide the unnecessary implementation details."

Both concepts help us build cleaner and more maintainable
programs.
"""


# ============================================================
# 8. EXAMPLE: ENCAPSULATION VS ABSTRACTION
# ============================================================

"""
Consider a BankAccount class.

Encapsulation can protect the balance from being changed
directly.

Abstraction can provide simple operations such as:

    deposit()
    withdraw()
    get_balance()

The user does not need to know all the internal steps used
when a transaction is processed.
"""


class BankAccount:

    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        if(amount>0):
            self.__balance+=amount

    def withdraw(self,amount):
        if(0<amount<=self.__balance):
            self.__balance-=amount

    def get_balance(self):
        return self.__balance


account_object=BankAccount(1000)

account_object.deposit(500)
account_object.withdraw(200)

print("Balance:",account_object.get_balance())


"""
ENCAPSULATION:

    __balance

is protected from direct access through name mangling.

ABSTRACTION:

    deposit()
    withdraw()
    get_balance()

provide simple operations to interact with the account.

The user does not need to know exactly how the balance is
stored or how every transaction is processed internally.
"""


# ============================================================
# 9. ABSTRACTION HIDES IMPLEMENTATION DETAILS
# ============================================================

"""
Suppose we have a method:

    send_email()

The user might simply write:

    email_service.send_email()

Internally, the method may perform many operations:

    create connection
    authenticate user
    prepare message
    connect to server
    send data
    close connection

The user does not need to handle all these steps manually.

The complicated implementation is hidden behind a simple
interface.
"""


class EmailService:

    def send_email(self,recipient,message):
        self._connect_to_server()
        self._authenticate()
        self._send_message(recipient,message)
        self._disconnect()

        print("Email sent successfully.")

    def _connect_to_server(self):
        print("Connecting to email server.")

    def _authenticate(self):
        print("Authenticating.")

    def _send_message(self, recipient,message):
        print("Sending message to", recipient)

    def _disconnect(self):
        print("Disconnecting from server.")


email_service_object=EmailService()

email_service_object.send_email(
    "user@example.com",
    "Welcome to Python!"
)


"""
The user only needs to know:

    send_email(recipient,message)

The internal implementation is hidden behind this method.
"""


# ============================================================
# 10. ABSTRACTION CREATES A SIMPLE INTERFACE
# ============================================================

"""
An interface is the set of operations that a user interacts
with.

For our EmailService class, the simple interface is:

    send_email()

The internal helper methods are implementation details:

    _connect_to_server()
    _authenticate()
    _send_message()
    _disconnect()

The user can work with the simple interface without needing
to understand the complete implementation.
"""


# ============================================================
# 11. ANOTHER SIMPLE EXAMPLE
# ============================================================

"""
Consider a washing machine.

A user might select:

    wash()

The washing machine internally performs:

    fill water
    add detergent
    rotate drum
    rinse clothes
    spin clothes

The user does not need to manually control every step.
"""


class WashingMachine:

    def wash(self):
        self._fill_water()
        self._wash_clothes()
        self._rinse()
        self._spin()

        print("Washing completed.")

    def _fill_water(self):
        print("Filling water.")

    def _wash_clothes(self):
        print("Washing clothes.")

    def _rinse(self):
        print("Rinsing clothes.")

    def _spin(self):
        print("Spinning clothes.")


washing_machine_object=WashingMachine()

washing_machine_object.wash()


"""
The user interacts with:

    wash()

The implementation details are handled internally.

This makes the interface easier to understand and use.
"""


# ============================================================
# 12. ABSTRACTION REDUCES COMPLEXITY
# ============================================================

"""
Imagine a program that requires users to understand every
internal detail before they can perform a simple operation.

The program would become difficult to use.

Abstraction reduces this complexity.

Instead of exposing:

    20 complicated operations

we can expose:

    2 or 3 simple operations

The user can work with the system without understanding every
internal detail.
"""


# ============================================================
# 13. ABSTRACTION THROUGH FUNCTIONS
# ============================================================

"""
Abstraction is not limited to classes.

Functions also provide abstraction.

For example:
"""


def calculate_average(values):
    total=sum(values)
    count=len(values)

    return total/count


scores=[80,90,75,95]

average_score=calculate_average(scores)

print("Average:",average_score)


"""
The user only needs to know:

    calculate_average(scores)

The user does not need to manually perform:

    sum(values)
    len(values)
    total / count

The function hides those implementation details.
"""


# ============================================================
# 14. ABSTRACTION THROUGH MODULES
# ============================================================

"""
Python modules are another example of abstraction.

Suppose we use:

    math.sqrt()

We can simply write:
"""


import math

result=math.sqrt(81)

print("Square root:",result)


"""
We do not need to know the internal algorithm used by Python
to calculate the square root.

We simply use:

    math.sqrt()

The module provides a simple interface while hiding the
implementation details.

This is abstraction.
"""


# ============================================================
# 15. ABSTRACTION IN EVERYDAY PYTHON
# ============================================================

"""
You already use abstraction whenever you use built-in Python
features.

For example:

    print()
    len()
    sum()
    sorted()

You use these functions without needing to know exactly how
Python implements them internally.

For example:
"""


numbers=[40,10,30,20]

print(len(numbers))
print(sum(numbers))
print(sorted(numbers))


"""
You know what these functions do.

You do not need to understand their internal implementation
to use them.

This is the benefit of abstraction.
"""


# ============================================================
# 16. ABSTRACTION AND THE len() FUNCTION
# ============================================================

"""
When you write:

    len(numbers)

you do not need to manually count the elements.

Python handles the internal details.

You only need to know the interface:

    len(object)

This allows you to focus on what you want to accomplish
instead of how Python performs the operation internally.
"""


items = [
    "Python",
    "Java",
    "C++",
    "JavaScript"
]

item_count=len(items)

print("Number of items:",item_count)


# ============================================================
# 17. ABSTRACTION AND THE sorted() FUNCTION
# ============================================================

"""
Similarly, when you use:

    sorted()

you do not need to manually implement a sorting algorithm.

You simply write:
"""


values=[50,10,40,20,30]

sorted_values=sorted(values)

print(sorted_values)


"""
The sorting implementation is hidden from us.

The simple interface is:

    sorted(values)

This is another example of abstraction in everyday Python.
"""


# ============================================================
# 18. ABSTRACTION IN A CLASS
# ============================================================

"""
Let's create another example.

Suppose we have a music player.

The user wants to play a song.

The user should not have to manually:

    load the audio file
    decode the audio
    initialize the audio system
    send audio data to the speaker

The class can hide these details.
"""


class MusicPlayer:

    def play(self,song):
        self._load_song(song)
        self._decode_audio()
        self._start_playback()

        print("Playing:",song)

    def _load_song(self,song):
        print("Loading:",song)

    def _decode_audio(self):
        print("Decoding audio.")

    def _start_playback(self):
        print("Starting playback.")


music_player_object=MusicPlayer()

music_player_object.play("Python Tutorial.mp3")


"""
The user only needs to call:

    play(song)

The internal operations are hidden.
"""


# ============================================================
# 19. WHAT THE USER NEEDS TO KNOW
# ============================================================

"""
A good abstraction should make it clear what the user needs
to know.

For example:

    music_player.play(song)

The user needs to know:

    1. The method name.
    2. The required arguments.
    3. What the method does.

The user does not need to know:

    1. How the file is loaded.
    2. How audio is decoded.
    3. How playback is started internally.

This separation makes code easier to use.
"""


# ============================================================
# 20. ABSTRACTION IMPROVES MAINTAINABILITY
# ============================================================

"""
Abstraction also makes programs easier to maintain.

Suppose the internal implementation of our MusicPlayer
changes.

For example, we change how audio is decoded.

The user can still write:

    music_player.play(song)

The interface remains the same.

Only the internal implementation changes.
"""


class MusicPlayer:

    def play(self,song):
        self._prepare_audio(song)
        self._start_playback()

        print("Playing:",song)

    def _prepare_audio(self,song):
        print("Preparing audio:",song)

    def _start_playback(self):
        print("Starting playback.")


player_object=MusicPlayer()

player_object.play("Python Course.mp3")


"""
The code using MusicPlayer does not need to know how the
implementation changed.

This is one of the major benefits of abstraction.
"""


# ============================================================
# 21. ABSTRACTION AND INTERFACE DESIGN
# ============================================================

"""
A good abstraction should provide a simple and meaningful
interface.

For example:

    bank_account.deposit(500)

is easier to understand than requiring the user to manually
modify internal balance data.

Similarly:

    coffee_machine.make_coffee()

is easier than manually controlling every step of the coffee
making process.

The goal is:

    Simple outside
    Complex inside
"""


# ============================================================
# 22. SIMPLE OUTSIDE, COMPLEX INSIDE
# ============================================================

"""
A useful mental model for abstraction is:

              USER
                |
                ↓
        SIMPLE INTERFACE
                |
                ↓
      COMPLEX IMPLEMENTATION
                |
                ↓
             RESULT

The user interacts with the simple interface.

The implementation details remain hidden.
"""


# ============================================================
# 23. ABSTRACTION DOES NOT MEAN HIDING EVERYTHING
# ============================================================

"""
Abstraction does not mean that every detail must be hidden.

We should expose the operations that users actually need.

For example, a BankAccount might expose:

    deposit()
    withdraw()
    get_balance()

But it should not necessarily expose every internal operation
used to process a transaction.

The goal is to hide unnecessary details, not useful features.
"""


# ============================================================
# 24. ABSTRACTION VS ENCAPSULATION
# ============================================================

"""
Let's compare them more clearly.

ENCAPSULATION:

    Main idea:
        Bundle data and methods together and control access
        to the internal state.

    Focus:
        Protecting and controlling data.

    Example:
        __balance

        deposit()
        withdraw()

ABSTRACTION:

    Main idea:
        Hide implementation details and expose essential
        functionality.

    Focus:
        Reducing complexity and providing a simple interface.

    Example:
        account.withdraw(500)

The user does not need to know every internal step involved
in processing the withdrawal.
"""


# ============================================================
# 25. A SIMPLE COMPARISON
# ============================================================

"""
Think about a car.

ENCAPSULATION:

    The internal engine components are kept together and
    protected from uncontrolled access.

ABSTRACTION:

    The driver interacts with simple controls such as:

        accelerator
        brake
        steering wheel

    without needing to understand how the engine works
    internally.

So:

    Encapsulation → controls access to internal state.

    Abstraction   → hides unnecessary implementation details.
"""


# ============================================================
# 26. ABSTRACTION WITH A CALCULATOR
# ============================================================

"""
Consider a calculator application.

The user enters:

    10 + 20

and receives:

    30

The user does not need to know how the calculator internally
processes the expression.
"""


class Calculator:

    def add(self,first_value,second_value):
        return self._perform_addition(
            first_value,
            second_value
        )

    def _perform_addition(self,first_value,second_value):
        return first_value+second_value


calculator_object=Calculator()

result=calculator_object.add(10,20)

print("Result:",result)


"""
The public method:

    add()

provides the simple interface.

The internal method:

    _perform_addition()

contains implementation details.

The user only needs to call:

    add()
"""


# ============================================================
# 27. ABSTRACTION CAN HIDE MULTIPLE STEPS
# ============================================================

"""
One public method can hide many internal operations.

For example:
"""


class OnlineOrder:

    def place_order(self):
        self._check_inventory()
        self._calculate_price()
        self._process_payment()
        self._create_order()

        print("Order placed successfully.")

    def _check_inventory(self):
        print("Checking inventory.")

    def _calculate_price(self):
        print("Calculating price.")

    def _process_payment(self):
        print("Processing payment.")

    def _create_order(self):
        print("Creating order.")


order_object=OnlineOrder()

order_object.place_order()


"""
The user only sees:

    place_order()

The internal process contains several steps.

This is exactly the kind of complexity abstraction helps us
hide.
"""


# ============================================================
# 28. ABSTRACTION MAKES CODE EASIER TO USE
# ============================================================

"""
Imagine if a user had to write all of this:

    order.check_inventory()
    order.calculate_price()
    order.process_payment()
    order.create_order()

every time an order was placed.

Instead, we provide:

    order.place_order()

The second interface is simpler and easier to understand.

This is the purpose of abstraction.
"""


# ============================================================
# 29. ABSTRACTION MAKES CODE EASIER TO CHANGE
# ============================================================

"""
Suppose our online ordering system changes.

Maybe we add:

    discount calculation
    tax calculation
    fraud detection
    shipping calculation

We can add these steps internally to place_order().

The code using the class can continue to use:

    order.place_order()

The interface does not necessarily need to change.

This makes the system easier to maintain.
"""


# ============================================================
# 30. ABSTRACTION IN LARGE SOFTWARE SYSTEMS
# ============================================================

"""
Abstraction becomes even more important in large programs.

A large application may contain:

    user interface
    database
    authentication
    payment system
    logging
    network communication

A developer working on one part of the system should not
need to understand every internal detail of every other part.

Instead, each component can provide a simple interface.

For example:

    database.save()
    database.find()
    payment.process()
    email.send()

Each component hides its internal implementation.
"""


# ============================================================
# 31. A SIMPLE SOFTWARE SYSTEM EXAMPLE
# ============================================================

class Database:

    def save(self,data):
        self._connect()
        self._write_data(data)
        self._disconnect()

        print("Data saved.")

    def _connect(self):
        print("Connecting to database.")

    def _write_data(self,data):
        print("Writing:",data)

    def _disconnect(self):
        print("Disconnecting from database.")


database_object=Database()

database_object.save("Python Student")


"""
The user only needs:

    database.save(data)

The internal database operations are hidden.
"""


# ============================================================
# 32. IMPORTANT NOTE ABOUT UNDERSCORES
# ============================================================

"""
You may have noticed methods such as:

    _connect()
    _write_data()
    _disconnect()

The single underscore is a convention in Python.

It tells other programmers:

    "This is intended to be an internal implementation detail."

It does not create true private methods.

We will study Python's access conventions and encapsulation
in more detail in the related chapters.

For now, the important idea is that these methods represent
internal details that the user normally does not need to call
directly.
"""


# ============================================================
# 33. ABSTRACTION DOES NOT REQUIRE ABSTRACT CLASSES
# ============================================================

"""
It is important to understand that abstraction as a general
OOP concept does not necessarily require Python's abstract
classes.

We can create abstraction simply by designing a class or
function with a clean interface.

For example:

    coffee_machine.make_coffee()

is already an example of abstraction.

Later, we will learn about Python's formal tools for
abstraction, such as:

    abstract classes
    abstract methods

Those topics will be covered in the next chapter.
"""


# ============================================================
# 34. ABSTRACTION AND USER EXPERIENCE
# ============================================================

"""
Good abstraction improves the experience of the programmer
using your code.

Instead of asking the user to understand:

    10 internal methods

you can expose:

    2 or 3 meaningful methods.

For example:

    order.place_order()

is easier to understand than manually performing every
internal operation.

Good abstraction therefore makes APIs easier to learn and
use.
"""


# ============================================================
# 35. A COMPLETE EXAMPLE
# ============================================================

"""
Let's create one complete example that combines the main ideas.

Imagine an ATM.

The user wants to withdraw money.

The user interacts with:

    withdraw()

Internally, the ATM may:

    check the account
    verify the PIN
    check the balance
    process the transaction
    update the balance

The user does not need to control each step manually.
"""


class ATM:

    def __init__(self,balance):
        self.__balance=balance

    def withdraw(self,amount):
        if self._verify_amount(amount):
            if self._has_sufficient_balance(amount):
                self.__balance-=amount
                self._process_transaction()

                print("Please collect your cash.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid amount.")

    def _verify_amount(self,amount):
        return amount>0

    def _has_sufficient_balance(self,amount):
        return amount<=self.__balance

    def _process_transaction(self):
        print("Transaction processed.")


atm_object=ATM(5000)

atm_object.withdraw(1500)

"""
The user only needs to know:

    atm_object.withdraw(1500)

The internal steps are hidden:

    _verify_amount()
    _has_sufficient_balance()
    _process_transaction()

The user interacts with a simple interface while the class
handles the complicated implementation.
"""


# ============================================================
# 36. THE MAIN IDEA OF ABSTRACTION
# ============================================================

"""
The main idea of abstraction can be remembered as:

    Hide the unnecessary.
    Expose the necessary.

Or:

    Show WHAT to do.
    Hide HOW it is done.

For example:

    car.start()

The user needs to know:

    "This starts the car."

The user does not need to know every internal engine step
required to start it.
"""


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. Abstraction is one of the four important concepts of
   Object-Oriented Programming.

2. Abstraction means hiding unnecessary implementation details
   and exposing only the essential functionality.

3. A simple definition is:

       Show what an object can do.
       Hide how it does it.

4. A real-world example is a car.

5. A driver uses:

       steering
       accelerator
       brake

   without needing to understand all the internal details of
   the engine.

6. Functions can provide abstraction.

   Example:

       calculate_total(price, quantity)

   hides the internal calculation steps.

7. Classes can also provide abstraction.

   Example:

       coffee_machine.make_coffee()

   hides the internal coffee-making process.

8. Abstraction reduces complexity.

9. Abstraction provides a simpler interface to users.

10. Abstraction can hide multiple internal operations behind
    one simple method.

11. For example:

        order.place_order()

    can internally perform:

        check inventory
        calculate price
        process payment
        create order

12. The user only needs to know how to use the public
    interface.

13. Abstraction also makes programs easier to maintain.

14. Internal implementation can change while the public
    interface remains the same.

15. Abstraction and encapsulation are related but different.

16. Encapsulation focuses on:

        bundling data and methods
        controlling access to internal state

17. Abstraction focuses on:

        hiding implementation details
        exposing essential functionality
        reducing complexity

18. A simple way to remember the difference:

        Encapsulation:
            "Protect the data."

        Abstraction:
            "Hide the complexity."

19. Python functions such as:

        len()
        sum()
        sorted()

    are examples of abstraction because we use them without
    knowing their internal implementation.

20. Python modules also provide abstraction.

21. For example:

        math.sqrt(81)

    lets us use square-root functionality without implementing
    the algorithm ourselves.

22. Abstraction does not mean hiding everything.

23. We should expose the operations that users actually need
    and hide unnecessary implementation details.

24. A good abstraction provides a clear and simple interface.

25. A useful mental model is:

        Simple outside
             ↓
        Complex inside

26. Abstraction does not necessarily require an abstract class.

27. We can create abstraction simply by designing clean
    functions, classes, and interfaces.

28. Python's single underscore convention is often used to
    indicate internal implementation details.

29. Formal abstraction tools such as abstract classes and
    abstract methods will be covered in the next chapter.

The main idea to remember is:

    Abstraction allows us to work with a simple interface
    without needing to understand the complicated
    implementation behind it.

In the next chapter, we will learn about Abstract Classes and
Abstract Methods and see how Python provides a formal way to
define what subclasses are expected to implement.
"""