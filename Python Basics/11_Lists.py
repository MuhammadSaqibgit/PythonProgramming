"""
Lists (Mutable):

Lists are ordered collection of data items.
They store multiple items in a single variable.
List items are separated by commas and enclosed within square brackets [].
Lists are changeable, meaning we can alter them after creation.
"""

list1=["Muhammad Saqib",1,True,10.5]

print(list1)


"""
(1) List indexing:

Each item/element in a list has its own unique index.
The first item has index [0] and so on.

We can use positive and negative indexing.
"""

colors=["Red","Green","Blue","Yellow"]

print(colors[0])    # Positive indexing
print(colors[1])
print(colors[-1])   # Negative indexing


"""
(2) Range of index:

We can access a range of items from a list by using slicing.

Syntax:
list_name[start:end:jump_index]
"""

animals=["Cat","Dog","Mouse","Horse","Donkey"]

print(animals[0:4])     # Positive indexing
print(animals[0:5])
print(animals[-3:-2])   # Negative indexing
print(animals[0:])      # Till end
print(animals[:3])      # From start
print(animals[-4:])     # Till end using negative index
print(animals[:-1])     # From start using positive index


"""
(3) Use of jump index:

By default, jump index is 1.
We can provide a different jump index to skip items while slicing.

Syntax:
list_name[start:end:jump_index]
"""

marks=[20,25,24,21,22,23]

print(marks[0:6:2])
print(marks[0::2])
print(marks[::2])
print(marks[::-1])


"""
(4) Accessing list elements using loop:

We can use a loop to access each element of a list.

Example:-
"""

list2=[1,2,3,4,5,6,7]

for i in list2:
    print(i)

for j in range(0,7,1):
    print(list2[j])


"""
(5) Check whether an item is present in the list:

We can use the 'in' operator to check whether an item exists
in a list.
"""

colors1=["Red","Green","Blue","Yellow","Green"]

if "Yellow" in colors1:
    print("Yellow is present")
else:
    print("Yellow is absent")


"""
(6) List Comprehension:

List comprehensions are used for creating new lists from other iterables
like lists, tuples, dictionaries, sets, and even arrays and strings.

Syntax:
list_name=[Expression(any-name) for any-name in iterable(parent_list)
            if condition]
"""
names=[
    "Muhammad Saqib",
    "Muhammad Ali",
    "Muhammad Ahmad",
    "Muhammad Zahid"
]

names_with_e=[name for name in names if "e" in name]

print(names_with_e)


"""
We can also create a list based on the length of items.
"""

names1=[
    "Muhammad Saqib",
    "Muhammad Ali",
    "Muhammad Ahmad",
    "Muhammad Zahid"
]

nameswithlengthgreaterthan14=[
    name for name in names1 if len(name)>14
]

print(nameswithlengthgreaterthan14)


"""
List Methods:

List methods are built-in methods used to perform different operations
on lists.


(1) append():

The append() method adds an item to the end of the list.
"""

numbers=[1,2,3]

numbers.append(4)

print(numbers)


"""
(2) insert():

The insert() method inserts an item at a specific position.

Syntax:
list_name.insert(index,item)
"""

numbers1=[1,2,3]

numbers1.insert(1,10)

print(numbers1)


"""
(3) extend():

The extend() method extends the list by appending all elements
from another iterable/list.
"""

numbers2=[1,2,3]

numbers2.extend([5,6])

print(numbers2)


"""
We can also extend one list using another list.
"""

numbers3=[1,2,3]
marks1=[4,5,6]

numbers3.extend(marks1)

print(numbers3)


"""
(4) remove():

The remove() method removes an element from the list.
"""

numbers4=[1,2,3]

numbers4.remove(2)

print(numbers4)


"""
(5) pop():

The pop() method removes and returns an item at a specific index.
The default index is the last item.

Syntax:
list_name.pop(index)
"""

numbers5=[1,2,3]

last_item=numbers5.pop()

print(last_item)
print(numbers5)


"""
(6) clear():

The clear() method removes all elements from the list.
"""

numbers6=[1,2,3]

numbers6.clear()

print(numbers6)


"""
(7) index():

The index() method returns the index of the item to find.
It returns the first occurrence.

Syntax:
list_name.index(item, start, end)
"""

numbers7=[1,2,3,4,5,6]

print(numbers7.index(2))


"""
We can also give starting and ending indexes in the index() method.
"""

numbers8=[1,2,3,4,5,6]

print(numbers8.index(4,1,5))


"""
(8) count():

The count() method returns the count of an item.
"""

numbers9=[1,2,3,5,2,6,2]

print(numbers9.count(2))


"""
(9) sort():

The sort() method sorts the list in ascending or descending order.
"""
# Ascending Order

numbers10=[4,1,3,2]

numbers10.sort()

print(numbers10)

# Descending order

numbers11=[4,1,3,2]

numbers11.sort(reverse=True)

print(numbers11)


"""
(10) sorted():

The sorted() function returns a new sorted list without modifying
the original list.
"""

numbers12=[4,1,3,2]

print(sorted(numbers12)) # Ascending Order
print(sorted(numbers12,reverse=True)) # Descending Order
print(numbers12)


"""
(11) reverse():

The reverse() method reverses the list in place.
"""

numbers13=[4,2,3,1]

numbers13.reverse()

print(numbers13)


"""
(12) copy():

The copy() method creates a shallow copy of the list.
"""

numbers14=[1, 3, 5, 6]

new_list=numbers14.copy()

print(new_list)


"""
Two Dimensional Lists:

A two dimensional list can be considered as a table that consists
of rows and columns.

A two dimensional list contains multiple one dimensional list.

Each element in a 2D list is referred to with the help of two indexes.
One index is used to indicate the row and the second index is used
to indicate the column of the element.

Example:-

This is a 3-by-4 list:
"""

list3=[
    [1,2,3,4],       # First row
    [5,6,7,8],       # Second row
    [9,10,11,12]     # Third row
]

print(list3)


"""
We can also make a 2D list like this.
"""

list4=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(list4)


"""
Accessing individual elements of 2D list
"""

print(list4[1][2]) # 2nd row and 3rd column element (7)


"""
Accessing elements of 2D list using loop
"""

for row_num in range(0,3,1):
    for col_num in range(0,4,1):
        print(list4[row_num][col_num],end=" ")

print()

"""
Three Dimensional Lists:

A three-dimensional (3D) list is a list that contains 2D lists, 
which themselves contain 1D lists.

Each element in a 3D list is referred to with the help of three 
indexes. One index is used to indicate the dimension of the 
element, the second  index is used to indicate the row of the 
element and the third index is used to indicate the column of 
the element.
"""

list5=[
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
]

print(list5)


"""
Accessing individual elements of 3D list
"""

print(list5[0][1][2]) # Dimension 1, 2nd row and 3rd column element (6)


"""
Accessing elements of 2D list using loop
"""

for dim_num in range(0,2,1):
    for row_num1 in range(0,2,1):
        for col_num1 in range(0,3,1):
            print(list5[dim_num][row_num1][col_num1],end=" ")

print()
