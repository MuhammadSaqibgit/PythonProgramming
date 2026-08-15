"""
Sets (Mutable):

Sets are unordered collection of data items.
They store multiple items in a single variable.
Set items are separated by commas and enclosed within curly brackets {}.

Sets are mutable, meaning we can add or remove items after creation.
Sets do not contain duplicate items.
"""

set1={2,3,6,2,3}
print(set1)

info={"Muhammad Saqib",18,3.9}
print(info)


"""
Sets are unordered:

The items of a set occur in random/unordered order.
Therefore, set items cannot be accessed using an index.
"""

info1={"Muhammad Saqib",18,3.9}
print(info1)

# Set indexing is not possible:
# print(info[0])


"""
How to make an empty set:

Using only {} creates an empty dictionary, not an empty set.
"""

empty_set={}
print(type(empty_set))


"""
To create an empty set, use set().
"""

empty_set=set()
print(type(empty_set))


"""
Accessing set items:

Since sets are unordered and do not have indexes,
we access their items using a loop.
"""

info2={"Muhammad Saqib",18,3.9}

for items in info2:
    print(items)


"""
Joining Sets:

Sets in Python work more or less like sets in mathematics.
We can perform operations such as union and intersection on sets.

(1) union() and update():

The union() method returns all items that are present in
the two sets as a new set.

The update() method adds items from another set/iterable
into the existing set.
"""

cities1={"Tokyo","Madrid","Berlin","Mexico"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}

cities3=cities1.union(cities2)
print(cities3)

cities4={"Okara","Lahore"}
cities5={"Karachi","Faisalabad"}

cities4.update(cities5)
print(cities4)


"""
(2) intersection() and intersection_update():

The intersection() method returns only the items that are
common to both sets as a new set.

The intersection_update() method updates the existing set
and keeps only the common items.
"""

cities6={"Tokyo","Madrid"}
cities7={"Tokyo","Berlin"}

cities8=cities6.intersection(cities7)
print(cities8)

cities9={"Tokyo","Madrid","Berlin"}
cities10={"Seoul","Tokyo","Kabul"}

cities9.intersection_update(cities10)
print(cities9)


"""
(3) symmetric_difference() and symmetric_difference_update():

The symmetric_difference() method returns only the items
that are not common to both sets.

The symmetric_difference_update() method updates the existing
set with the symmetric difference.
"""

cities11={"Tokyo","Madrid"}
cities12={"Tokyo","Madrid","Berlin"}

cities13=cities11.symmetric_difference(cities12)
print(cities13)

cities14={"Tokyo","Berlin"}
cities15={"Tokyo","Madrid"}

cities14.symmetric_difference_update(cities15)
print(cities14)


"""
(4) difference() and difference_update():

The difference() method returns only the items that are
present in the original set but not in the other set.

The difference_update() method updates the existing set
by removing items that are present in the other set.
"""

cities16={"Tokyo","Madrid","Berlin"}
cities17={"Seoul","Kabul","Berlin"}

cities18=cities16.difference(cities17)
print(cities18)

cities19={"Tokyo","Madrid","Berlin"}
cities20={"Seoul","Kabul","Berlin"}

cities19.difference_update(cities20)
print(cities19)


"""
Set Methods:

There are several built-in methods used for the manipulation
of sets.

(1) isdisjoint():

The isdisjoint() method checks whether the items of the given
set are present in another set.

It returns True when the two sets have no common items.
"""

cities21={"Tokyo","Madrid","Berlin","Mexico"}
cities22={"Tokyo","Seoul","Kabul","Madrid"}

print(cities21.isdisjoint(cities22))


"""
(2) issuperset():

The issuperset() method checks if all the items of a particular
set are present in the original set.
"""

cities23={"Tokyo","Madrid","Berlin","Mexico"}
cities24={"Tokyo","Mexico"}

print(cities23.issuperset(cities24))


"""
(3) issubset():

The issubset() method checks if all the items of the original
set are present in the particular set.
"""

cities25={"Tokyo","Madrid","Berlin","Delhi"}
cities26={"Delhi","Madrid"}

print(cities25.issubset(cities26))


"""
(4) add():

If you want to add a single item to the set,
use the add() method.
"""

cities27={"Tokyo","Madrid"}
cities27.add("Mexico")
print(cities27)


"""
(5) update():

If you want to add more than one item, create another set
or use any other iterable object such as a list or tuple,
and use the update() method to add it into the existing set.
"""

cities28={"Tokyo","Madrid"}
cities29={"Seoul","Berlin"}

cities28.update(cities29)
print(cities28)


"""
(6) remove() / discard():

We can use remove() and discard() to remove items from a set.

The main difference is that if we try to delete an item
which is not present in the set, remove() raises an error,
whereas discard() does not raise an error.
"""

cities30={"Tokyo","Madrid","Berlin"}
cities30.remove("Tokyo")
print(cities30)


"""
Example of discard():

discard() does not raise an error if the item is absent.
"""

cities31={"Tokyo","Madrid","Berlin"}
cities31.discard("Paris")
print(cities31)


"""
(7) pop():

The pop() method removes an item from the set and returns it.

Since sets are unordered, we do not know which item will
be popped.
"""

cities32={"Tokyo","Madrid","Berlin"}

item=cities32.pop()

print(cities32)
print(item)


"""
(8) del:

del is not a method. It is a Python keyword which deletes
the set entirely.

Example:-
"""

cities33={"Tokyo","Madrid","Berlin"}
del cities33


"""
(9) clear():

The clear() method removes all items from the set
and produces an empty set.
"""

cities34={"Tokyo","Madrid","Berlin"}

cities34.clear()
print(cities34)


"""
Check if item exists in set:

We can use the 'in' operator to check whether an item
is present in a set.
"""

cities35={"Tokyo","Madrid","Berlin"}

if "Tokyo" in cities35:
    print("Tokyo is present")
else:
    print("Tokyo is not present")