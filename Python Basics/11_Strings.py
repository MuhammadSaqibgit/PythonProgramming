"""
Strings (Immutable):

A string is essentially a sequence or array of textual data.
In Python, anything enclosed between single or double quotation marks
is considered a string.
"""

name1="Muhammad Saqib"
name2='Muhammad Ali'

print("Hello",name1)
print("Hello",name2)


"""
Strings are immutable:

Immutable means that the existing string cannot be changed directly.
A new string is created when we perform an operation on a string.
"""

name="python"
new_name=name.upper()

print("Original string:",name)
print("New string:",new_name)


"""
Putting quotation marks inside a string:

Sometimes we need to put double or single quotation marks inside a string.
We can use different quotation marks or an escape character.
"""

print('He said, "I want to eat an apple".')
print("It's a beautiful day.")
print("He said, \"Python is easy to learn.\"")


"""
Multiline strings:

If our string has multiple lines, we can create it using triple
double quotation marks or triple single quotation marks.
"""

string1="""Muhammad Saqib
Python programmer
Data Analyst"""

print(string1)

string2="Python\nProgramming\nLanguage"
print(string2)


"""
Accessing characters of a string:

In Python, a string is like an array of characters.
We can access characters by using their index.
String indexing starts from 0.

Square brackets [] are used to access elements of a string.
"""

name3="Muhammad Saqib"

print(name3[0])
print(name3[1])
print(name3[2])


"""
String slicing:

Slicing is used to access a range of characters from a string.

Syntax:
string_name[start:end]

The ending index is not included.
"""

fruit="Apple"

print(fruit[:5])
print(fruit[0:5])
print(fruit[0:3])
print(fruit[1:])
print(fruit[-3:-1]) # Negative Indexing


"""
Loop through a string:

Strings are arrays/sequences and are iterable.
Therefore, we can access every character using a loop.

"""

name4="Muhammad Saqib"

for i in name4:
    print(i)


"""
len() function:

We can use the len() function to find the length of a string.
"""

name5="Muhammad Saqib"
print(len(name5))


"""
String methods:

String methods are built-in methods used to perform different operations
on strings.

(1) capitalize():

It converts the first character of the string to uppercase.
"""

text="hello world"
print(text.capitalize())


"""
(2) lower():

It converts all characters of the string to lowercase.
"""

text1="HELLO WORLD"
print(text1.lower())


"""
(3) upper():

It converts all characters of the string to uppercase.
"""

text2="hello world"
print(text2.upper())


"""
(4) center():

It places the string in the center of a given width.
"""

text3="Python"
print(text3.center(10,"*"))


"""
(5) count():

It returns the number of occurrences of a given value.
"""

text4="HELLO WORLD"
print(text4.count("L"))


"""
(6) index():

It returns the index of the first occurrence of a given value.
"""

text5="HELLO WORLD"
print(text5.index("O"))


"""
(7) find():

It searches for a value and returns its index.
"""

text6="HELLO WORLD"
print(text6.find("OR"))


"""
(8) replace():

It replaces a specified value with another value.
"""

date="14/09/2022"
print(date.replace("/","-"))


"""
(9) split():

It splits a string into a list using the given separator.
"""

date1="14/09/2022"
print(date1.split("/"))


"""
(10) isalnum():

It returns True if all characters in the string are alphanumeric.
"""

text7="abc123"
print(text7.isalnum())


"""
(11) isnumeric():

It returns True if all characters in the string are numeric.
"""

text8="12345"
print(text8.isnumeric())


"""
(12) islower():

It returns True if the string is in lowercase.
"""

text9="hello world"
print(text9.islower())


"""
(13) isupper():

It returns True if the string is in uppercase.
"""

text10="HELLO WORLD"
print(text10.isupper())


"""
(14) strip():

The strip() method removes whitespace before and after the string.
"""

name6="  Muhammad Saqib  "
print(name.strip())


"""
(15) rstrip():

The rstrip() method removes trailing characters from the right side.
"""

text11="Hello!!!"
print(text11.rstrip("!"))


"""
(16) endswith():

The endswith() method checks if the string ends with a given value.
"""

text12="Welcome to the Terminal !!!"
print(text12.endswith("!!!"))


"""
(17) isprintable():

It returns True if all characters in the string are printable.
"""

text13="Good Job"
print(text13.isprintable())


"""
(18) isspace():

It returns True only if the string contains whitespace characters.
"""

text14="   "
print(text14.isspace())


"""
(19) istitle():

It returns True if the first letter of each word is capitalized.
"""

text15="World Health Organization"
print(text15.istitle())


"""
(20) startswith():

It checks if the string starts with a given value.
"""

text16="Python is an interpreted language"
print(text16.startswith("Python"))


"""
(21) swapcase():

It changes uppercase characters to lowercase and lowercase characters
to uppercase.
"""

text17="Python Is An Interpreted Language"
print(text17.swapcase())


"""
(22) title():

It capitalizes the first letter of each word in the string.
"""

text18="My name is Muhammad Saqib"
print(text18.title())
