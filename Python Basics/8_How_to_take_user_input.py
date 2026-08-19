# ============================================================
# PYTHON TUTORIAL: HOW TO TAKE USER INPUT
# ============================================================
#
# In Python, we use the input() function to take information
# from the user through the keyboard.
#
# IMPORTANT:
# input() always returns the user's answer as a STRING (str).
#
# Example:
# name=input("What is your name? ")
#
# ============================================================


# ------------------------------------------------------------
# BASIC USER INPUT
# ------------------------------------------------------------

print("Hello! Let's learn how to take user input.")

name=input("What is your name? ")

print("Hello,",name)


# ------------------------------------------------------------
# USING INPUT WITH A VARIABLE
# ------------------------------------------------------------

# We can store the user's input in a variable.

age=input("How old are you? ")

print("You are",age,"years old.")


# ------------------------------------------------------------
# INPUT() ALWAYS RETURNS A STRING
# ------------------------------------------------------------

# Even if the user enters a number, input() gives us a string.

number=input("Enter a number: ")

print("The value you entered is:",number)
print("The type of this value is:",type(number))

# If the user enters:
# 25
#
# Python sees it as:
# "25"
#
# NOT:
# 25


# ------------------------------------------------------------
# CONVERTING USER INPUT TO AN INTEGER
# ------------------------------------------------------------

# If we want to perform mathematical calculations,
# we need to convert the input into an integer using int().

age=int(input("Enter your age: "))

print("Next year you will be",age+1)


# ------------------------------------------------------------
# TAKING TWO NUMBERS FROM THE USER
# ------------------------------------------------------------

first_number=int(input("Enter the first number: "))
second_number=int(input("Enter the second number: "))

total=first_number+second_number

print("The total is:",total)


# ------------------------------------------------------------
# BASIC CALCULATOR
# ------------------------------------------------------------

print("\n--- Simple Calculator ---")

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

print("Addition:",num1+num2)
print("Subtraction:",num1-num2)
print("Multiplication:",num1*num2)


# ------------------------------------------------------------
# TAKING DECIMAL NUMBERS
# ------------------------------------------------------------

# Use float() when the user might enter a decimal number.

height=float(input("\nEnter your height in meters: "))

print("Your height is",height,"meters.")


# ------------------------------------------------------------
# TAKING MULTIPLE TYPES OF INPUT
# ------------------------------------------------------------

name=input("\nEnter your name: ")
age=int(input("Enter your age: "))
height=float(input("Enter your height in meters: "))

print("\n--- Your Information ---")
print("Name:",name)
print("Age:",age)
print("Height:",height,"meters")


# ------------------------------------------------------------
# SIMPLE SHOPPING EXAMPLE
# ------------------------------------------------------------

print("\n--- Shopping Calculator ---")

price=float(input("Enter product price: "))
quantity=int(input("Enter quantity: "))

total=price*quantity

print(f"Total price:",total)


# ------------------------------------------------------------
# CALCULATING AGE IN THE FUTURE
# ------------------------------------------------------------

current_age=int(input("\nEnter your current age: "))
years=int(input("How many years into the future? "))

future_age=current_age+years

print(f"Your Future Age:",future_age)


# ------------------------------------------------------------
# COMMON MISTAKE
# ------------------------------------------------------------

# WRONG:
#
# age = input("Enter your age: ")
# print(age + 1)
#
# This causes an error because age is a string.
#
# For example:
#
# "20" + 1
#
# Python cannot add a string and an integer.


# CORRECT:

age=int(input("\nEnter your age: "))

print("Next year:",age+1)