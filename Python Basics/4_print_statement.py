"""
The print statement:-
The print() statement in Python is used to display output on the screen.
--> It is used to show text, numbers, or variable values to the user.

"""

print("Hello World")
print("Hello World",1,2,14.5)

"""
Some useful parameters:-
In print() function we have some parameters:

(i) sep:-
sep means separator.
--> It defines what should appear between multiple values.
--> By default, Python uses a space to seperate values in a single print statement.

Syntax:-
print(value1,value2,...,sep="use anything a character, a special character etc.")

(ii) end:-
end defines what should be printed at the end of the output.
--> By default, Python prints a new line at the end of the output.

Syntax:-
print(value,end="use a space or something else(anything)")

"""

# sep

print(1,2,3,sep="~") # Output: 1~2~3

# end

print("Hello")
print("World")

# First Hello should be printed and than in a new line World should be printed. 

print("Hello",end=" ")
print("World")

# First Hello should be printed and than after a space not in a new line World should be printed.
 