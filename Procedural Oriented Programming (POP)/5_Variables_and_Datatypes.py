"""

(1) Data types:-
A data type defines the kind of data a variable can store.

--> Python is dynamically typed object oriented programming language. In other programming languages like C++
we have to write data types with variables but in python we don't have to mention data type.

(i) str:-
str --> string data type (charater, words, sentences, paragraphs etc.).
Strings can br written in double quotes ("") as well as in single quotes ('').

(ii) int:-
int --> integer data type (numbers).

(iii) float:-
float --> Decimal values (12.3,1.5823 etc)

(iv) bool:-
bool --> Stores boolean values (true or false).

(v) None:-
None --> It is used when a variable currently has no value or an empty value assigned to it.
This data type is commonly used when we want to decalre a variable instead of initializing it. 

(2) Variable:
A variable is like a container or named memory location used to store data.

Syntax:-
var_name=data

e.g name="your_name"

Rules for creating variables:-

--> Variable names cannot start with a number. (1name ❌, name1 ✅)
--> Variable names can contains: letters (a-z, A-Z), numbers (0-9), underscores (_)
--> Spaces are not allowed in variable names. (user name ❌, user_name ✅)
--> Special characters are not allowed. (user-name, name@ ❌, username ✅)
--> Variable names are case sensitive. (name and Name are different variables)
--> Python reserved keywords cannot be used as variable names. (class, for, if ❌)
--> Use meaningful and readable variable names.
--> Underscores are allowed and commonly used.

"""

a="string" # we can also wrtie it as 'string'
b=10
c=12.4
d=True
e=None

# To check which type of data is stored in a variable we can use type() function.

print("Data type of variable a is:",type(a))
print("Data type of variable b is:",type(b))
print("Data type of variable c is:",type(c))
print("Data type of variable d is:",type(d))
print("Data type of variable e is:",type(e))

# Now i want to give some data in variable e

e=19

print("Data type of variable e is:",type(e))

# Creating multiple variable in a single line with two different conditions

# First Condition

name,age,percentage="Ahmad",16,70.76  # In this condition first value is assign to first varibale and so on.

print("name:",name)
print("age:",age)
print("percentage:",percentage)

# Second Condition

x=y=z=100  # In this condition the same value is assigned to all varibales.

print("x:",x)
print("y:",y)
print("z:",z)


