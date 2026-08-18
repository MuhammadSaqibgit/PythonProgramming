"""
CLASS AND METHOD DECORATORS
"""


# ============================================================
# 1. INTRODUCTION
# ============================================================

"""
In the Python Basics folder, we learned about decorators.

A decorator is a function that modifies or extends the behavior
of another function without changing the original function's
code.

For example:

    @decorator
    def function():
        ...

Python passes the function to the decorator and uses the
modified version.

Decorators are also very useful in Object-Oriented Programming.

We can use decorators with:

    1. Methods
    2. Classes

In this chapter, we will learn how decorators work with methods
and classes and how to create our own custom decorators.
"""


# ============================================================
# 2. QUICK RECAP OF DECORATORS
# ============================================================

"""
A decorator is a function that takes another function and
returns a new function.

Basic structure:

    def my_decorator(function):

        def wrapper():
            ...
            function()
            ...

        return wrapper

Then we can use:

    @my_decorator
    def greet():
        print("Hello!")

The @ syntax is simply a convenient way of applying the
decorator.

This:

    @my_decorator
    def greet():
        ...

is equivalent to:

    def greet():
        ...

    greet = my_decorator(greet)
"""


# ============================================================
# 3. SIMPLE DECORATOR RECAP
# ============================================================

def announce_call(function):

    def wrapper():
        print("Function is about to run.")
        function()
        print("Function has finished.")

    return wrapper


@announce_call
def say_hello():
    print("Hello, Python!")


say_hello()


"""
The decorator adds extra behavior before and after the original
function.

The original function does not need to contain the extra
messages.

This is the basic idea behind decorators.
"""


# ============================================================
# 4. DECORATORS WITH ARGUMENTS
# ============================================================

"""
Methods often receive arguments.

Therefore, a useful decorator should normally be able to handle
different arguments.

We can use:

    *args
    **kwargs

inside the wrapper.
"""


def show_arguments(function):

    def wrapper(*args,**kwargs):
        print("Arguments:",args)
        print("Keyword arguments:",kwargs)

        return function(*args,**kwargs)

    return wrapper


@show_arguments
def multiply_numbers(first_number,second_number):
    return first_number*second_number


result=multiply_numbers(5,4)

print("Result:",result)


"""
The decorator receives all arguments and passes them to the
original function.

This pattern becomes especially important when decorating
methods.
"""


# ============================================================
# 5. DECORATORS AND METHODS
# ============================================================

"""
A method is simply a function defined inside a class.

Therefore, decorators can also be applied to methods.

For example:
"""


class Greeter:

    @announce_call
    def greet(self):
        print("Welcome!")


greeter_object=Greeter()

greeter_object.greet()


"""
The decorator is applied to the greet() method.

However, there is an important detail:

    self

is automatically passed to instance methods.

Therefore, when writing decorators for methods, the wrapper
must usually be able to receive self.
"""


# ============================================================
# 6. A METHOD DECORATOR
# ============================================================

def log_method(function):

    def wrapper(*args,**kwargs):
        print(f"Calling method: {function.__name__}")

        result=function(*args,**kwargs)

        print(f"Finished method: {function.__name__}")

        return result

    return wrapper


class Calculator:

    @log_method
    def add(self,first_value,second_value):
        return first_value+second_value


calculator_object=Calculator()

answer=calculator_object.add(10,20)

print("Answer:",answer)


"""
The wrapper receives:

    self
    first_value
    second_value

through:

    *args

The decorator can therefore work with an instance method.
"""


# ============================================================
# 7. WHY *args AND **kwargs ARE USEFUL
# ============================================================

"""
Different methods can have different parameters.

For example:

    def first_method(self,name):
        ...

    def second_method(self,x,y):
        ...

    def third_method(self,value,unit="kg"):
        ...

If our decorator is supposed to work with all of them, it
would be inconvenient to specify every possible parameter.

Using:

    *args
    **kwargs

allows the decorator to accept different arguments and pass
them to the original method.
"""


# ============================================================
# 8. USING functools.wraps
# ============================================================

"""
When a decorator replaces a function with a wrapper, Python's
function metadata can be replaced as well.

For example:

    __name__
    __doc__

The functools module provides:

    @wraps

to preserve this information.
"""


from functools import wraps


def track_call(function):

    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f"Running: {function.__name__}")
        return function(*args,**kwargs)

    return wrapper


class Messenger:

    @track_call
    def send_message(self,message):
        print(f"Message sent: {message}")


messenger_object=Messenger()

messenger_object.send_message("Hello!")


"""
Using @wraps is a good practice when creating custom
decorators.

It keeps useful information about the original function.
"""


# ============================================================
# 9. BUILT-IN DECORATOR: @staticmethod
# ============================================================

"""
Python provides several built-in decorators that are commonly
used with classes.

One of them is:

    @staticmethod

A static method does not automatically receive:

    self

or:

    cls

It behaves like a regular function placed inside a class.
"""


class MathTools:

    @staticmethod
    def square(number):
        return number*number


square_result=MathTools.square(7)

print("Square:",square_result)


"""
The square() method does not need information about a particular
object or the class.

Therefore, @staticmethod is appropriate.
"""


# ============================================================
# 10. BUILT-IN DECORATOR: @classmethod
# ============================================================

"""
Another built-in decorator is:

    @classmethod

A class method receives the class as its first argument.

By convention, this argument is called:

    cls
"""


class Product:

    category="General"

    @classmethod
    def show_category(cls):
        print("Category:",cls.category)


Product.show_category()


"""
Here:

    cls

refers to the Product class.

A class method is useful when the method needs to work with
class-level information.
"""


# ============================================================
# 11. BUILT-IN DECORATOR: @property
# ============================================================

"""
The @property decorator allows a method to be accessed like an
attribute.

For example:
"""


class Employee:

    def __init__(self,name):
        self._name=name

    @property
    def name(self):
        return self._name


employee_object=Employee("Ali")

print(employee_object.name)


"""
Although name() is technically a method, we access it as:

    employee_object.name

instead of:

    employee_object.name()

@property is useful when we want controlled access to an
attribute.
"""


# ============================================================
# 12. THREE IMPORTANT BUILT-IN DECORATORS
# ============================================================

"""
In OOP, three decorators are especially important:

    @staticmethod
        → creates a static method

    @classmethod
        → creates a class method

    @property
        → creates a property

We already learned these decorators in previous chapters.

Now we will focus on creating custom decorators.
"""


# ============================================================
# 13. CUSTOM METHOD DECORATOR: LOGGING
# ============================================================

"""
One practical use of decorators is logging.

Suppose a class has many methods.

Instead of writing:

    print("Method started")
    ...
    print("Method finished")

inside every method, we can create one decorator and reuse it.
"""


def log_activity(function):

    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f"[LOG] {function.__name__} started.")

        result=function(*args,**kwargs)

        print(f"[LOG] {function.__name__} finished.")

        return result

    return wrapper


class BankService:

    @log_activity
    def deposit(self,amount):
        print(f"Depositing ${amount}")

    @log_activity
    def withdraw(self,amount):
        print(f"Withdrawing ${amount}")


bank_service=BankService()

bank_service.deposit(500)
bank_service.withdraw(150)


"""
The logging behavior is added automatically to both methods.

The methods themselves remain focused on their actual work.
"""


# ============================================================
# 14. CUSTOM METHOD DECORATOR: TIMING
# ============================================================

"""
Another common use of decorators is measuring how long a method
takes to execute.

Python's time module provides:

    time.perf_counter()

which can be used to measure elapsed time.
"""


import time


def measure_time(function):

    @wraps(function)
    def wrapper(*args,**kwargs):
        start_time=time.perf_counter()

        result=function(*args,**kwargs)

        end_time=time.perf_counter()

        elapsed_time=end_time-start_time

        print(
            f"{function.__name__} took "
            f"{elapsed_time:.6f} seconds."
        )

        return result

    return wrapper


class DataProcessor:

    @measure_time
    def process_data(self):
        total=0

        for number in range(1,100001):
            total+=number

        return total


processor_object=DataProcessor()

processed_result=processor_object.process_data()

print("Result:",processed_result)


"""
The decorator measures the execution time automatically.

The process_data() method does not need to contain timing code.
"""


# ============================================================
# 15. CUSTOM METHOD DECORATOR: VALIDATING INPUT
# ============================================================

"""
Decorators can also be used to validate method inputs.

For example, suppose a bank account should only allow a
positive deposit amount.

We can create a decorator that checks the amount before the
method runs.
"""


def require_positive(function):

    @wraps(function)
    def wrapper(self,amount,*args,**kwargs):

        if(amount<=0):
            print("Amount must be greater than zero.")
            return None

        return function(
            self,
            amount,
            *args,
            **kwargs
        )

    return wrapper


class SavingsAccount:

    def __init__(self,balance):
        self.balance=balance

    @require_positive
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited: ${amount}")
        print(f"Balance: ${self.balance}")


savings_account=SavingsAccount(1000)

savings_account.deposit(500)

savings_account.deposit(-200)


"""
The decorator checks the input before deposit() executes.

This separates validation logic from the main method logic.
"""


# ============================================================
# 16. A MORE FLEXIBLE VALIDATION DECORATOR
# ============================================================

"""
We can also create a decorator that validates several numeric
arguments.

For simplicity, this example checks that all positional
arguments after self are positive.
"""


def positive_values_only(function):

    @wraps(function)
    def wrapper(self,*args,**kwargs):

        for value in args:

            if isinstance(value,(int,float)) and value<=0:
                print("All numeric values must be positive.")
                return None

        return function(
            self,
            *args,
            **kwargs
        )

    return wrapper


class Order:

    @positive_values_only
    def calculate_total(self,price,quantity):
        total=price*quantity

        print("Total:",total)

        return total


order_object=Order()

order_object.calculate_total(25,3)

order_object.calculate_total(25,-2)


"""
The decorator performs validation before calculate_total()
runs.
"""


# ============================================================
# 17. CUSTOM CLASS DECORATORS
# ============================================================

"""
Decorators are not limited to functions and methods.

A decorator can also modify a class.

A class decorator receives the class itself.

Basic structure:

    def class_decorator(cls):

        ...

        return cls

Then:

    @class_decorator
    class MyClass:
        ...

The decorator receives MyClass.
"""


# ============================================================
# 18. SIMPLE CLASS DECORATOR
# ============================================================

def add_label(cls):

    cls.label="This class has been decorated."

    return cls


@add_label
class Report:

    pass


report_object=Report()

print(report_object.label)


"""
The class decorator added a new class attribute:

    label

to the Report class.

The original class definition did not contain that attribute.
"""


# ============================================================
# 19. CLASS DECORATOR ADDING A METHOD
# ============================================================

"""
A class decorator can also add a method to a class.
"""


def add_description(cls):

    def describe(self):
        print(f"This object belongs to {cls.__name__}.")

    cls.describe=describe

    return cls


@add_description
class Notebook:

    def __init__(self,pages):
        self.pages=pages


notebook_object=Notebook(200)

notebook_object.describe()


"""
The decorator added the describe() method to Notebook.

Therefore, the object can call:

    notebook_object.describe()

even though describe() was not written directly inside the
Notebook class.
"""


# ============================================================
# 20. CLASS DECORATOR FOR AUTOMATIC LOGGING
# ============================================================

"""
A class decorator can be used to automatically decorate methods
inside a class.

For example, suppose we want to log every public method of a
class.

Instead of writing:

    @log_activity
    def method_one():
        ...

    @log_activity
    def method_two():
        ...

we can create a class decorator that applies the method
decorator automatically.
"""


def log_all_methods(cls):

    for name,attribute in cls.__dict__.items():

        if callable(attribute) and not name.startswith("_"):
            setattr(cls,name,log_activity(attribute))

    return cls


@log_all_methods
class Store:

    def add_item(self,item):
        print(f"Adding {item}")

    def remove_item(self,item):
        print(f"Removing {item}")


store_object=Store()

store_object.add_item("Keyboard")
store_object.remove_item("Mouse")


"""
The class decorator examines the class methods and applies
log_activity() to the public methods.

This allows us to add the same behavior automatically to
multiple methods.
"""


# ============================================================
# 21. UNDERSTANDING setattr()
# ============================================================

"""
In the previous example, we used:

    setattr(cls,name,value)

setattr() allows us to set an attribute dynamically.

For example:

    setattr(cls,"name","Ali")

is similar to:

    cls.name="Ali"

And:

    setattr(cls,"greet",some_function)

can add a method to a class.

This is useful when creating class decorators that modify
classes dynamically.
"""


# ============================================================
# 22. CLASS DECORATOR FOR VALIDATION
# ============================================================

"""
A class decorator can also modify or add behavior to a class.

For example, we can add a simple validation method to every
class that uses the decorator.
"""


def add_validator(cls):

    def is_valid(self):
        return bool(self.__dict__)

    cls.is_valid=is_valid

    return cls


@add_validator
class Customer:

    def __init__(self,name):
        self.name=name


customer_object=Customer("Sara")

print("Valid object:",customer_object.is_valid())


"""
The class decorator adds:

    is_valid()

to Customer.

This demonstrates how class decorators can extend a class.
"""


# ============================================================
# 23. METHOD DECORATOR VS CLASS DECORATOR
# ============================================================

"""
A method decorator receives a function or method.

Example:

    def my_method_decorator(function):
        ...

A class decorator receives a class.

Example:

    def my_class_decorator(cls):
        ...

So:

    Method decorator
        → modifies a method/function

    Class decorator
        → modifies a class
"""


# ============================================================
# 24. SIMPLE COMPARISON
# ============================================================

"""
Method decorator:

    @log_activity
    def calculate(self):
        ...

The decorator modifies calculate().

Class decorator:

    @add_label
    class Product:
        ...

The decorator modifies Product.
"""


# ============================================================
# 25. USING BOTH DECORATORS
# ============================================================

"""
A class can use a class decorator and its methods can use method
decorators.

For example:
"""


def add_category(cls):

    cls.category="Utility"

    return cls


@add_category
class NumberTool:

    @log_activity
    def double(self,value):
        return value*2


number_tool_object=NumberTool()

print("Category:",number_tool_object.category)

doubled_value=number_tool_object.double(8)

print("Doubled:",doubled_value)


"""
Here:

    @add_category

is a class decorator.

And:

    @log_activity

is a method decorator.

Both can work together.
"""


# ============================================================
# 26. DECORATOR ORDER
# ============================================================

"""
When multiple decorators are applied to the same method, their
order matters.

For example:

    @first
    @second
    def task():
        ...

Python applies them approximately like:

    task=first(second(task))

Therefore, decorators are applied from the bottom upward.

When using multiple decorators, always pay attention to their
order.
"""


# ============================================================
# 27. EXAMPLE OF MULTIPLE METHOD DECORATORS
# ============================================================

def before_message(function):

    @wraps(function)
    def wrapper(*args,**kwargs):
        print("Before method.")
        return function(*args,**kwargs)

    return wrapper


def after_message(function):

    @wraps(function)
    def wrapper(*args,**kwargs):
        result=function(*args,**kwargs)
        print("After method.")
        return result

    return wrapper


class Demo:

    @before_message
    @after_message
    def show(self):
        print("Inside method.")


demo_object=Demo()

demo_object.show()


"""
The execution order demonstrates that decorator order matters.

The outer decorator receives the result of the inner
decorator.
"""


# ============================================================
# 28. DECORATORS SHOULD RETURN THE ORIGINAL RESULT
# ============================================================

"""
A good general-purpose decorator should normally return the
result of the original function.

For example:

    result=function(*args,**kwargs)

    return result

If we forget to return the result, the decorated function may
unexpectedly return None.
"""


def safe_logger(function):

    @wraps(function)
    def wrapper(*args,**kwargs):

        print(f"Calling {function.__name__}")

        result=function(*args,**kwargs)

        return result

    return wrapper


class Converter:

    @safe_logger
    def convert(self,number):
        return number*100


converter_object=Converter()

converted_value=converter_object.convert(5)

print("Converted:",converted_value)


"""
The return value from convert() is preserved by the decorator.
"""


# ============================================================
# 29. DECORATORS AND self
# ============================================================

"""
When decorating an instance method, remember that the first
argument is normally self.

For example:

    class Person:

        def greet(self,message):
            ...

When calling:

    person.greet("Hello")

Python automatically passes the Person object as self.

Therefore, a method decorator often receives:

    self
    message

through:

    *args

This is why:

    def wrapper(*args,**kwargs):

is commonly used for method decorators.
"""


# ============================================================
# 30. DECORATORS AND cls
# ============================================================

"""
Class methods are different.

For a class method:

    @classmethod
    def create(cls,value):
        ...

Python automatically passes the class as:

    cls

If we create a decorator for class methods, it must preserve
the arguments correctly.

For example:
"""


def trace_class_method(function):

    @wraps(function)
    def wrapper(*args,**kwargs):

        print(f"Calling {function.__name__}")

        return function(*args,**kwargs)

    return wrapper


class Product:

    @classmethod
    @trace_class_method
    def create_default(cls):
        return cls()


product_object=Product.create_default()

print(type(product_object))


"""
The decorator does not need to manually handle cls.

It simply forwards all arguments using:

    *args
    **kwargs

The class method mechanism continues to provide cls.
"""


# ============================================================
# 31. DECORATOR WITH A METHOD THAT RETURNS A VALUE
# ============================================================

"""
Decorators are not limited to methods that print something.

They can also work with methods that return values.
"""


def log_result(function):

    @wraps(function)
    def wrapper(*args,**kwargs):

        result=function(*args,**kwargs)

        print(
            f"{function.__name__} returned {result}"
        )

        return result

    return wrapper


class Calculator:

    @log_result
    def subtract(self,first_number,second_number):
        return first_number-second_number


calculator=Calculator()

difference=calculator.subtract(30,12)

print("Difference:",difference)


"""
The decorator logs the returned value while still returning it
to the caller.
"""


# ============================================================
# 32. PRACTICAL EXAMPLE: ACCESS LOGGING
# ============================================================

"""
Decorators are useful in real applications for automatically
logging important operations.

For example:
"""


def audit(function):

    @wraps(function)
    def wrapper(*args,**kwargs):

        print(
            f"[AUDIT] {function.__name__} was called."
        )

        result=function(*args,**kwargs)

        print(
            f"[AUDIT] {function.__name__} completed."
        )

        return result

    return wrapper


class Account:

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    @audit
    def deposit(self,amount):
        self.balance+=amount
        print(f"New balance: ${self.balance}")

    @audit
    def withdraw(self,amount):
        self.balance-=amount
        print(f"New balance: ${self.balance}")


account_object=Account("Usman",2000)

account_object.deposit(500)
account_object.withdraw(300)


"""
The audit behavior is automatically added to both methods.

This is much cleaner than repeating audit messages inside every
method.
"""


# ============================================================
# 33. PRACTICAL EXAMPLE: VALIDATING A CLASS METHOD
# ============================================================

"""
Decorators can also be combined with class methods.

For example, we can create a class method that creates an object
from a positive value.
"""


def log_creation(function):

    @wraps(function)
    def wrapper(*args,**kwargs):

        print(
            f"Creating object using {function.__name__}"
        )

        return function(*args,**kwargs)

    return wrapper


class Ticket:

    def __init__(self,number):
        self.number=number

    @classmethod
    @log_creation
    def from_number(cls,number):

        if(number<=0):
            raise ValueError(
                "Ticket number must be positive."
            )

        return cls(number)


ticket_object=Ticket.from_number(101)

print("Ticket number:",ticket_object.number)


"""
Here:

    @classmethod

turns from_number() into a class method.

    @log_creation

adds logging behavior.

The two decorators work together.
"""


# ============================================================
# 34. IMPORTANT: DECORATORS DO NOT CHANGE THE ORIGINAL
#     FUNCTION'S SOURCE CODE
# ============================================================

"""
One of the biggest advantages of decorators is that they can
add behavior without requiring us to rewrite the original
function or method.

For example:

    @log_activity
    def deposit(self,amount):
        ...

The deposit() method does not contain the logging code.

The decorator adds that behavior from outside.
"""


# ============================================================
# 35. WHEN TO USE METHOD DECORATORS
# ============================================================

"""
Method decorators are useful when the same behavior needs to be
applied to multiple methods.

Common examples include:

    Logging
    Timing
    Validation
    Authentication
    Authorization
    Caching
    Error handling
    Access control

Instead of repeating the same code in every method, we can
place the common behavior inside a decorator.
"""


# ============================================================
# 36. WHEN TO USE CLASS DECORATORS
# ============================================================

"""
Class decorators are useful when we want to modify or extend
an entire class.

Common examples include:

    Adding methods
    Adding class attributes
    Automatically decorating methods
    Registering classes
    Adding validation behavior
    Configuring classes

A class decorator receives the class and can modify it before
the class is used.
"""


# ============================================================
# 37. METHOD DECORATOR VS CLASS DECORATOR
# ============================================================

"""
                         METHOD DECORATOR
                         -----------------

    Receives:
        A function/method

    Purpose:
        Modify the behavior of one method

    Example:
        @log_activity
        def save(self):
            ...


                         CLASS DECORATOR
                         ----------------

    Receives:
        A class

    Purpose:
        Modify or extend the entire class

    Example:
        @add_label
        class Product:
            ...
"""


# ============================================================
# 38. BUILT-IN VS CUSTOM DECORATORS
# ============================================================

"""
Python provides many decorators.

Some important built-in decorators we have learned are:

    @staticmethod
    @classmethod
    @property

We can also create our own decorators:

    @log_activity
    @measure_time
    @require_positive

The idea is the same:

    A decorator modifies or extends behavior.
"""


# ============================================================
# 39. COMPLETE PRACTICAL EXAMPLE
# ============================================================

"""
Let's combine several ideas into one small example.

We will create:

    1. A method decorator for logging.
    2. A method decorator for validation.
    3. A class that uses those decorators.
"""


def log_action(function):

    @wraps(function)
    def wrapper(*args,**kwargs):

        print(
            f"[LOG] {function.__name__} called."
        )

        result=function(*args,**kwargs)

        print(
            f"[LOG] {function.__name__} finished."
        )

        return result

    return wrapper


def validate_score(function):

    @wraps(function)
    def wrapper(self,score,*args,**kwargs):

        if (not 0<=score<=100):
            print(
                "Score must be between 0 and 100."
            )
            return None

        return function(
            self,
            score,
            *args,
            **kwargs
        )

    return wrapper


class Student:

    def __init__(self,name):
        self.name=name
        self.score=0

    @log_action
    @validate_score
    def update_score(self,score):
        self.score=score

        print(
            f"{self.name}'s score is now "
            f"{self.score}."
        )


student_object=Student("Amina")

student_object.update_score(85)

student_object.update_score(120)


"""
Here:

    @log_action

logs the method call.

    @validate_score

checks the input.

The actual update_score() method remains simple and focused on
updating the score.
"""


# ============================================================
# 40. IMPORTANT POINT ABOUT DECORATOR ORDER
# ============================================================

"""
In the previous example:

    @log_action
    @validate_score
    def update_score(...):
        ...

The effective order is:

    update_score=log_action(
        validate_score(update_score)
    )

Therefore, changing the decorator order can change the
behavior.

When using multiple decorators, understand which decorator
should run first.
"""


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. A decorator modifies or extends the behavior of another
   function or class.

2. Decorators allow us to add behavior without changing the
   original function's main code.

3. A method is a function defined inside a class, so methods can
   also be decorated.

4. A method decorator receives a function/method.

5. A class decorator receives a class.

6. A common method decorator structure is:

       def decorator(function):

           @wraps(function)
           def wrapper(*args,**kwargs):
               ...
               return function(*args,**kwargs)

           return wrapper

7. *args and **kwargs allow a decorator to work with methods
   having different parameters.

8. When decorating instance methods, self is normally included
   in the arguments automatically.

9. When decorating class methods, cls is automatically provided
   by the @classmethod mechanism.

10. functools.wraps is useful because it preserves metadata
    such as the original function's name and documentation.

11. Python provides several important built-in decorators.

12. @staticmethod creates a static method.

13. @classmethod creates a class method.

14. @property creates a property that can be accessed like an
    attribute.

15. Custom method decorators can be used for:

       Logging
       Timing
       Validation
       Authentication
       Error handling
       Caching

16. A logging decorator can automatically record when a method
    starts and finishes.

17. A timing decorator can measure how long a method takes to
    execute.

18. A validation decorator can check method arguments before
    allowing the method to run.

19. A class decorator receives the class itself.

20. A class decorator can add attributes to a class.

21. A class decorator can add methods to a class.

22. A class decorator can also automatically apply method
    decorators to multiple methods.

23. A simple class decorator has the form:

       def decorator(cls):
           ...
           return cls

24. A method decorator has the form:

       def decorator(function):
           ...
           return wrapper

25. Method decorators affect individual methods.

26. Class decorators affect the entire class.

27. Multiple decorators can be applied to the same method.

28. Decorator order matters.

29. For:

       @first
       @second
       def function():
           ...

    Python effectively performs:

       function=first(second(function))

30. A decorator should normally return the original function's
    result when the result needs to be preserved.

31. Decorators help avoid repeating common code across many
    methods.

32. They can make classes cleaner by separating common
    behavior from the main business logic.

33. Decorators are especially useful when the same behavior must
    be applied consistently.

34. The main idea is:

       Method decorator
           → modifies method behavior

       Class decorator
           → modifies class behavior

35. Built-in decorators such as @staticmethod, @classmethod,
    and @property are examples of how Python uses decorators
    to provide special behavior.

36. Custom decorators allow us to create our own reusable
    behavior.

The most important idea to remember is:

    Decorators allow us to add or modify behavior without
    rewriting the original function, method, or class.

This completes the main OOP decorator concepts in this folder.
The next chapter will introduce Dataclasses and show how
Python can reduce boilerplate code when creating classes that
mainly store data.
"""