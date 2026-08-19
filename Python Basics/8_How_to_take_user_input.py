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
# name = input("What is your name? ")
#
# ============================================================


# ------------------------------------------------------------
# 1. BASIC USER INPUT
# ------------------------------------------------------------

print("Hello! Let's learn how to take user input.")

name = input("What is your name? ")

print("Hello,", name)


# ------------------------------------------------------------
# 2. USING INPUT WITH A VARIABLE
# ------------------------------------------------------------

# We can store the user's input in a variable.

age = input("How old are you? ")

print("You are", age, "years old.")


# ------------------------------------------------------------
# 3. INPUT() ALWAYS RETURNS A STRING
# ------------------------------------------------------------

# Even if the user enters a number, input() gives us a string.

number = input("Enter a number: ")

print("The value you entered is:", number)
print("The type of this value is:", type(number))

# If the user enters:
# 25
#
# Python sees it as:
# "25"
#
# NOT:
# 25


# ------------------------------------------------------------
# 4. CONVERTING USER INPUT TO AN INTEGER
# ------------------------------------------------------------

# If we want to perform mathematical calculations,
# we need to convert the input into an integer using int().

age = int(input("Enter your age: "))

print("Next year you will be", age + 1)


# ------------------------------------------------------------
# 5. TAKING TWO NUMBERS FROM THE USER
# ------------------------------------------------------------

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

total = first_number + second_number

print("The total is:", total)


# ------------------------------------------------------------
# 6. BASIC CALCULATOR
# ------------------------------------------------------------

print("\n--- Simple Calculator ---")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

# We should check that the second number is not zero
# before performing division.

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Cannot divide by zero.")


# ------------------------------------------------------------
# 7. TAKING DECIMAL NUMBERS
# ------------------------------------------------------------

# Use float() when the user might enter a decimal number.

height = float(input("\nEnter your height in meters: "))

print("Your height is", height, "meters.")


# ------------------------------------------------------------
# 8. TAKING MULTIPLE TYPES OF INPUT
# ------------------------------------------------------------

name = input("\nEnter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

print("\n--- Your Information ---")
print("Name:", name)
print("Age:", age)
print("Height:", height, "meters")


# ------------------------------------------------------------
# 9. USING INPUT WITH F-STRINGS
# ------------------------------------------------------------

# f-strings make it easier to combine variables and text.

name = input("\nWhat is your name? ")
age = int(input("How old are you? "))

print(f"Hello {name}!")
print(f"You are {age} years old.")


# ------------------------------------------------------------
# 10. USER INPUT AND IF/ELSE
# ------------------------------------------------------------

age = int(input("\nEnter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")


# ------------------------------------------------------------
# 11. USER INPUT WITH MULTIPLE CONDITIONS
# ------------------------------------------------------------

marks = float(input("\nEnter your marks: "))

if marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")


# ------------------------------------------------------------
# 12. TAKING YES/NO INPUT
# ------------------------------------------------------------

answer = input("\nDo you like Python? ")

if answer.lower() == "yes":
    print("That's great!")
else:
    print("Keep learning. You might like it later!")


# ------------------------------------------------------------
# 13. .lower() AND .upper()
# ------------------------------------------------------------

# .lower() converts text to lowercase.
# .upper() converts text to uppercase.

name = input("\nEnter your name: ")

print("Lowercase:", name.lower())
print("Uppercase:", name.upper())


# This is useful when comparing user input.

answer = input("Do you want to continue? ")

if answer.lower() == "yes":
    print("Continuing...")
else:
    print("Stopping...")


# ------------------------------------------------------------
# 14. REMOVING EXTRA SPACES WITH .strip()
# ------------------------------------------------------------

# Sometimes users accidentally enter spaces before or after
# their answer.

name = input("\nEnter your name: ")

name = name.strip()

print("Hello", name)


# We can also combine methods:

name = input("Enter your name: ").strip().lower()

print("Your name in lowercase is:", name)


# ------------------------------------------------------------
# 15. SIMPLE LOGIN EXAMPLE
# ------------------------------------------------------------

print("\n--- Login ---")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Invalid username or password.")


# ------------------------------------------------------------
# 16. SIMPLE SHOPPING EXAMPLE
# ------------------------------------------------------------

print("\n--- Shopping Calculator ---")

price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print(f"Total price: ${total:.2f}")


# ------------------------------------------------------------
# 17. CALCULATING AGE IN THE FUTURE
# ------------------------------------------------------------

current_age = int(input("\nEnter your current age: "))
years = int(input("How many years into the future? "))

future_age = current_age + years

print(f"You will be {future_age} years old in {years} years.")


# ------------------------------------------------------------
# 18. COMMON MISTAKE
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

age = int(input("\nEnter your age: "))

print("Next year:", age + 1)


# ------------------------------------------------------------
# 19. HANDLING INVALID NUMBER INPUT
# ------------------------------------------------------------

# If the user enters text when we expect a number,
# int() or float() will cause a ValueError.
#
# We can use try/except to handle this safely.

try:
    age = int(input("\nEnter your age: "))
    print("Your age is:", age)

except ValueError:
    print("Please enter a valid number.")


# ------------------------------------------------------------
# 20. A BEGINNER-FRIENDLY MINI PROJECT
# ------------------------------------------------------------
#
# Let's create a small program that asks for:
# - Name
# - Age
# - Favorite color
# - Favorite number
#
# Then it displays all the information.

print("\n================================")
print("       ABOUT YOU PROGRAM")
print("================================")

name = input("What is your name? ").strip()
age = int(input("How old are you? "))
color = input("What is your favorite color? ").strip()
favorite_number = float(input("What is your favorite number? "))

print("\n--- Your Information ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favorite color: {color}")
print(f"Favorite number: {favorite_number}")


# ============================================================
# SUMMARY
# ============================================================
#
# input()
#     Takes input from the user.
#
# int()
#     Converts a value to an integer.
#
# float()
#     Converts a value to a decimal number.
#
# str()
#     Converts a value to a string.
#
# .lower()
#     Converts text to lowercase.
#
# .upper()
#     Converts text to uppercase.
#
# .strip()
#     Removes extra spaces from the beginning and end.
#
#
# The most important pattern to remember is:
#
# name = input("Enter your name: ")
#
# For numbers:
#
# age = int(input("Enter your age: "))
#
# For decimal numbers:
#
# price = float(input("Enter the price: "))
#
# ============================================================
#
# PRACTICE:
#
# 1. Ask the user for their name and print a greeting.
#
# 2. Ask for two numbers and print their sum.
#
# 3. Ask for someone's age and calculate their age next year.
#
# 4. Ask for the price and quantity of a product and calculate
#    the total price.
#
# 5. Create a program that asks for a user's name, age, and
#    favorite hobby, then displays a short introduction.
#
# ============================================================