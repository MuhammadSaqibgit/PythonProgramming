"""
REAL-WORLD MINI PROJECT
LIBRARY MANAGEMENT SYSTEM

This project brings together many of the Object-Oriented
Programming concepts learned throughout this folder.

Concepts used in this project:

    - Classes and Objects
    - self
    - Constructors
    - Instance Variables
    - Methods
    - Encapsulation
    - Properties
    - Inheritance
    - Method Overriding
    - Polymorphism
    - Dataclasses
    - Magic Methods
    - __str__()
    - __len__()
    - if __name__=="__main__"

The goal is not to build a complete professional library
application.

The goal is to see how different OOP concepts can work together
in one small and understandable project.
"""


# ============================================================
# 1. IMPORTS
# ============================================================

from dataclasses import dataclass


# ============================================================
# 2. DATACLASS: BOOK
# ============================================================

"""
A Book mainly stores information about a book.

Therefore, a dataclass is a good choice for representing it.

The @dataclass decorator automatically provides common methods
such as __init__(), __repr__(), and __eq__().
"""


@dataclass
class Book:

    title:str
    author:str
    isbn:str
    available:bool=True

    def __str__(self):
        status="Available" if self.available else "Borrowed"

        return (
            f"{self.title} by {self.author} "
            f"({status})"
        )


"""
Example:

    Book(
        "Python Basics",
        "Ahmed Khan",
        "ISBN001"
    )

creates a Book object.

The available field has a default value of True.
"""


# ============================================================
# 3. BASE CLASS: LIBRARY MEMBER
# ============================================================

"""
LibraryMember is the base class for people who can use the
library.

It demonstrates:

    - Classes
    - self
    - Constructor
    - Instance variables
    - Encapsulation
    - Properties
    - Methods
    - Magic method __str__()
"""


class LibraryMember:

    def __init__(self,member_id,name):

        self.member_id=member_id
        self.name=name

        # Protected by name convention.
        self._borrowed_books=[]

        # Private attribute using name mangling.
        self.__active=True

    # --------------------------------------------------------
    # Property: active
    # --------------------------------------------------------

    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self,value):

        if(not isinstance(value,bool)):
            raise TypeError(
                "active must be True or False."
            )

        self.__active = value

    # --------------------------------------------------------
    # Borrow a book
    # --------------------------------------------------------

    def borrow_book(self,book):

        if(not self.active):
            print(
                f"{self.name} cannot borrow books "
                "because the membership is inactive."
            )
            return False

        if(not book.available):
            print(
                f"'{book.title}' is already borrowed."
            )
            return False

        book.available=False
        self._borrowed_books.append(book)

        print(
            f"{self.name} borrowed "
            f"'{book.title}'."
        )

        return True

    # --------------------------------------------------------
    # Return a book
    # --------------------------------------------------------

    def return_book(self,book):

        if(book not in self._borrowed_books):
            print(
                f"{self.name} does not have "
                f"'{book.title}'."
            )
            return False

        book.available=True
        self._borrowed_books.remove(book)

        print(
            f"{self.name} returned "
            f"'{book.title}'."
        )

        return True

    # --------------------------------------------------------
    # Display borrowed books
    # --------------------------------------------------------

    def show_borrowed_books(self):

        if(not self._borrowed_books):
            print(
                f"{self.name} has no borrowed books."
            )
            return

        print(
            f"\nBooks borrowed by {self.name}:"
        )

        for book in self._borrowed_books:
            print(f"- {book.title}")

    # --------------------------------------------------------
    # __str__() magic method
    # --------------------------------------------------------

    def __str__(self):

        status=(
            "Active"
            if self.active
            else "Inactive"
        )

        return (
            f"Member ID: {self.member_id}, "
            f"Name: {self.name}, "
            f"Status: {status}"
        )


"""
The class contains the private attribute:

    __active

External code should not directly modify this attribute.

Instead, it can use the property:

    member.active

The property allows us to control how the value is accessed
and modified.

This is an example of encapsulation.
"""


# ============================================================
# 4. CHILD CLASS: PREMIUM MEMBER
# ============================================================

"""
PremiumMember inherits from LibraryMember.

This demonstrates inheritance.

PremiumMember is a specialized type of LibraryMember.

It also overrides borrow_book() to provide different behavior.

This gives us an example of:

    Inheritance
    Method overriding
    Polymorphism
"""


class PremiumMember(LibraryMember):

    def __init__(
        self,
        member_id,
        name,
        discount_percent
    ):

        # Call the parent constructor.
        super().__init__(
            member_id,
            name
        )

        self.discount_percent=discount_percent

    # --------------------------------------------------------
    # Overridden method
    # --------------------------------------------------------

    def borrow_book(self,book):

        print(
            f"Premium member {self.name} "
            "is borrowing a book."
        )

        return super().borrow_book(book)

    # --------------------------------------------------------
    # __str__() override
    # --------------------------------------------------------

    def __str__(self):

        return (
            f"Premium Member ID: {self.member_id}, "
            f"Name: {self.name}, "
            f"Discount: {self.discount_percent}%"
        )


"""
PremiumMember gets the methods and attributes of
LibraryMember through inheritance.

It then adds:

    discount_percent

and overrides:

    borrow_book()
    __str__()

The use of:

    super().__init__()

allows the parent class to initialize the common attributes.
"""


# ============================================================
# 5. LIBRARY CLASS
# ============================================================

"""
The Library class manages the collection of books and members.

It demonstrates composition.

A Library object contains Book objects and Member objects.

The Library is responsible for managing these objects.
"""


class Library:

    def __init__(self,name):

        self.name=name
        self.books=[]
        self.members=[]

    # --------------------------------------------------------
    # Add a book
    # --------------------------------------------------------

    def add_book(self,book):

        self.books.append(book)

        print(
            f"Added '{book.title}' "
            f"to the library."
        )

    # --------------------------------------------------------
    # Add a member
    # --------------------------------------------------------

    def add_member(self,member):

        self.members.append(member)

        print(
            f"Added {member.name} "
            "as a library member."
        )

    # --------------------------------------------------------
    # Display available books
    # --------------------------------------------------------

    def show_available_books(self):

        print(
            f"\nAvailable books in {self.name}:"
        )

        available_books=[
            book
            for book in self.books
            if book.available
        ]

        if(not available_books):
            print("No books are currently available.")
            return

        for book in available_books:
            print(f"- {book}")

    # --------------------------------------------------------
    # Find a member
    # --------------------------------------------------------

    def find_member(self,member_id):

        for member in self.members:

            if(member.member_id==member_id):
                return member

        return None

    # --------------------------------------------------------
    # Find a book
    # --------------------------------------------------------

    def find_book(self,isbn):

        for book in self.books:

            if(book.isbn==isbn):
                return book

        return None

    # --------------------------------------------------------
    # __len__() magic method
    # --------------------------------------------------------

    def __len__(self):

        return len(self.books)

    # --------------------------------------------------------
    # __str__() magic method
    # --------------------------------------------------------

    def __str__(self):

        return (
            f"{self.name} "
            f"({len(self.books)} books, "
            f"{len(self.members)} members)"
        )


"""
Because we defined __len__(), we can use:

    len(library)

Python will call:

    library.__len__()

automatically.

Similarly, because we defined __str__(), we can use:

    print(library)

Python will call:

    library.__str__()
"""


# ============================================================
# 6. POLYMORPHISM EXAMPLE
# ============================================================

"""
The following function does not need to know the exact type of
member.

It simply expects the object to have a borrow_book() method.

Both:

    LibraryMember

and:

    PremiumMember

provide this method.

However, PremiumMember has overridden the method.

Therefore, the same function can work with both objects.

This is polymorphism.
"""


def borrow_for_member(member,book):

    print(
        f"\nProcessing borrowing request "
        f"for {member.name}..."
    )

    return member.borrow_book(book)


# ============================================================
# 7. DRIVER / DEMO SECTION
# ============================================================

"""
The following section runs the project demonstration.

The condition:

    if __name__=="__main__":

ensures that this code runs when this file is executed
directly.

It will not automatically run when the file is imported into
another Python file.
"""


if __name__=="__main__":

    print("="*60)
    print("LIBRARY MANAGEMENT SYSTEM")
    print("="*60)

    # --------------------------------------------------------
    # Create Library
    # --------------------------------------------------------

    central_library=Library(
        "Central City Library"
    )

    print(
        f"\nLibrary created: "
        f"{central_library}"
    )

    # --------------------------------------------------------
    # Create Book objects
    # --------------------------------------------------------

    book_one=Book(
        "Python Programming",
        "Adeel Hussain",
        "ISBN101"
    )

    book_two=Book(
        "Object-Oriented Python",
        "Sara Malik",
        "ISBN102"
    )

    book_three=Book(
        "Learning Algorithms",
        "Usman Raza",
        "ISBN103"
    )

    # --------------------------------------------------------
    # Add books to library
    # --------------------------------------------------------

    central_library.add_book(book_one)
    central_library.add_book(book_two)
    central_library.add_book(book_three)

    # --------------------------------------------------------
    # len() uses __len__()
    # --------------------------------------------------------

    print(
        f"\nTotal books: {len(central_library)}"
    )

    # --------------------------------------------------------
    # Create normal member
    # --------------------------------------------------------

    regular_member=LibraryMember(
        101,
        "Hassan"
    )

    # --------------------------------------------------------
    # Create premium member
    # --------------------------------------------------------

    premium_member=PremiumMember(
        202,
        "Mariam",
        15
    )

    # --------------------------------------------------------
    # Add members to library
    # --------------------------------------------------------

    central_library.add_member(
        regular_member
    )

    central_library.add_member(
        premium_member
    )

    # --------------------------------------------------------
    # Display members
    # --------------------------------------------------------

    print("\nMembers:")

    print(regular_member)
    print(premium_member)

    # --------------------------------------------------------
    # Encapsulation through property
    # --------------------------------------------------------

    print(
        f"\nIs {regular_member.name}'s "
        f"membership active? "
        f"{regular_member.active}"
    )

    regular_member.active=False

    print(
        f"Membership changed to: "
        f"{regular_member.active}"
    )

    # --------------------------------------------------------
    # Try borrowing while inactive
    # --------------------------------------------------------

    regular_member.borrow_book(book_one)

    # --------------------------------------------------------
    # Reactivate membership
    # --------------------------------------------------------

    regular_member.active=True

    print(
        f"\n{regular_member.name}'s "
        "membership has been reactivated."
    )

    # --------------------------------------------------------
    # Borrow a book
    # --------------------------------------------------------

    regular_member.borrow_book(book_one)

    # --------------------------------------------------------
    # Display available books
    # --------------------------------------------------------

    central_library.show_available_books()

    # --------------------------------------------------------
    # Premium member borrowing
    # --------------------------------------------------------

    premium_member.borrow_book(book_two)

    # --------------------------------------------------------
    # Polymorphism
    # --------------------------------------------------------

    print("\n--- Polymorphism Example ---")

    book_three.available = True

    borrow_for_member(
        regular_member,
        book_three
    )

    # --------------------------------------------------------
    # Method overriding
    # --------------------------------------------------------

    print(
        "\nThe premium member uses an overridden "
        "borrow_book() method."
    )

    # --------------------------------------------------------
    # Show borrowed books
    # --------------------------------------------------------

    regular_member.show_borrowed_books()
    premium_member.show_borrowed_books()

    # --------------------------------------------------------
    # Return a book
    # --------------------------------------------------------

    print("\n--- Returning a Book ---")

    regular_member.return_book(
        book_one
    )

    # --------------------------------------------------------
    # Show available books again
    # --------------------------------------------------------

    central_library.show_available_books()

    # --------------------------------------------------------
    # Dataclass comparison
    # --------------------------------------------------------

    print("\n--- Dataclass Example ---")

    another_book=Book(
        "Python Programming",
        "Adeel Hussain",
        "ISBN101"
    )

    print(
        "Book one:",
        book_one
    )

    print(
        "Another book:",
        another_book
    )

    print(
        "Are they equal?",
        book_one==another_book
    )

    # --------------------------------------------------------
    # Final library information
    # --------------------------------------------------------

    print("\n--- Final Library Information ---")

    print(central_library)

    print(
        f"Total books in library: "
        f"{len(central_library)}"
    )

    print("="*60)
    print("END OF DEMONSTRATION")
    print("="*60)


"""
==============================================================
CONCEPTS USED IN THIS PROJECT
==============================================================

1. CLASSES AND OBJECTS

We created classes such as:

    Book
    LibraryMember
    PremiumMember
    Library

Then we created objects from those classes.


2. self

Instance methods use self to access the current object's data.

For example:

    self.name
    self.books
    self.active


3. CONSTRUCTORS

The __init__() method initializes objects.

For example:

    def __init__(self,member_id,name):

        self.member_id=member_id
        self.name=name


4. ENCAPSULATION

The LibraryMember class contains:

    self.__active

The double underscore makes this attribute private through
Python's name-mangling mechanism.

Access is controlled through the active property.


5. PROPERTIES

The active property allows controlled access to the private
__active attribute.

We use:

    @property

and:

    @active.setter


6. INHERITANCE

PremiumMember inherits from:

    LibraryMember

using:

    class PremiumMember(LibraryMember):


7. super()

The child class uses:

    super().__init__(member_id,name)

to call the parent constructor.

It also uses:

    super().borrow_book(book)

to reuse the parent's borrowing behavior.


8. METHOD OVERRIDING

PremiumMember provides its own version of:

    borrow_book()

and:

    __str__()

This is called method overriding.


9. POLYMORPHISM

The function:

    borrow_for_member()

can work with both LibraryMember and PremiumMember objects.

The correct borrow_book() method is selected based on the
actual object.


10. DATACLASSES

Book is created using:

    @dataclass

This gives Book useful automatically generated behavior such as:

    __init__()
    __repr__()
    __eq__()


11. MAGIC METHODS

We used:

    __str__()
    __len__()

These allow our custom objects to work naturally with Python's
built-in functions.

For example:

    print(library)

uses:

    __str__()

while:

    len(library)

uses:

    __len__()


12. COMPOSITION

A Library object contains Book and Member objects.

For example:

    self.books
    self.members

This demonstrates how objects can work together to build a
larger system.


13. if __name__=="__main__"

The demo code is placed inside:

    if __name__=="__main__":

This is a common Python pattern for code that should execute
when the file is run directly.


==============================================================
FINAL IDEA
==============================================================

This project demonstrates an important idea:

OOP concepts are not normally used separately in real programs.

A real application often combines many concepts.

For example, this small library system uses:

    Classes
        ↓
    Objects
        ↓
    Encapsulation
        ↓
    Inheritance
        ↓
    Method Overriding
        ↓
    Polymorphism
        ↓
    Dataclasses
        ↓
    Magic Methods

Each concept solves a different problem.

The purpose of this project is not to create a complete
production-ready library system.

The purpose is to understand how the OOP concepts learned in
this folder can work together to create a small, organized
Python application.
"""