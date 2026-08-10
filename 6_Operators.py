"""
Operators:

Operators are special symbols or words used in programming to perform operations
on values or variables.

1. Arithmetic Operators

Used for mathematical calculations.

Operator	                   Meaning	
+	                           Addition (Adds two numbers together)
-	                           Subtraction	(Subtracts the second number from the first)
*	                           Multiplication (Multiplies two numbers)
/	                           Division (Divides the first number by the second and gives the full answer with decimals)
Double forward slash(//)       Floor Division (Divides two numbers but chops off the decimal part to give you just the whole number)	
%	                           Modulus (Divides two numbers and gives you only the leftover remainder)
**                             Exponent (Raises the first number to the power of the second (e.g., Square of 5))

"""

# Arithmetic operators

a=10
b=8
print("==Arithmetic Operators==")
print("Addition:",a+b)
print("Subtraction:",a-b)
print("Mulltiplication:",a*b)
print("Division:",a/b)
print("Floor Division:",a//b)
print("Modulus:",a%b)
print("Exponent:",a**b)
print() # Adding this so that next output should be displayed in next line


"""
2. Comparison (Relational) Operators

Used to compare values. Result is True or False.

Operator	Meaning
==	        Equal to (Returns true if two values are equal otherwise false (e.g., 5 == 5 is True))
!=	        Not equal to
>	        Greater than
<	        Less than
>=	        Greater than or equal to
<=	        Less than or equal to

"""

# Conditional (Relational) Operators

print("==Conditional Operators==")
print("a is equal to b:",a==b)
print("a is not equal to b:",a!=b)
print("a is greater than b:",a>b)
print("a is less than b:",a<b)
print("a is greater than or equal to b:",a>=b)
print("a is less than or equal to b:",a<=b)
print() # Adding this so that next output should be displayed in next line


"""
3. Assignment Operators

Used to assign values to variables.

Operator	Example
=	        x = 5 (Gives a variable a specific value (e.g., sets x to 5).)
+=	        x += 2 (It is same as x = x + 2)
-=	        x -= 2 (It is same as x = x - 2)
*=	        x *= 2 (It is same as x = x * 2)
/=	        x /= 2 (It is same as x = x / 2)

"""

# Assingment Operators

print("==Assignment Operators==")
x=5 
print("x =",x)
x+=5
print("After x = x + 5 value of x is:",x)
x-=5
print("After x = x - 5 value of x is:",x)
x*=5
print("After x = x * 5 value of x is:",x)
x/=5
print("After x = x / 5 value of x is:",x)
print() # Adding this so that next output should be displayed in next line


"""
4. Logical Operators

Used to combine conditions.

Operator	Meaning
and	        True if both conditions are true
or	        True if at least one condition is true
not	        Reverses the result (True to false and false to true)

"""

# Logical Operators

print("==Logical Operators==")
y=10
print("y<20 and y>9:",y<20 and y>9)
print("y>20 or y<11:",y>20 or y<11)
print("not(y>9):",not(y>9))
print() # Adding this so that next output should be displayed in next line