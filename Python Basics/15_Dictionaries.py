"""
Dictionaries (Mutable):

Dictionaries are ordered collection of data items.
They store multiple items in a single variable.
Dictionary items are key-value pairs that are separated by commas
and enclosed within curly brackets {}.
"""

info={"Name":"Muhammad Saqib","Age":18}

print(info)


"""
Accessing Dictionary items:

(i) Accessing single values:

Values in a dictionary can be accessed by using keys.
We can access dictionary values by mentioning keys either in
square brackets or by using the get() method.
"""

info1={"Name":"Muhammad Saqib","Age":18}

print(info1["Name"])
print(info1.get("Name"))


"""
get() function:

The get() function in Python is used with dictionaries to retrieve
the value of a specified key.

It helps avoid errors if the key is missing by allowing you to
specify a default return value.

Syntax:
dict.get(key, default_value)
"""

data={"Name":"Saqib","Age":18}

print(data.get("City","Not Available"))


"""
(ii) Accessing multiple values:

We can print all the values in the dictionary using the values()
method.
"""

info2={"Name":"Muhammad Saqib","Age":18}

print(info2.values())


"""
(iii) Accessing keys:

We can print all the keys in the dictionary using the keys()
method.
"""

info3={"Name":"Muhammad Saqib","Age":18}

print(info3.keys())


"""
(iv) Accessing key-value pairs:

We can print all the key-value pairs in the dictionary using
the items() method.
"""

info4={"Name":"Muhammad Saqib","Age": 18}

print(info4.items())


"""
Dictionary Methods:

Dictionary uses several built-in methods for manipulation.
They are listed below.

(i) update():

The update() method updates the value of the key provided to it
if the item already exists in the dictionary, else it creates
a new key-value pair.
"""

info5={"Name":"Muhammad Saqib","Age":18}

info5.update({"Age":19})
info5.update({"DOB":2006})

print(info5)


"""
(ii) clear():

The clear() method removes all the items from the dictionary.
"""

info6={"Name":"Muhammad Saqib","Age":18}

info6.clear()

print(info6)     # Output: {}


"""
(iii) pop():

The pop() method removes the key-value pair whose key is
passed as a parameter.
"""

info7={"Name":"Muhammad Saqib","Age":18,"DOB":2006}

info7.pop("DOB")

print(info7)


"""
(iv) popitem():

The popitem() method removes the last key-value pair
from the dictionary.
"""

info8={"Name":"Muhammad Saqib","Age":18,"DOB":2006}

info8.popitem()

print(info8)


"""
(v) del:

We can also use the del keyword to remove a dictionary item.
"""

info9={"Name":"Muhammad Saqib","Age":18}

del info9["Age"]

print(info9)


"""
If key is not provided, then the del keyword will delete
the dictionary entirely.
"""

info10={"Name":"Muhammad Saqib","Age":18}

del info10

# The dictionary 'info' no longer exists.


"""
Check if a value exit in dictionary
"""

info11={"Name":"Muhammad Saqib","Age":18}

name=info11.get("Name","Not Available")

if name in info11.values():
    print("Muhammad Saqib is present in dict")
else:
    print("Muhammad Saqib is not present in dict")


