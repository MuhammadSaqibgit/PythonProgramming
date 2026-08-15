"""
Tuples (Immutable):

Tuples are ordered collection of data items.
They store multiple items in a single variable.
Tuple items are separated by commas and enclosed within round brackets ().

Tuples are unchangeable, meaning we cannot alter them after creation.
"""

tup=(1,2,3,4,5,6)
print(tup)


"""
Creating a tuple with only one element:

If we declare only one element in a tuple without a comma,
Python considers it as an integer data type, not a tuple.
"""

tup1=(1)
print(tup1)
print(type(tup1))


"""
To create a tuple containing only one element,
we have to put a comma after the element.
"""

tup2=(1,)
print(tup2)
print(type(tup2))


"""
We can store different types of data items in a tuple.
"""

tup3=("Muhammad Saqib",18,7803)
print(tup3)


"""
Tuple indexing:

Each item/element in a tuple has its own index.
"""

country=("Spain","Italy","Pakistan")

print(country[0])
print(country[1])
print(country[2])


"""
Negative indexing:

We can also access tuple elements using negative indexes.
The last element has index -1.
"""

country1=("Spain","Italy","Pakistan")

print(country1[-1])

# Python interprets country[-1] like this:
print(country1[len(country1)-1])


"""
Accessing elements using loop:

We can access each element of a tuple using a loop.
"""

tup4=(1,2,3,4,5,6,7)

for i in range(0,7,1):
    print(tup4[i])


"""
Range of index:

We can print a range of tuple items by specifying:
1. Where we want to start.
2. Where we want to end.
3. Whether we want to skip elements in between the range.

Syntax:
tuple_name[start:end]
"""

animals=("Cat","Dog","Bat","Mouse","Horse")

print(animals[3:5])
print(animals[-3:-1])
print(animals[0:])
print(animals[:5])
print(animals[-4:])
print(animals[:])
print(animals[:-1])


"""
Use of jump index:

We can use a jump index to skip elements while accessing
a range of tuple items.

By default, jump index = 1.

Syntax:
tuple_name[start:end:jump_index]
"""

marks=(20,28,25,21,23)

print(marks[0:5:2])
print(marks[0::2])
print(marks[:5:2])
print(marks[::2])
print(marks[:])
print(marks[-5:-1:2])


"""
Check for an item:

We can use the 'in' operator to check whether an item
is present in a tuple.
"""

country2=("Germany","Spain","Pakistan","England")

if "Pakistan" in country2:
    print("Pakistan is present")
else:
    print("Pakistan is not present")


"""
Manipulating Tuples:

Tuples are immutable, so we cannot directly change them.

If we want to make changes in a tuple, we first convert
the tuple into a list. After making the changes, we convert
the list back into a tuple.
"""

countries=("Spain","Germany","Pakistan","England")

temp=list(countries)

temp.append("Australia")
temp.pop(1)

countries=tuple(temp)

print(countries)


"""
Concatenating two tuples:

We can directly concatenate two tuples without converting
them into lists.
"""

countries1=("Pakistan","Afghanistan","England")
countries2=("Spain","Russia")

countries3=countries1+countries2

print(countries3)


"""
How to make a tuple by taking user input:

We cannot make a tuple by taking user input directly because
tuples are immutable.

We can take input from the user in a list and then convert
the list into a tuple.
"""

making_tuple=[]

for i in range(0,5,1):
    country3=input("Enter a country: ")
    making_tuple.append(country3)

countries4=tuple(making_tuple)

print(countries4)


"""
Tuple Methods:

As tuple is immutable so it has limited built in functions.

(i) count() metod:

The count() method of tuple returns the number of times the
given element appears in the tuple.
"""

tup5=(0,1,2,3,2,3,1,3,2)

print(tup5.count(3))


"""
(i) count() metod:

The count() method of tuple returns the first occurance of 
the given element from the tuple.
"""

tup6=(1,2,3,4,4,3,2,1)

print(tup6.index(4))