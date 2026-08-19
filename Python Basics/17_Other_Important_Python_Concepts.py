"""
OTHER PYTHON CONCEPTS
"""

# ============================================================
# 1. format() METHOD OF STRINGS
# ============================================================

"""
The format() method is used to format strings by inserting values
into placeholders {}.

Syntax:
"string {}".format(value)
"""

name="Muhammad Saqib"
age=18

print("My name is {} and I am {} years old.".format(name,age))

"""
Positional indexes can be used to control the position of values.

The index starts from 0.
"""

print("My name is {1} and I am {0} years old.".format(age,name))


# ============================================================
# 2. f-STRINGS
# ============================================================

"""
f-strings provide a concise and readable way to embed expressions
inside string literals by using curly braces {}.

Syntax:
f"Text {expression}"
"""

name1="Muhammad Saqib"
age1=18

print(f"My name is {name1} and I am {age1} years old.")

"""
Expressions can also be written inside the curly braces.
"""

x=5
y=10

print(f"Sum: {x+y}, Product: {x*y}")

"""
Formatting numbers can be done inside an f-string.
"""

pi=3.14159265

print(f"Pi: {pi:.2f}")


"""
Using dictionaries with f-strings:
"""

person={"name":"Saqib","age":18}

print(f"Name: {person['name']}, Age: {person['age']}")


# ============================================================
# 3. DOCSTRINGS
# ============================================================

"""
Docstrings are string literals that appear immediately after the
definition of a function, method, class, or module.

Docstrings are different from comments. Comments are ignored by
the Python interpreter, while docstrings can be accessed by Python.
"""

def square(n):
    """
    Takes a number and returns the square of the number.
    """
    return n*n

print(square(5))
print(square.__doc__) # Used to print the doc string written inside square function,


# ============================================================
# 4. PEP 8
# ============================================================

"""
PEP 8 is a Python Enhancement Proposal that provides guidelines
and best practices for writing Python code.

It helps programmers write code that is clean, readable,
consistent, and maintainable.

Example of readable PEP 8 style:
"""

first_number=10
second_number=20

total=first_number+second_number

print("Total:",total)


# ============================================================
# 5. ZEN OF PYTHON
# ============================================================

"""
The Zen of Python is a collection of guiding principles for
writing clean, readable, and maintainable Python code.

It can be viewed by importing this module:
"""

import this


# ============================================================
# 6. EXCEPTIONAL HANDLING (ERROR HANDLING)
# ============================================================

"""
Exception handling is done using try and except blocks to handle
runtime errors and prevent the program from crashing.

Syntax:

try:
    # code that may cause an exception
except:
    # code executed when an exception occurs
"""

try:
    result=10/0
except ZeroDivisionError:
    print("Error: Cannot divide by zero")


# ============================================================
# HANDLING MULTIPLE EXCEPTIONS
# ============================================================

"""
Different except blocks can be used to handle different types
of exceptions.
"""

try:
    num=int(input("Enter a number for multiple-exception example: "))
    print(12/num)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Invalid input")


# ============================================================
# USING A GENERIC EXCEPTION
# ============================================================

"""
Exception can be used as a generic exception handler.

The exception object can be stored using "as".
"""

try:
    result1=10/0
except Exception as error:
    print("Error:", error) # error stores the exception object that occurred.


# ============================================================
# finally BLOCK
# ============================================================

"""
The finally block always executes, whether an exception occurs
or not.

Syntax:

try:
    # code
except:
    # error handling
finally:
    # always executed
"""

try:
    result2=10/0
except Exception as error:
    print("Error:", error)
finally:
    print("I am always executed!")


# ============================================================
# else BLOCK WITH EXCEPTION HANDLING
# ============================================================

"""
The else block runs when no exception occurs in the try block.

Structure:

try:
    # code
except:
    # error handling
else:
    # runs if no exception occurs
"""

try:
    result3=10/2
except Exception as error:
    print("Error:",error)
else:
    print("No exception occurred.")
    print("Result:",result3)


# ============================================================
# RAISING BUILT-IN EXCEPTIONS
# ============================================================

"""
Python allows us to raise an exception using the raise keyword.

This is useful when we want to create an error based on a
specific custom condition.
"""

age2=15

try:
    if(age2<0):
        raise ValueError("Age cannot be negative")
    print("Valid age:",age2)
except ValueError as error:
    print("Error:", error)


# ============================================================
# CREATING CUSTOM EXCEPTIONS USING A CLASS
# ============================================================

"""
A custom exception can be created by defining a class that
inherits from Exception.

Syntax:

class MyError(Exception):
    pass
"""

class MyError(Exception):
    """Custom Exception."""
    pass

"""
It's a placeholder you use when Python's syntax requires 
something to be written (like a body for a class, function, 
loop, or if-statement), but you don't actually want to write 
any code there yet.

It is used for declaring a class, and a function.
"""

age3=0

if(age3<=0):
    raise MyError("Age cannot be zero and negative")
else:
    if(age3>=18):
        print("You can drive")
    else:
        print("You cannot drive")


# ============================================================
# 7. enumerate() FUNCTION
# ============================================================

"""
The enumerate() function adds a counter to an iterable and returns
an enumerate object.

It is useful when we need both the index and the value while
looping through an iterable.

Syntax:
enumerate(iterable, start=0)
"""

fruits=["apple","banana","cherry"]

for index,fruit in enumerate(fruits):
    print(index,fruit)


"""
Changing the starting index:
"""

for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)


"""
Using enumerate() with a tuple:
"""

colors=("red","green","blue")

for index,color in enumerate(colors):
    print(index,color)


"""
Using enumerate() with a string:
"""

text="Python"

for index,character in enumerate(text):
    print(index,character)


"""
Converting enumerate() to a list:
"""

numbers=[10,20,30]

enumerated_numbers=list(enumerate(numbers))

print(enumerated_numbers)


# ============================================================
# 8. IMPORTING IN PYTHON
# ============================================================

"""
Importing in Python is the process of bringing code from a Python
module into the current script.

This allows us to use functions and variables defined in modules.
"""

import math

result4=math.sqrt(16)

print("Square root:",result4)


# ============================================================
# from KEYWORD
# ============================================================

"""
Specific functions or variables can be imported from a module
using the from keyword.

Syntax:
from module import name
"""

from math import sqrt,pi

print("Square root:",sqrt(25))
print("Pi:",pi)


# ============================================================
# IMPORTING EVERYTHING USING *
# ============================================================

"""
It is possible to import all functions and variables from a module
using the * wildcard.

However, this is generally not recommended because it can cause
confusion and make code harder to understand.
"""

from math import *

print("Square root:",sqrt(36))


# ============================================================
# IMPORTING WITH an ALIAS USING as
# ============================================================

"""
Python allows an imported module to be renamed using the as keyword.

This can be useful for shorter or more descriptive names.

Syntax:
import module as alias
"""

import math as m

result5=m.sqrt(49)

print("Square root:",result5)


# ============================================================
# 9. dir() FUNCTION
# ============================================================

"""
The dir() function is a built-in function that can be used to view
the names of functions, variables, and other attributes defined
in an object or module.

It is useful for exploring the contents of a module.
"""

import math

print(dir(math))


# ============================================================
# 10. __name__=="__main__"
# ============================================================

"""
Every Python script has a built-in variable called __name__.

When a script is executed directly:
    __name__=="__main__"

When the script is imported as a module:
    __name__ contains the module's name.

The following code runs only when this file is executed directly.
"""

def greet():
    print("Hello World!")


if __name__=="__main__":
    greet()


# ============================================================
# 11. LAMBDA FUNCTION
# ============================================================

"""
A lambda function is a small anonymous function without a name.

It is defined using the lambda keyword.

Syntax:
lambda arguments: expression

Lambda functions are often used when a small function is required
for a short period of time.
"""

double=lambda x:x*2

print("Double:",double(5))


"""
Another example:
"""

multiply=lambda x,y:x*y

print("Product:",multiply(4,5))


"""
Printing a multiplication table using lambda:
"""

table=lambda x, y: print(f"{x} x {y} = {x * y}")

number=5

for i in range(1,11):
    table(number,i)


# ============================================================
# 12. map()
# ============================================================

"""
map() applies a function to every item in an iterable and returns
a map object.

Syntax:
map(function,iterable)
"""

def cube(x):
    return x**3

numbers1=[2,3,4,5,6]

cube_values=list(map(cube,numbers1))

print("Cubes:",cube_values)


# ============================================================
# 13. filter()
# ============================================================

"""
filter() filters items from an iterable based on a condition.

It returns only the items for which the function returns True.

Syntax:
filter(function,iterable)
"""

def greater_than_5(x):
    return x>5

numbers2=[2,3,4,5,6,7]

filtered_numbers=list(filter(greater_than_5,numbers2))

print("Numbers greater than 5:",filtered_numbers)


# ============================================================
# 14. reduce()
# ============================================================

"""
reduce() combines items of an iterable cumulatively and reduces
them to a single value.

reduce() is available from the functools module.

Syntax:

from functools import reduce
reduce(function,iterable)
"""

from functools import reduce

def product(x,y):
    return x*y

numbers3=[1,2,3,4,5,6]

result6=reduce(product,numbers3)

print("Product:",result6)
