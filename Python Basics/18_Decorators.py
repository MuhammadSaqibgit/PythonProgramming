"""
DECORATORS
"""

# ============================================================
# 1. INTRODUCTION TO DECORATORS
# ============================================================

"""
A decorator is a function that modifies or extends the behavior
of another function without changing the original function code.

A decorator normally takes a function as an argument and returns
a new function.
"""

def greet():
    print("Hello!")


# ============================================================
# 2. FUNCTIONS AS FIRST-CLASS OBJECTS
# ============================================================

"""
Python functions are first-class objects.

This means a function can be:
1. Stored in a variable.
2. Passed as an argument.
3. Returned from another function.
4. Stored in a data structure.
"""

def say_hello():
    print("Hello from Python!")

message=say_hello
message()

print("Function name:", message.__name__)


# ============================================================
# 3. PASSING FUNCTIONS AS ARGUMENTS
# ============================================================

"""
A function can be passed to another function as an argument.

Syntax:

def execute(function):
    function()
"""

def welcome():
    print("Welcome to Python!")

def execute_function(function):
    function()

execute_function(welcome)


# ============================================================
# 4. RETURNING FUNCTIONS FROM FUNCTIONS
# ============================================================

"""
A function can return another function.

This concept is important for understanding decorators.
"""

def outer_function():
    def inner_function():
        print("Hello from inner function!")
    return inner_function

returned_function=outer_function()
returned_function()


# ============================================================
# 5. NESTED FUNCTIONS
# ============================================================

"""
A nested function is a function defined inside another function.

The inner function can normally be used inside the scope of
the outer function.
"""

def outer():
    print("Outer function")
    def inner():
        print("Inner function")
    inner()
outer()


# ============================================================
# 6. CREATING A SIMPLE DECORATOR
# ============================================================

"""
A basic decorator:
1. Receives the original function.
2. Defines a wrapper function.
3. Adds extra behavior.
4. Calls the original function.
5. Returns the wrapper.
"""

def simple_decorator(function):
    def wrapper():
        print("Before the function")
        function()
        print("After the function")
    return wrapper

def greet_user():
    print("Hello, user!")

decorated_greet=simple_decorator(greet_user)
decorated_greet()


# ============================================================
# 7. @ DECORATOR SYNTAX
# ============================================================

"""
Python provides @ syntax as a shorter way to apply a decorator.

The following:

@decorator
def function():
    pass

is equivalent to:

def function():
    pass

function=decorator(function)
"""

def decorator(function):
    def wrapper():
        print("Starting...")
        function()
        print("Finished.")
    return wrapper

@decorator
def show_message():
    print("Hello from decorated function!")

show_message()


# ============================================================
# 8. DECORATORS WITH FUNCTION ARGUMENTS
# ============================================================

"""
If the original function accepts arguments, the wrapper must
also accept those arguments.
"""

def argument_decorator(function):
    def wrapper(name):
        print("Before function")
        function(name)
        print("After function")
    return wrapper

@argument_decorator
def greet_person(name):
    print("Hello,",name)

greet_person("Muhammad Saqib")


"""
Example with two arguments:
"""

def add_decorator(function):
    def wrapper(a,b):
        print("Adding numbers...")
        function(a,b)
    return wrapper

@add_decorator
def add(a,b):
    print("Sum:",a+b)

add(10,20)


# ============================================================
# 9. *args AND **kwargs IN DECORATORS
# ============================================================

"""
*args collects positional arguments into a tuple.

**kwargs collects keyword arguments into a dictionary.

Using both allows a decorator to work with functions having
different arguments.
"""

def flexible_decorator(function):
    def wrapper(*args,**kwargs):
        print("Before function")
        function(*args,**kwargs)
        print("After function")
    return wrapper


@flexible_decorator
def student_info(name,age):
    print("Name:",name)
    print("Age:",age)

student_info("Muhammad Saqib",18)


@flexible_decorator
def calculate(a,b,c):
    print("Total:",a+b+c)

calculate(10,20,30)


# ============================================================
# 10. DECORATORS WITH RETURN VALUES
# ============================================================

"""
If the original function returns a value, the wrapper should
return that value as well.

Otherwise, the decorated function may return None.
"""

def return_decorator(function):
    def wrapper(*args,**kwargs):
        print("Calling function")
        result=function(*args,**kwargs)
        print("Function completed")
        return result
    return wrapper

@return_decorator
def multiply(a,b):
    return a*b

result=multiply(5,4)
print("Result:",result)


# ============================================================
# 11. MULTIPLE DECORATORS
# ============================================================

"""
More than one decorator can be applied to the same function.

Syntax:

@decorator_one
@decorator_two
def function():
    pass

This is equivalent to:

function=decorator_one(decorator_two(function))
"""

def decorator_one(function):
    def wrapper():
        print("Decorator One - Before")
        function()
        print("Decorator One - After")
    return wrapper

def decorator_two(function):
    def wrapper():
        print("Decorator Two - Before")
        function()
        print("Decorator Two - After")
    return wrapper

@decorator_one
@decorator_two
def show():
    print("Original function")

show()


# ============================================================
# 12. DECORATOR EXECUTION ORDER
# ============================================================

"""
When multiple decorators are used, the decorator closest to the
function is applied first.

For:

@A
@B
def function():
    pass

Python creates:

function=A(B(function))

During execution, A is the outer wrapper and B is the inner
wrapper.
"""

def first(function):
    def wrapper():
        print("First - Before")
        function()
        print("First - After")
    return wrapper

def second(function):
    def wrapper():
        print("Second - Before")
        function()
        print("Second - After")
    return wrapper

@first
@second
def test():
    print("Original function")

test()


# ============================================================
# 13. functools.wraps
# ============================================================

"""
A decorator can replace the original function with a wrapper.
Without special handling, the wrapper can hide the original
function's metadata such as its name and documentation.

functools.wraps copies important metadata from the original
function to the wrapper.

Syntax:

from functools import wraps
"""

from functools import wraps


def metadata_decorator(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        return function(*args,**kwargs)
    return wrapper

@metadata_decorator
def calculate_square(number):
    """Returns the square of a number."""
    return number*number

print("Function name:",calculate_square.__name__)
print("Documentation:",calculate_square.__doc__)
print("Result:",calculate_square(5))


# ============================================================
# 14. PRACTICAL USE OF DECORATORS
# ============================================================

"""
Decorators are useful when the same additional behavior needs
to be applied to multiple functions.

Common uses include:
- Logging
- Authentication
- Authorization
- Validation
- Timing
- Caching
"""

def logging_decorator(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print("Calling:",function.__name__)
        result=function(*args,**kwargs)
        print("Finished:",function.__name__)
        return result
    return wrapper

@logging_decorator
def calculate_sum(a,b):
    return a+b

print("Sum:", calculate_sum(10,20))


"""
Example of validation:
"""

def positive_number(function):
    @wraps(function)
    def wrapper(number):
        if(number<0):
            print("Error: Number must not be negative.")
            return None
        return function(number)
    return wrapper

@positive_number
def square_number(number):
    return number*number

print("Square:",square_number(5))
print("Square:",square_number(-5))


# ============================================================
# 15. BUILT-IN DECORATORS
# ============================================================

"""
Python provides decorators that are commonly used with classes
and methods.

Important built-in decorators include:

@staticmethod
    Creates a method that does not automatically receive self.

@classmethod
    Creates a method that receives the class as its first argument.

@property
    Allows a method to be accessed like an attribute.

These decorators are especially important in OOP. So we learn it 
while we are learning OOP.
"""


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. Functions are first-class objects.
2. Functions can be passed as arguments.
3. Functions can return other functions.
4. Nested functions are commonly used in decorators.
5. A decorator modifies or extends function behavior.
6. @ syntax is the short syntax for applying a decorator.
7. *args and **kwargs make decorators flexible.
8. Decorators should preserve return values when appropriate.
9. Multiple decorators can be applied to one function.
10. The decorator closest to the function is applied first.
11. functools.wraps preserves function metadata.
12. Decorators are useful for reusable functionality such as
    logging and validation.

END OF CHAPTER 12: DECORATORS
"""
