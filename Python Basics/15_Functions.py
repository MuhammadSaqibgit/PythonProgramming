"""
Functions

A function is a block of code that performs a specific task whenever
it is called. Functions make large programs organized and neat.

Types of functions:
1) Built-in functions
2) User-defined functions
"""

"""
Built-in Functions:

These functions are pre-defined in Python.

Examples: min(), max(), len(), sum(), type(), range(), dict(),
list(), tuple(), set(), print(), etc.
"""
numbers=[10,20,5,40]
print(min(numbers))
print(max(numbers))
print(len(numbers))
print(sum(numbers))
print(type(numbers))


"""
User-defined Functions:

User-defined functions are defined by the programmer to perform
specific tasks according to our needs.

Syntax:
def function_name(parameters):
    # function code
"""
def sum_numbers(a,b):
    print(a+b)


"""
Calling a Function:

We call a function by giving the function name followed by
parameters (if any) in parentheses.
"""
def full_name(fname,lname):
    print("Hello,",fname,lname)

full_name("Muhammad","Saqib")


"""
Calling a function using user input:
"""
def add(a,b):
    print(a+b)

x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
add(x,y)


"""
Returning Value From Function:

A function can return a value using the return keyword.

Syntax:
return expression


(i) Assignment Statement:

The returned value can be stored in a variable.
"""
def cube(num):
    return num*num*num

n=int(input("Enter a number: "))
c=cube(n)
print("Cube is:",c)


"""
(ii) Arithmetic Expression:

The returned value can be used directly in an arithmetic expression.
"""
def cube1(num):
    return num*num*num

n1=int(input("Enter a number: "))
c1=5+cube1(n1)
print(c1)


"""
(iii) Output Statement:

The returned value can be used directly in an output statement.
"""
def cube2(num):
    return num*num*num

n2=int(input("Enter a number: "))
print("Cube is:",cube2(n2))


"""
Function Arguments:

Types of function arguments:
1) Default arguments
2) Positional arguments
3) Keyword arguments
4) Required arguments
5) Variable-length arguments
"""


"""
(i) Default Arguments:

A default value can be provided while creating a function.
The default value can be changed while calling the function.
"""
def sum_default(a=10,b=13):
    print(a+b)

sum_default()
sum_default(20,15)


"""
(ii) Positional Arguments:

Arguments passed to a function in a specific order are
called positional arguments.
"""
def info(name,age):
    print(name,age)

info("Muhammad Saqib",18)


"""
A positional argument can also have a default value.
"""
def info1(name,age=20):
    print(name,age)

info1("Muhammad Saqib",18)


"""
(iii) Keyword Arguments:

Arguments can be provided using key=value. The parameter name
identifies the argument.
"""
def name_info(fname,mname,lname):
    print(fname,mname,lname)

name_info(lname="Akram",fname="Muhammad", mname="Waseem")


"""
(iv) Required Arguments:

Required arguments are parameters that must be provided when
calling a function.
"""
def sum_required(a,b):
    print(a+b)

sum_required(10,12)

# sum_required(10)  # Raises TypeError because b is required.


"""
(v) Variable-Length Arguments:

Sometimes we need to pass more arguments than the parameters
defined in the function.

Types:
(i) Arbitrary arguments (*args)
(ii) Keyword arbitrary arguments (**kwargs)
"""


"""
(i) Arbitrary Arguments:
Passing a tuple to a function.

A * before the parameter name collects the arguments as a tuple.
"""
def passing_tuple(*adding):
    print("Arguments:",adding)
    print("Sum:",sum(adding))

passing_tuple(20,21,20,22,25,27,29,30)


"""
Example of *args with a normal parameter:
"""
def example(name,*numbers):
    print("Name:",name)
    print("Numbers:",numbers)

example("Saqib",1,2,3,4,5)


"""
(ii) Keyword Arbitrary Arguments:
Passing a dictionary to a function.

A ** before the parameter name collects keyword arguments
as a dictionary.
"""
def info_person(**kwargs):
    for key,value in kwargs.items():
        print(key,value)


info_person(name="Muhammad Saqib",age=18)
info_person(name="Muhammad Ahmad")


"""
Passing normal arguments, *args and **kwargs together:
"""
def info_person1(programmer,*args,**kwargs):
    if(programmer==True):
        print("Programmer")
    else:
        print("Not a Programmer")
    
    for i in args:
        print(i,end=" ")
    print()

    for key,value in kwargs.items():
        print(key,value)

info_person1(True,1,2,3,4,5,name="Muhammad Saqib",age=18)


"""
Functions and Lists:

(i) Calling a function with a list parameter.
"""
def list_passing(numbers):
    for i in numbers:
        print(i)

list_of_numbers=[10,20,30,40,50]
list_passing(list_of_numbers)


"""
(ii) Passing individual list elements to a function.
"""
def square(num):
    print(num,"=",num*num)


list1=[2,3,4,5,6,7,8]

for i in range(0,len(list1),1):
    square(list1[i])


"""
(iii) Passing a 2D list to a function.
"""
def maximum(numbers):
    m=numbers[0][0]
    for i in range(0,len(numbers),1):
        for j in range(0,len(numbers[i]),1):
            if(numbers[i][j]>m):
                m=numbers[i][j]
    return m


list_of_numbers1=[[1,2],[3,4],[5,6]]
maximum_value=maximum(list_of_numbers1)
print("Maximum:",maximum_value)


"""
Functions and Sets:

(i) Passing a set to a function.
"""
def display_set(my_set):
    for item in my_set:
        print(item)

numbers1={1,2,3,4,5}
display_set(numbers1)


"""
(ii) Modifying a set inside a function.
"""
def add_element(my_set,element):
    my_set.add(element)

numbers2={1,2,3}
add_element(numbers2,4)
print(numbers2)


"""
(iii) Returning a set from a function.
"""
def return_set_of_even_numbers(my_set):
    even_set=set()
    for i in my_set:
        if(i%2==0):
            even_set.add(i)
    return even_set

set1={1,2,3,4,5,6,7,8,9,10}
even_numbers_set=return_set_of_even_numbers(set1)
print(even_numbers_set)


"""
Function Overloading:

Python does not support traditional function overloading:
defining the same function name again replaces the previous
definition. Similar behavior can be achieved using default
or variable-length arguments.
"""
def average(a=None,b=None,c=None,d=None):
    values=[x for x in (a,b,c,d) if x is not None]
    return sum(values)/len(values)

print(average(10, 20))
print(average(10, 20, 30, 40))


"""
Recursion:

The programming technique in which a function calls itself
is known as recursion.

A recursive function has a base condition and a recursive call.
"""
def factorial(n):
    if(n<=0):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))


"""
Local Variables:

A variable declared inside a function is known as a local variable.
Local variables are also called automatic variables.

Scope:
A local variable can be used only inside the function in which
it is declared.
"""
def my_function():
    x=5
    print("Local x:",x)

my_function()


"""
Scope:

The area where a variable can be accessed is known as its scope.
"""
def calculate():
    local_value=20
    print("Inside function:",local_value)

calculate()


"""
Global Variables:

A variable declared outside any function is known as a global variable.

Scope:
Global variables can be used by all functions in the program.
"""
x1=10

def my_function():
    y1=5
    print("The sum of x1 and y1 is:",x1+y1)

my_function()


"""
Global and Local Variable With Same Name:

A global and local variable can have the same name.
Inside the function, the local variable has priority.
"""
x2=10

def my_function():
    x2=5
    print("Local x2:",x2)

my_function()
print("Global x2:",x2)


"""
Accessing a Global Variable Inside a Function:
"""
x3=10

def my_function():
    print("Global x3:",x3)

my_function()


"""
global Keyword:

The global keyword is used to modify the value of a global
variable within a function.
"""
x4=10

def my_function():
    global x4
    x4=8

my_function()
print("Modified global x4:", x4)


"""
Nested Functions:

A nested function is a function defined inside another function.
The inner function is accessible within the outer function.
"""
def outer():
    print("This is the outer function")
    def inner():
        print("This is the inner function")
    inner()

outer()


"""
Returning an Inner Function:

An outer function can return its inner function.
"""
def outer():
    def inner():
        return "Hello from inner function"
    return inner


func=outer()
print(func())
