"""
MAGIC METHODS
"""


# ============================================================
# 1. INTRODUCTION TO MAGIC METHODS
# ============================================================

"""
Magic methods are special methods in Python that allow our
objects to interact with Python's built-in features.

They are also commonly called:

    Dunder methods
    Special methods

The word "dunder" comes from:

    Double Underscore

because these methods usually have double underscores at the
beginning and end of their names.

For example:

    __init__()
    __str__()
    __repr__()
    __len__()
    __eq__()

Python calls many of these methods automatically when we use
certain operations.

For example:

    print(object)

may call:

    object.__str__()

Similarly:

    len(object)

may call:

    object.__len__()

And:

    object1 == object2

may call:

    object1.__eq__(object2)

Magic methods allow our custom objects to work naturally with
Python's built-in syntax and functions.
"""


# ============================================================
# 2. WHY DO MAGIC METHODS EXIST?
# ============================================================

"""
Normally, Python already knows how to work with built-in
objects.

For example:

    numbers=[10,20,30]

    print(numbers)
    print(len(numbers))

Python knows what these operations mean for a list.

But what happens when we create our own class?

For example:
"""


class Book:

    pass


book_object=Book()


"""
Python does not automatically know:

    How should this object be displayed?
    What should len(book_object) mean?
    How should two Book objects be compared?

Magic methods allow us to define this behavior.

We can tell Python how our custom objects should behave when
used with built-in functions and operators.
"""


# ============================================================
# 3. THE BASIC IDEA OF MAGIC METHODS
# ============================================================

"""
The basic idea is:

    Python operation
          ↓
    Special method
          ↓
    Custom behavior

For example:

    print(object)
          ↓
    __str__()

    len(object)
          ↓
    __len__()

    object1 == object2
          ↓
    __eq__()

    object1 < object2
          ↓
    __lt__()

We define these methods inside our class.
"""


# ============================================================
# 4. __init__() IS ALSO A MAGIC METHOD
# ============================================================

"""
We have already used __init__() in previous chapters.

__init__() is a special method that Python calls automatically
when an object is created.

For example:
"""


class Student:

    def __init__(self,name,age):
        self.name=name
        self.age=age


student_object=Student("Ayesha",20)

print(student_object.name)
print(student_object.age)


"""
When we write:

    Student("Ayesha",20)

Python automatically calls:

    __init__()

with the newly created object.

So __init__() is also a magic method.

We will now learn some other important magic methods.
"""


# ============================================================
# 5. __str__() METHOD
# ============================================================

"""
The __str__() method defines a user-friendly string
representation of an object.

It is commonly called when we use:

    print(object)

For example:
"""


class Product:

    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __str__(self):
        return f"{self.name}-${self.price}"


product_object=Product("Keyboard",45)

print(product_object)


"""
Because Product has a __str__() method, Python uses it when
print() is called.

Output:

    Keyboard-$45

Without __str__(), Python would normally display something
similar to:

    <__main__.Product object at 0x...>

which is not very useful to a user.
"""


# ============================================================
# 6. __str__() SHOULD RETURN A STRING
# ============================================================

"""
The __str__() method must return a string.

For example:
"""


class Movie:

    def __init__(self,title):
        self.title=title

    def __str__(self):
        return self.title


movie_object=Movie("Python Adventures")

print(movie_object)


"""
Here __str__() returns:

    "Python Adventures"

Therefore, print() can display it.
"""


# ============================================================
# 7. __repr__() METHOD
# ============================================================

"""
Another important magic method is:

    __repr__()

__repr__() provides a representation of an object that is
mainly intended for developers and debugging.

For example:
"""


class User:

    def __init__(self,username):
        self.username=username

    def __repr__(self):
        return f"User(username='{self.username}')"


user_object=User("python_learner")

print(repr(user_object))


"""
repr() calls the object's __repr__() method.

The result is:

    User(username='python_learner')

This gives us useful information about the object.
"""


# ============================================================
# 8. __str__() VS __repr__()
# ============================================================

"""
Both __str__() and __repr__() return a string representation
of an object, but they have different purposes.

__str__():

    Intended to be readable and user-friendly.

__repr__():

    Intended to be informative and useful for developers.

A simple way to remember:

    __str__()
        → What should the user see?

    __repr__()
        → What should the developer see?

For example:
"""


class Employee:

    def __init__(self,name,department):
        self.name=name
        self.department=department

    def __str__(self):
        return f"{self.name} works in {self.department}"

    def __repr__(self):
        return (
            f"Employee(name='{self.name}', "
            f"department='{self.department}')"
        )


employee_object=Employee("Bilal", "IT")

print(employee_object)
print(repr(employee_object))


"""
__str__():

    Bilal works in IT

__repr__():

    Employee(name='Bilal', department='IT')

The first is more natural for a user.

The second provides more details about the object.
"""


# ============================================================
# 9. WHAT HAPPENS IF __str__() IS NOT DEFINED?
# ============================================================

"""
If __str__() is not defined, Python may fall back to
__repr__().

If neither is defined, Python uses the default object
representation.

For example:
"""


class Camera:

    def __init__(self,brand):
        self.brand=brand


camera_object=Camera("Canon")

print(camera_object)


"""
The output will look similar to:

    <__main__.Camera object at 0x...>

This is why defining __str__() can make custom objects much
more readable.
"""


# ============================================================
# 10. __repr__() AND __str__() TOGETHER
# ============================================================

"""
It is common to define both methods when a class needs a
friendly representation for users and a detailed representation
for developers.
"""


class Laptop:

    def __init__(self,brand,memory):
        self.brand=brand
        self.memory=memory

    def __str__(self):
        return f"{self.brand} laptop with {self.memory}GB RAM"

    def __repr__(self):
        return (
            f"Laptop(brand='{self.brand}', "
            f"memory={self.memory})"
        )


laptop_object=Laptop("Dell",16)

print(laptop_object)
print(repr(laptop_object))


# ============================================================
# 11. __len__() METHOD
# ============================================================

"""
The __len__() method allows our custom objects to work with:

    len()

For example:

    len(object)

causes Python to look for:

    object.__len__()

Let's create a class representing a playlist.
"""


class Playlist:

    def __init__(self,songs):
        self.songs=songs

    def __len__(self):
        return len(self.songs)


playlist_object=Playlist(
    ["Song A","Song B","Song C","Song D"]
)

print("Number of songs:",len(playlist_object))


"""
Because we defined __len__(), Python knows what:

    len(playlist_object)

should mean.

Internally, it uses:

    playlist_object.__len__()
"""


# ============================================================
# 12. __len__() MUST RETURN AN INTEGER
# ============================================================

"""
The __len__() method should return a non-negative integer.

For example:
"""


class Team:

    def __init__(self,members):
        self.members=members

    def __len__(self):
        return len(self.members)


team_object=Team(
    ["Ali","Sara","Hamza","Noor"]
)

print("Team size:",len(team_object))


"""
Here __len__() returns:

    4

Therefore, len(team_object) works correctly.
"""


# ============================================================
# 13. __eq__() METHOD
# ============================================================

"""
The __eq__() method defines what should happen when two
objects are compared using:

    ==

For example:

    object1==object2

Python can call:

    object1.__eq__(object2)

Let's create a class representing a book.
"""


class Book:

    def __init__(self,title,author):
        self.title=title
        self.author=author

    def __eq__(self,other):
        return (
            self.title==other.title
            and self.author==other.author
        )


first_book=Book("Python Basics","John")
second_book=Book("Python Basics","John")
third_book=Book("Advanced Python","David")

print(first_book==second_book)
print(first_book==third_book)


"""
The first comparison returns:

    True

because both books have the same title and author.

The second comparison returns:

    False

because their data is different.
"""


# ============================================================
# 14. __eq__() CHANGES HOW EQUALITY IS DEFINED
# ============================================================

"""
Without defining __eq__(), two separate objects are generally
considered different even if their attributes contain the same
values.

For example:
"""


class Product:

    def __init__(self,name,price):
        self.name=name
        self.price=price


first_product=Product("Mouse",25)
second_product=Product("Mouse",25)

print(first_product==second_product)


"""
The result is normally:

    False

because these are two different object instances.

Now let's define __eq__().
"""


class Item:

    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __eq__(self,other):
        return (
            self.name==other.name
            and self.price==other.price
        )


first_item=Item("Mouse",25)
second_item=Item("Mouse",25)

print(first_item==second_item)


"""
Now the result is:

    True

because we defined what equality means for Item objects.
"""


# ============================================================
# 15. __lt__() METHOD
# ============================================================

"""
The __lt__() method defines behavior for the less-than operator:

    <

For example:

    object1 < object2

can call:

    object1.__lt__(object2)

Let's create a class representing a score.
"""


class Score:

    def __init__(self,value):
        self.value=value

    def __lt__(self,other):
        return self.value<other.value


first_score=Score(70)
second_score=Score(85)

print(first_score<second_score)
print(second_score<first_score)


"""
The first comparison returns:

    True

because:

    70<85

The second comparison returns:

    False

because:

    85<70

We have defined how Score objects should behave with <.
"""


# ============================================================
# 16. OTHER COMPARISON MAGIC METHODS
# ============================================================

"""
Python provides several comparison-related magic methods.

Some important ones are:

    __eq__()   → ==
    __ne__()   → !=
    __lt__()   → <
    __le__()   → <=
    __gt__()   → >
    __ge__()   → >=

In this chapter, we focus mainly on:

    __eq__()
    __lt__()

These methods allow us to define meaningful comparisons for
our custom objects.
"""


# ============================================================
# 17. __del__() METHOD
# ============================================================

"""
Another special method is:

    __del__()

It is sometimes called a destructor.

Python may call __del__() when an object is about to be
destroyed.

For example:
"""


class TemporaryFile:

    def __del__(self):
        print("Object is being cleaned up.")


temporary_object=TemporaryFile()


"""
When the object is eventually destroyed, Python may call:

    __del__()

However, __del__() should be used carefully.

You generally should not rely on it for important resource
management or cleanup.
"""


# ============================================================
# 18. WHY __del__() IS RARELY USED DIRECTLY
# ============================================================

"""
There are several reasons why __del__() is rarely used
directly.

Python uses automatic memory management and garbage
collection.

The exact time when an object is destroyed may not always be
what you expect.

Therefore, __del__() is not a good place for important cleanup
that must happen at a predictable time.

For example, resources such as:

    files
    database connections
    network connections

are generally better managed using explicit techniques such
as context managers.

For now, remember:

    __del__() exists,
    but you should rarely need to define it yourself.
"""


# ============================================================
# 19. MAGIC METHODS ARE CALLED BY PYTHON
# ============================================================

"""
One important point is that we normally do not call magic
methods directly.

For example, instead of writing:

    product_object.__str__()

we normally write:

    print(product_object)

Instead of:

    playlist_object.__len__()

we normally write:

    len(playlist_object)

Instead of:

    first_book.__eq__(second_book)

we normally write:

    first_book==second_book

Python calls the appropriate magic method for us.
"""


# ============================================================
# 20. PRINT() AND __str__()
# ============================================================

"""
When we write:

    print(object)

Python uses the object's string representation.

If __str__() is defined, it is used to produce a
user-friendly representation.
"""


class Phone:

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def __str__(self):
        return f"{self.brand} {self.model}"


phone_object=Phone("Samsung","Galaxy")

print(phone_object)


"""
The following:

    print(phone_object)

uses:

    phone_object.__str__()

internally.
"""


# ============================================================
# 21. LEN() AND __len__()
# ============================================================

"""
Similarly:

    len(object)

uses:

    object.__len__()

if the class defines it.
"""


class Library:

    def __init__(self,books):
        self.books=books

    def __len__(self):
        return len(self.books)


library_object=Library(
    ["Book 1","Book 2","Book 3"]
)

print("Books:",len(library_object))


"""
Python uses:

    library_object.__len__()

behind the scenes.
"""


# ============================================================
# 22. == AND __eq__()
# ============================================================

"""
When we write:

    object1==object2

Python can use:

    object1.__eq__(object2)

"""


class Student:

    def __init__(self,student_id):
        self.student_id=student_id

    def __eq__(self,other):
        return self.student_id==other.student_id


student_one=Student(101)
student_two=Student(101)

print(student_one==student_two)


"""
Both objects have the same student ID, so the result is:

    True
"""


# ============================================================
# 23. < AND __lt__()
# ============================================================

"""
When we write:

    object1 < object2

Python can use:

    object1.__lt__(object2)
"""


class Temperature:

    def __init__(self,value):
        self.value=value

    def __lt__(self,other):
        return self.value<other.value


morning_temperature=Temperature(18)
afternoon_temperature=Temperature(32)

print(morning_temperature<afternoon_temperature)


"""
The result is:

    True

because:

    18 < 32
"""


# ============================================================
# 24. MAGIC METHODS MAKE CUSTOM OBJECTS FEEL PYTHONIC
# ============================================================

"""
One of the biggest advantages of magic methods is that they
allow our custom classes to work naturally with Python.

Instead of creating methods such as:

    show_object()
    get_length()
    is_equal()
    is_less_than()

we can integrate our class with Python's existing syntax:

    print(object)
    len(object)
    object1 == object2
    object1 < object2

This makes custom classes easier and more natural to use.
"""


# ============================================================
# 25. A COMPLETE EXAMPLE
# ============================================================

"""
Let's create a ShoppingCart class that uses several magic
methods.
"""


class ShoppingCart:

    def __init__(self,items):
        self.items=items

    def __str__(self):
        return f"ShoppingCart with {len(self.items)} items"

    def __repr__(self):
        return f"ShoppingCart(items={self.items!r})"

    def __len__(self):
        return len(self.items)

    def __eq__(self,other):
        return self.items==other.items


first_cart=ShoppingCart(
    ["Keyboard","Mouse","Monitor"]
)

second_cart=ShoppingCart(
    ["Keyboard","Mouse","Monitor"]
)

print(first_cart)
print(repr(first_cart))
print("Number of items:",len(first_cart))
print("Carts are equal:",first_cart==second_cart)


"""
This one class now works with:

    print()
    repr()
    len()
    ==

because we implemented the corresponding magic methods.
"""


# ============================================================
# 26. __repr__() AND !r
# ============================================================

"""
In the previous example, we used:

    {self.items!r}

inside an f-string.

The !r conversion asks Python to use the repr() representation
of the value.

For example:
"""


items_list=["Keyboard","Mouse"]

print(f"Normal: {items_list}")
print(f"Repr: {items_list!r}")


"""
For many basic values, the results may look similar.

The important idea is that:

    !r

asks for the object's repr representation.
"""


# ============================================================
# 27. __str__() VS __repr__() IN A LIST
# ============================================================

"""
There is an important behavior to understand.

Suppose we have objects inside a list.

Python commonly uses repr() to represent objects inside
containers such as lists.

For example:
"""


class Course:

    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Course('{self.name}')"


python_course=Course("Python")
java_course=Course("Java")

course_list=[python_course,java_course]

print(python_course)
print(course_list)


"""
The direct print:

    print(python_course)

uses __str__().

The list representation:

    print(course_list)

uses the objects' __repr__() representations.

This is one reason why defining __repr__() can be useful even
when __str__() is already defined.
"""


# ============================================================
# 28. __init__() VS __str__() VS __repr__()
# ============================================================

"""
These three methods have different purposes.

__init__():

    Initializes an object after it is created.

__str__():

    Provides a user-friendly string representation.

__repr__():

    Provides a developer-oriented representation.

For example:
"""


class Account:

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def __str__(self):
        return f"Account for {self.owner}"

    def __repr__(self):
        return (
            f"Account(owner='{self.owner}', "
            f"balance={self.balance})"
        )


account_object=Account("Hassan",5000)

print(account_object)
print(repr(account_object))


"""
The three methods have separate responsibilities:

    __init__()
        → creates and initializes object data

    __str__()
        → readable representation

    __repr__()
        → detailed representation
"""


# ============================================================
# 29. USING __eq__() SAFELY
# ============================================================

"""
When writing __eq__(), we should consider what happens if
the other object is not the same type.

A simple beginner-friendly approach is to check the type.
"""


class Coordinate:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __eq__(self,other):
        if not isinstance(other,Coordinate):
            return NotImplemented

        return self.x==other.x and self.y==other.y


first_point=Coordinate(2,4)
second_point=Coordinate(2,4)
third_point=Coordinate(5,8)

print(first_point==second_point)
print(first_point==third_point)


"""
The use of:

    NotImplemented

tells Python that this comparison is not supported for that
type of object.

For beginner programs, a simpler comparison may be enough,
but this pattern is useful when writing more robust classes.
"""


# ============================================================
# 30. __lt__() WITH REAL-WORLD OBJECTS
# ============================================================

"""
Magic methods are not limited to numbers.

We can define meaningful comparisons for real-world objects.

For example, we can compare books based on their page count.
"""


class ReadingBook:

    def __init__(self,title,pages):
        self.title=title
        self.pages=pages

    def __lt__(self,other):
        return self.pages<other.pages


short_book=ReadingBook("Python Basics",150)
long_book=ReadingBook("Python Programming",500)

print(short_book<long_book)


"""
Python now understands:

    short_book<long_book

because we defined __lt__().
"""


# ============================================================
# 31. SORTING CUSTOM OBJECTS
# ============================================================

"""
Once __lt__() is defined, it can also help Python compare
objects during operations such as sorting.
"""


class Player:

    def __init__(self,name,score):
        self.name=name
        self.score=score

    def __lt__(self,other):
        return self.score<other.score

    def __str__(self):
        return f"{self.name}: {self.score}"


players=[
    Player("Ali",75),
    Player("Sara",92),
    Player("Usman",68)
]

sorted_players=sorted(players)

for player in sorted_players:
    print(player)


"""
The Player class defines:

    __lt__()

Therefore, Python can compare players based on their scores.

The sorted() function can then arrange them accordingly.
"""


# ============================================================
# 32. MAGIC METHODS AND BUILT-IN FUNCTIONS
# ============================================================

"""
Magic methods allow custom objects to integrate with many
Python features.

Some examples:

    print(object)
        → __str__()

    repr(object)
        → __repr__()

    len(object)
        → __len__()

    object1 == object2
        → __eq__()

    object1 < object2
        → __lt__()

    object1 <= object2
        → __le__()

    object1 > object2
        → __gt__()

    object1 >= object2
        → __ge__()

    object1 != object2
        → __ne__()

This is called implementing special behavior for our custom
objects.
"""


# ============================================================
# 33. MAGIC METHODS ARE NOT NORMAL METHODS
# ============================================================

"""
Magic methods are still methods, but Python gives them special
meaning.

For example, this is a normal method:

    def greet(self):
        print("Hello")

We call it directly:

    object.greet()

But this:

    def __str__(self):
        ...

has special meaning.

Python knows to use it when:

    print(object)

is executed.
"""


# ============================================================
# 34. DO NOT RANDOMLY CREATE DUNDER METHODS
# ============================================================

"""
Magic methods have specific names and specific purposes.

You should not create names such as:

    __hello__()
    __calculate__()
    __display__()

and expect Python to automatically use them.

Python only gives special meaning to defined special method
names.

Examples include:

    __init__()
    __str__()
    __repr__()
    __len__()
    __eq__()
    __lt__()

So always use the appropriate magic method for the behavior
you want to customize.
"""


# ============================================================
# 35. MAGIC METHODS AND OPERATOR OVERLOADING
# ============================================================

"""
Methods such as:

    __eq__()
    __lt__()

are examples of operator overloading.

They allow operators such as:

    ==
    <
    >
    +

to work with custom objects.

We will study operator overloading in more detail in the next
chapter.

For now, remember that magic methods provide the mechanism
that allows Python operators to work with our custom objects.
"""


# ============================================================
# 36. COMMON MAGIC METHODS
# ============================================================

"""
There are many magic methods in Python.

Some commonly encountered ones include:

    __init__()
        Initialize an object.

    __str__()
        User-friendly string representation.

    __repr__()
        Developer-oriented representation.

    __len__()
        Defines behavior for len().

    __eq__()
        Defines behavior for ==.

    __lt__()
        Defines behavior for <.

    __le__()
        Defines behavior for <=.

    __gt__()
        Defines behavior for >.

    __ge__()
        Defines behavior for >=.

    __ne__()
        Defines behavior for !=.

    __del__()
        Called when an object is being finalized.

There are many more, but these are enough to begin
understanding the concept.
"""


# ============================================================
# 37. WHY __del__() SHOULD NOT BE USED FOR IMPORTANT CLEANUP
# ============================================================

"""
Let's look at __del__() one more time.

It may be tempting to write:

    def __del__(self):
        close_file()

However, relying on __del__() for important resource cleanup
is generally not recommended.

The timing of object destruction is not something you should
use as a reliable cleanup mechanism.

For resources that must be closed properly, Python provides
better approaches.

For example, files can be handled using:

    with open(...) as file:

We will study file handling separately in Python Basics, so
for now simply remember:

    __del__() exists, but it is rarely appropriate for
    important resource management.
"""


# ============================================================
# 38. A FINAL COMBINED EXAMPLE
# ============================================================

"""
Let's combine the main magic methods from this chapter into one
class.
"""


class LibraryBook:

    def __init__(self,title,pages):
        self.title=title
        self.pages=pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __repr__(self):
        return (
            f"LibraryBook(title='{self.title}', "
            f"pages={self.pages})"
        )

    def __len__(self):
        return self.pages

    def __eq__(self,other):
        if not isinstance(other,LibraryBook):
            return NotImplemented

        return (
            self.title==other.title
            and self.pages==other.pages
        )

    def __lt__(self, other):
        if not isinstance(other,LibraryBook):
            return NotImplemented

        return self.pages<other.pages


book_one=LibraryBook("Python Basics",200)
book_two=LibraryBook("Python Basics",200)
book_three=LibraryBook("Advanced Python",450)


# __str__()
print(book_one)


# __repr__()
print(repr(book_one))


# __len__()
print("Pages:",len(book_one))


# __eq__()
print("book_one == book_two:",book_one==book_two)


# __lt__()
print("book_one < book_three:",book_one<book_three)


"""
Our LibraryBook objects now work naturally with Python's
built-in features.

We can use:

    print(book_one)
    repr(book_one)
    len(book_one)
    book_one==book_two
    book_one<book_three

without manually calling the magic methods.
"""


# ============================================================
# 39. IMPORTANT IDEA: PYTHON CALLS THEM FOR US
# ============================================================

"""
Remember the following relationships:

    print(object)
        ↓
    object.__str__()

    repr(object)
        ↓
    object.__repr__()

    len(object)
        ↓
    object.__len__()

    object1==object2
        ↓
    object1.__eq__(object2)

    object1<object2
        ↓
    object1.__lt__(object2)

This is the main purpose of magic methods.

They allow our classes to communicate with Python's built-in
language features.
"""


# ============================================================
# 40. SUMMARY
# ============================================================

"""
Important points:

1. Magic methods are special methods provided by Python.

2. They are also called dunder methods.

3. "Dunder" means double underscore.

4. Examples include:

       __init__()
       __str__()
       __repr__()
       __len__()
       __eq__()
       __lt__()

5. Magic methods allow custom objects to work naturally with
   Python's built-in functions and operators.

6. __init__() is called automatically when an object is
   initialized.

7. __str__() provides a user-friendly string representation.

8. __repr__() provides a detailed representation mainly useful
   for developers and debugging.

9. A simple way to remember the difference:

       __str__()
           → user-friendly

       __repr__()
           → developer-friendly

10. print(object) commonly uses __str__().

11. repr(object) uses __repr__().

12. __len__() defines what len(object) means for a custom
    object.

13. __eq__() defines how two objects behave with:

        ==

14. __lt__() defines how two objects behave with:

        <

15. Other comparison magic methods include:

        __ne__()
        __le__()
        __gt__()
        __ge__()

16. __del__() may be called when an object is being finalized.

17. __del__() is rarely used directly for important cleanup
    because object destruction timing should not be relied upon
    for predictable resource management.

18. We normally do not call magic methods directly.

19. Instead, we use normal Python syntax:

        print(object)
        len(object)
        object1==object2
        object1<object2

20. Python calls the appropriate magic method behind the
    scenes.

21. Magic methods make custom objects feel more natural and
    Pythonic.

22. They allow our classes to integrate with Python's built-in
    behavior.

23. __eq__() and __lt__() are examples of methods used for
    operator overloading.

24. There are many other magic methods in Python, but learning
    the most common ones first is enough to understand the
    concept.

The main idea to remember is:

    Magic methods allow us to define how our custom objects
    should behave when Python performs built-in operations
    on them.

For example:

    print(object)
        → __str__()

    len(object)
        → __len__()

    object1 == object2
        → __eq__()

    object1 < object2
        → __lt__()

In the next chapter, we will learn about Operator Overloading
and see how magic methods can be used to define the behavior
of operators such as +, -, ==, <, and others for custom
objects.
"""