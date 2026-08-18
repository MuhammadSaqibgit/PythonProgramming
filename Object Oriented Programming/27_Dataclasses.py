"""
DATACLASSES
"""

# ============================================================
# 1. INTRODUCTION
# ============================================================

"""
In previous chapters, we created classes manually.

When a class mainly stores data, we often have to write a lot
of repetitive code.

For example, we may need to write:

    __init__()
    __repr__()
    __eq__()

again and again.

Python provides a convenient feature called a dataclass for
these situations.

A dataclass can automatically generate several common methods
for us.

We can create a dataclass using:

    @dataclass

from the:

    dataclasses

module.
"""


# ============================================================
# 2. THE BOILERPLATE PROBLEM
# ============================================================

"""
Suppose we want to create a class that stores information about
a student.

Without a dataclass, we might write:
"""


class Student:

    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

    def __repr__(self):
        return (
            f"Student(name={self.name!r}, "
            f"age={self.age!r}, "
            f"grade={self.grade!r})"
        )

    def __eq__(self,other):
        if(not isinstance(other,Student)):
            return NotImplemented

        return (
            self.name==other.name
            and self.age==other.age
            and self.grade==other.grade
        )


student_one=Student("Ayesha",20,"A")

student_two=Student("Ayesha",20,"A")

print(student_one)
print(student_one==student_two)


"""
There is a lot of code here just to create a class that mainly
stores data.

The __init__() method assigns the values.

The __repr__() method controls how the object is represented.

The __eq__() method allows two Student objects to be compared
based on their data.

This repetitive code is often called boilerplate code.

Dataclasses help reduce this boilerplate.
"""


# ============================================================
# 3. WHAT IS A DATACLASS?
# ============================================================

"""
A dataclass is a special type of class designed mainly for
storing data.

We use the @dataclass decorator from the dataclasses module.

Basic syntax:

    from dataclasses import dataclass

    @dataclass
    class ClassName:
        attribute: data_type

Python can automatically create several useful methods for us.
"""


# ============================================================
# 4. CREATING YOUR FIRST DATACLASS
# ============================================================

from dataclasses import dataclass


@dataclass
class StudentRecord:

    name:str
    age:int
    grade:str


student_record=StudentRecord(
    "Bilal",
    21,
    "B"
)

print(student_record)


"""
We did not write __init__() ourselves.

The @dataclass decorator generated it automatically.

Therefore, we can create an object like:

    StudentRecord("Bilal",21,"B")

The generated __init__() assigns the values to the attributes.
"""


# ============================================================
# 5. AUTO-GENERATED __init__()
# ============================================================

"""
One of the most useful features of dataclasses is that Python
automatically generates an __init__() method.

For example:
"""


@dataclass
class Book:

    title:str
    author:str
    pages:int


book_object=Book(
    "Python Fundamentals",
    "David",
    350
)

print(book_object.title)
print(book_object.author)
print(book_object.pages)


"""
Conceptually, Python creates an __init__() similar to:

    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

We do not need to write this repetitive code ourselves.
"""


# ============================================================
# 6. AUTO-GENERATED __repr__()
# ============================================================

"""
Dataclasses also generate a useful __repr__() method by default.

This makes objects easier to inspect and debug.
"""


@dataclass
class ProductInfo:

    name:str
    price:float
    quantity:int


product_object=ProductInfo(
    "Keyboard",
    45.50,
    2
)

print(product_object)


"""
The output will look similar to:

    ProductInfo(name='Keyboard',price=45.5,quantity=2)

The exact representation is generated automatically from the
class name and its fields.

We did not need to write __repr__() manually.
"""


# ============================================================
# 7. AUTO-GENERATED __eq__()
# ============================================================

"""
Dataclasses also generate an __eq__() method by default.

This allows objects to be compared based on their field values.
"""


@dataclass
class Point:

    x:int
    y:int


point_one=Point(10,20)
point_two=Point(10,20)
point_three=Point(5,15)

print(point_one==point_two)
print(point_one==point_three)


"""
The output is:

    True
    False

point_one and point_two contain the same values.

Therefore, they are considered equal.

Without a dataclass, we would normally need to write the
comparison logic ourselves.
"""


# ============================================================
# 8. DATACLASS VS REGULAR CLASS
# ============================================================

"""
Regular class:

    class Employee:

        def __init__(self,name,salary):
            self.name=name
            self.salary=salary

Dataclass:

    @dataclass
    class Employee:
        name: str
        salary: float

The dataclass version is shorter and easier to read when the
class mainly stores data.
"""


# ============================================================
# 9. TYPE ANNOTATIONS
# ============================================================

"""
Dataclasses use type annotations to define their fields.

For example:

    name: str
    age: int
    salary: float

These annotations tell us what type of data is expected.

They also make the class easier to understand.
"""


@dataclass
class EmployeeRecord:

    name:str
    employee_id:int
    salary:float


employee_record=EmployeeRecord(
    "Hassan",
    101,
    55000.0
)

print(employee_record)


"""
Type annotations are required for dataclass fields.

For example:

    name: str

creates a field called name.

The annotation does not automatically force Python to reject a
different type at runtime.

It mainly provides information to Python tools, developers,
linters, and type checkers.
"""


# ============================================================
# 10. ACCESSING DATACLASS ATTRIBUTES
# ============================================================

"""
A dataclass object behaves like a normal Python object.

We can access its attributes using dot notation.
"""


@dataclass
class Movie:

    title:str
    year:int


movie_object=Movie(
    "Example Movie",
    2026
)

print(movie_object.title)
print(movie_object.year)


"""
We can also modify its attributes unless the dataclass is made
frozen.
"""


movie_object.year=2027

print(movie_object.year)


"""
By default, dataclass objects are mutable.
"""


# ============================================================
# 11. DEFAULT VALUES
# ============================================================

"""
Dataclass fields can have default values.

For example:
"""


@dataclass
class UserProfile:

    username:str
    country:str="Pakistan"


user_one=UserProfile("ahmed123")

user_two=UserProfile(
    "sara456",
    "Canada"
)

print(user_one)
print(user_two)


"""
If the country is not provided, Python uses:

    "Pakistan"

If a different value is provided, that value is used instead.
"""


# ============================================================
# 12. MULTIPLE DEFAULT VALUES
# ============================================================

@dataclass
class Laptop:

    brand:str
    ram:int=8
    storage:int=256


laptop_one=Laptop("Dell")

laptop_two=Laptop(
    "Lenovo",
    16,
    512
)

print(laptop_one)
print(laptop_two)


"""
The first object uses the default values:

    ram=8
    storage=256

The second object provides its own values.
"""


# ============================================================
# 13. DEFAULT VALUES MUST FOLLOW NON-DEFAULT VALUES
# ============================================================

"""
A field without a default value must normally come before a
field with a default value.

Correct:

    @dataclass
    class Example:
        name:str
        age:int=18

Incorrect:

    @dataclass
    class Example:
        age:int=18
        name:str

The reason is related to how the automatically generated
__init__() method receives its arguments.
"""


# ============================================================
# 14. USING field()
# ============================================================

"""
The dataclasses module provides:

    field()

for more advanced control over individual fields.

We can import it using:

    from dataclasses import field
"""


from dataclasses import field


# ============================================================
# 15. field() WITH A DEFAULT VALUE
# ============================================================

@dataclass
class AccountInfo:

    owner:str
    balance:float=field(default=0.0)


account_one=AccountInfo("Usman")

account_two=AccountInfo(
    "Nadia",
    2500.0
)

print(account_one)
print(account_two)


"""
field(default=0.0) provides the default value for balance.

For a simple default value, writing:

    balance:float=0.0

is usually enough.

field() becomes more useful when we need additional options.
"""


# ============================================================
# 16. field() WITH default_factory
# ============================================================

"""
One important use of field() is:

    default_factory

It is useful when each object needs its own newly created
mutable value.

For example, suppose each student should have its own list of
subjects.
"""


@dataclass
class Learner:

    name:str
    subjects:list[str]=field(default_factory=list)


learner_one=Learner("Zara")
learner_two=Learner("Owais")

learner_one.subjects.append("Python")

print(learner_one)
print(learner_two)


"""
The two objects have separate lists.

learner_one has:

    ["Python"]

learner_two still has:

    []

This is because default_factory=list creates a new list for
each object.
"""


# ============================================================
# 17. WHY NOT USE [] DIRECTLY?
# ============================================================

"""
For mutable values such as lists and dictionaries, we should
not normally use:

    subjects: list[str]=[]

Instead, use:

    subjects: list[str]=field(
        default_factory=list
    )

This ensures that every object receives its own list.
"""


# ============================================================
# 18. field() WITH A DICTIONARY
# ============================================================

@dataclass
class Configuration:

    name:str
    settings:dict[str,str]=field(
        default_factory=dict
    )


config_one=Configuration("Development")
config_two=Configuration("Production")

config_one.settings["debug"]="True"

print(config_one)
print(config_two)


"""
Each Configuration object receives its own dictionary.
"""


# ============================================================
# 19. field() FOR HIDING A FIELD FROM repr
# ============================================================

"""
field() can also control whether a field appears in the
generated __repr__().

We can use:

    repr=False
"""


@dataclass
class CustomerRecord:

    name:str
    customer_id:int
    password:str=field(repr=False)


customer_record=CustomerRecord(
    "Ali",
    5001,
    "secret123"
)

print(customer_record)


"""
The password field still exists, but it is not included in the
generated representation.

This can be useful for values that we do not want displayed in
the object's representation.
"""


# ============================================================
# 20. field() WITH compare=False
# ============================================================

"""
By default, dataclass fields are used when comparing objects.

We can exclude a field from comparisons using:

    compare=False
"""


@dataclass
class ProductRecord:

    name:str
    price:float
    internal_code:str=field(
        compare=False
    )


product_one=ProductRecord(
    "Mouse",
    20.0,
    "A100"
)

product_two=ProductRecord(
    "Mouse",
    20.0,
    "B200"
)

print(product_one==product_two)


"""
The objects are considered equal because internal_code is not
included in the comparison.
"""


# ============================================================
# 21. FROZEN DATACLASSES
# ============================================================

"""
By default, dataclass objects are mutable.

That means we can change their attributes:

    object.attribute=new_value

Sometimes we want an object whose values cannot be changed
after creation.

We can use:

    frozen=True
"""


@dataclass(frozen=True)
class Coordinate:

    latitude:float
    longitude:float


location=Coordinate(
    32.58,
    73.50
)

print(location)


"""
Now the fields cannot be reassigned.
"""


# ============================================================
# 22. TRYING TO MODIFY A FROZEN DATACLASS
# ============================================================

"""
For example:

    location.latitude = 33.00

will raise a FrozenInstanceError.

This is because the dataclass is frozen.
"""


# ============================================================
# 23. FROZEN DOES NOT MEAN THE ENTIRE OBJECT IS DEEPLY
#     IMMUTABLE
# ============================================================

"""
An important point:

    frozen=True

prevents normal reassignment of dataclass fields.

It does not automatically make every object stored inside those
fields deeply immutable.

For example, a frozen dataclass containing a list can still
contain a mutable list.

The frozen setting mainly prevents reassignment of the fields.
"""


@dataclass(frozen=True)
class TeamInfo:

    name:str
    members:list[str]


team=TeamInfo(
    "Developers",
    ["Ali","Sara"]
)

team.members.append("Omar")

print(team)


"""
The field itself cannot be reassigned:

    team.members=[...]

but the list stored inside the field is still mutable.

This is an important distinction.
"""


# ============================================================
# 24. FROZEN DATACLASS WITH SIMPLE VALUES
# ============================================================

"""
Frozen dataclasses are particularly useful when the fields
contain immutable values such as:

    int
    float
    str
    bool
    tuple

For example:
"""


@dataclass(frozen=True)
class RGBColor:

    red:int
    green:int
    blue:int


blue_color=RGBColor(
    0,
    0,
    255
)

print(blue_color)


"""
This object represents a fixed color.

Once created, its values should not normally change.

A frozen dataclass is useful for this type of data.
"""


# ============================================================
# 25. DATACLASS WITH METHODS
# ============================================================

"""
A dataclass is still a class.

It can contain methods just like a regular class.

For example:
"""


@dataclass
class Rectangle:

    width:float
    height:float

    def area(self):
        return self.width*self.height


rectangle_object=Rectangle(
    10,
    5
)

print("Area:",rectangle_object.area())


"""
The @dataclass decorator handles the data-related boilerplate.

We can still add our own methods when the class needs behavior.
"""


# ============================================================
# 26. DATACLASS WITH A CALCULATED PROPERTY
# ============================================================

"""
Dataclasses can also be used with properties.
"""


@dataclass
class Circle:

    radius:float

    @property
    def diameter(self):
        return self.radius*2


circle_object=Circle(7)

print("Radius:",circle_object.radius)
print("Diameter:",circle_object.diameter)


"""
The dataclass manages the stored data.

The property provides calculated behavior.
"""


# ============================================================
# 27. DATACLASS WITH VALIDATION
# ============================================================

"""
A dataclass does not automatically validate the types of its
fields.

If we need validation, we can still use regular methods or
special methods such as __post_init__().

__post_init__() runs automatically after the generated
__init__().
"""


@dataclass
class ExamResult:

    student_name:str
    score:float

    def __post_init__(self):

        if(not 0<=self.score<=100):
            raise ValueError(
                "Score must be between 0 and 100."
            )


result_object=ExamResult(
    "Hina",
    88
)

print(result_object)


"""
__post_init__() is useful when we need additional initialization
or validation after the automatically generated __init__()
finishes.
"""


# ============================================================
# 28. DATACLASS AND __post_init__()
# ============================================================

"""
The process is approximately:

    1. Dataclass generates __init__().
    2. __init__() stores the field values.
    3. __post_init__() runs automatically.
    4. Additional validation or setup can be performed.

For example:
"""


@dataclass
class Temperature:

    celsius:float

    def __post_init__(self):

        if(self.celsius<-273.15):
            raise ValueError(
                "Temperature cannot be below absolute zero."
            )


temperature=Temperature(25)

print(temperature)


"""
The dataclass still saves us from writing the normal
__init__() method manually.
"""


# ============================================================
# 29. DATACLASS WITH CLASS VARIABLES
# ============================================================

"""
Sometimes a dataclass also needs a class variable.

For class variables, use ClassVar from typing.
"""


from typing import ClassVar


@dataclass
class Employee:

    company: ClassVar[str]="Tech Solutions"

    name:str
    employee_id:int


employee_one=Employee(
    "Hamza",
    101
)

employee_two=Employee(
    "Noor",
    102
)

print(employee_one)
print(employee_one.company)


"""
company is a class variable.

It is not treated as a normal dataclass field.

Therefore, it does not appear in the generated __repr__().
"""


# ============================================================
# 30. DATACLASS WITH A DEFAULT VALUE AND REQUIRED FIELD
# ============================================================

"""
A useful example is a product record.
"""


@dataclass
class InventoryItem:

    name:str
    price:float
    quantity:int=1
    available:bool=True


item_one=InventoryItem(
    "Notebook",
    5.50
)

item_two=InventoryItem(
    "Pen",
    1.25,
    10,
    False
)

print(item_one)
print(item_two)


"""
The first object uses the default values:

    quantity=1
    available=True

The second object provides its own values.
"""


# ============================================================
# 31. AUTO-GENERATED METHODS
# ============================================================

"""
By default, @dataclass can generate several useful methods.

The most important ones for beginners are:

    __init__()
        Creates and initializes the object.

    __repr__()
        Provides a useful representation of the object.

    __eq__()
        Compares objects based on their fields.

For example:
"""


@dataclass
class Device:

    name:str
    price:float


device_one=Device("Tablet",300)
device_two=Device("Tablet",300)

print(device_one)
print(device_one==device_two)


"""
The dataclass generated the required behavior automatically.
"""


# ============================================================
# 32. WHAT IF WE WRITE __init__ OURSELVES?
# ============================================================

"""
By default, @dataclass generates __init__() for us.

However, we can customize dataclass behavior when necessary.

For beginners, the important idea is:

    If the class mainly stores data, let @dataclass generate
    the standard initialization code.

If the class requires very unusual initialization behavior,
a regular class may sometimes be more appropriate.
"""


# ============================================================
# 33. DATACLASS VS REGULAR CLASS
# ============================================================

"""
Use a dataclass when:

    The class mainly stores data.

    The fields are clearly defined.

    You want automatic __init__().

    You want a useful __repr__().

    You want automatic equality comparison.

    You want less repetitive code.

For example:

    Student
    EmployeeRecord
    ProductInfo
    Point
    Configuration
    Coordinates


Use a regular class when:

    The class contains complex behavior.

    Object creation requires complicated logic.

    The class does much more than simply store data.

    You need highly customized behavior.

For example:

    DatabaseConnection
    GameEngine
    FileManager
    NetworkService
"""


# ============================================================
# 34. DATACLASS DOES NOT REPLACE ALL REGULAR CLASSES
# ============================================================

"""
A dataclass is not a replacement for every class.

For example, consider a class responsible for managing a
database connection.

Such a class may contain:

    connect()
    disconnect()
    execute_query()
    reconnect()
    error handling
    connection management

A regular class may be more appropriate.

Dataclasses are particularly useful when the primary purpose of
the class is to represent and store data.
"""


# ============================================================
# 35. REGULAR CLASS VS DATACLASS
# ============================================================

"""
Regular class:

    class Person:

        def __init__(self,name,age):
            self.name=name
            self.age=age

        def __repr__(self):
            return (
                f"Person(name={self.name!r}, "
                f"age={self.age!r})"
            )

        def __eq__(self,other):
            if not isinstance(other,Person):
                return NotImplemented

            return (
                self.name==other.name
                and self.age==other.age
            )


Dataclass:

    @dataclass
    class Person:
        name:str
        age:int


The dataclass version is much shorter.
"""


# ============================================================
# 36. DATACLASS IS STILL A NORMAL CLASS
# ============================================================

"""
It is important to understand that a dataclass is still a
Python class.

We can:

    Create objects.

    Access attributes.

    Modify attributes.

    Define methods.

    Define properties.

    Use inheritance.

    Use class methods.

    Use static methods.

    Use other OOP concepts.

The @dataclass decorator simply provides convenient automatic
behavior for data-oriented classes.
"""


# ============================================================
# 37. DATACLASS WITH INHERITANCE
# ============================================================

"""
Dataclasses can also participate in inheritance.

For example:
"""


@dataclass
class Person:

    name:str


@dataclass
class Student(Person):

    student_id:int


student_object=Student(
    "Maryam",
    501
)

print(student_object)


"""
The child dataclass inherits the name field from Person and adds
its own student_id field.
"""


# ============================================================
# 38. FROZEN DATACLASS AS A DATA OBJECT
# ============================================================

"""
A common use case for frozen dataclasses is representing values
that should not change after creation.
"""


@dataclass(frozen=True)
class Money:

    amount:float
    currency:str


price=Money(
    99.99,
    "USD"
)

print(price)


"""
The price object represents a fixed value.

If we try to change:

    price.amount=120

Python will raise an error because the dataclass is frozen.
"""


# ============================================================
# 39. DATACLASS WITH field() AND default_factory
# ============================================================

"""
Let's combine several features.

We will create a Course dataclass with:

    name
    instructor
    students

Each Course object should receive its own students list.
"""


@dataclass
class Course:

    name:str
    instructor:str
    students:list[str]=field(
        default_factory=list
    )

    def add_student(self,student_name):
        self.students.append(student_name)


python_course=Course(
    "Python Programming",
    "Mr. Ahmed"
)

python_course.add_student("Zoya")
python_course.add_student("Hamid")

print(python_course)


"""
default_factory=list creates a separate list for each Course
object.

The method add_student() provides behavior.

This demonstrates that dataclasses can contain both data and
methods.
"""


# ============================================================
# 40. PRACTICAL EXAMPLE
# ============================================================

"""
Let's create a simple shopping cart item.

The class mainly stores information about a product, so a
dataclass is a good choice.
"""


@dataclass
class CartItem:

    product_name:str
    price:float
    quantity:int=1

    def total_price(self):
        return self.price*self.quantity


cart_item=CartItem(
    "Headphones",
    75.0,
    2
)

print(cart_item)

print(
    "Total price:",
    cart_item.total_price()
)


"""
The dataclass automatically handles the basic data storage.

The total_price() method provides additional behavior.
"""


# ============================================================
# 41. PRACTICAL EXAMPLE WITH VALIDATION
# ============================================================


@dataclass
class BankTransaction:

    transaction_type:str
    amount:float

    def __post_init__(self):

        valid_types={
            "deposit",
            "withdrawal"
        }

        if(self.transaction_type not in valid_types):
            raise ValueError(
                "Invalid transaction type."
            )

        if(self.amount<=0):
            raise ValueError(
                "Amount must be greater than zero."
            )


transaction=BankTransaction(
    "deposit",
    500
)

print(transaction)


"""
The dataclass creates the object automatically.

__post_init__() provides additional validation.
"""


# ============================================================
# 42. IMPORTANT POINT ABOUT TYPE CHECKING
# ============================================================

"""
A common beginner misconception is that:

    @dataclass
    class Student:
        age:int

means Python will automatically reject:

    Student("Ali","twenty")

It does not.

The type annotation:

    age:int

describes the expected type.

Python does not automatically perform runtime type validation
just because a type annotation exists.

If runtime validation is required, we need additional logic or
a suitable validation library.
"""


# ============================================================
# 43. FROZEN DATACLASS AND EQUALITY
# ============================================================

"""
A frozen dataclass can still compare objects based on their
fields.
"""


@dataclass(frozen=True)
class Version:

    major:int
    minor:int


version_one=Version(1,2)
version_two=Version(1,2)

print(version_one==version_two)


"""
The objects contain the same field values, so they compare
equal.
"""


# ============================================================
# 44. WHY DATACLASSES ARE USEFUL
# ============================================================

"""
Dataclasses are useful because they reduce repetitive code.

Without a dataclass, we may need to manually write:

    __init__()
    __repr__()
    __eq__()

With a dataclass, Python can generate these methods
automatically.

This gives us:

    Less code
    Better readability
    Easier maintenance
    Clear field definitions
    Useful default behavior
"""


# ============================================================
# 45. WHEN NOT TO USE A DATACLASS
# ============================================================

"""
Do not automatically convert every class into a dataclass.

A regular class may be better when:

    The class has complex initialization.

    The class primarily performs operations rather than storing
    data.

    You need unusual control over object creation.

    The generated dataclass behavior does not match the desired
    design.

The goal is not to use dataclasses everywhere.

The goal is to use them when they make the class simpler and
clearer.
"""


# ============================================================
# 46. QUICK DECISION GUIDE
# ============================================================

"""
Ask yourself:

    "Is this class mainly a container for data?"

If YES:

    Consider using @dataclass.

If NO:

    A regular class may be more appropriate.

For example:

    Point
    Employee
    StudentRecord
    Product
    Configuration

are often good dataclass candidates.

While:

    DatabaseManager
    GameController
    FileProcessor
    NetworkClient

may be better represented as regular classes.
"""


# ============================================================
# 47. COMMON BEGINNER MISTAKES
# ============================================================

"""
Mistake 1:

Forgetting to import dataclass.

Correct:

    from dataclasses import dataclass


Mistake 2:

Forgetting the @dataclass decorator.

Correct:

    @dataclass
    class Person:
        name:str


Mistake 3:

Forgetting type annotations.

Dataclass fields should be declared with annotations:

    name:str
    age:int


Mistake 4:

Using a mutable object as a shared default.

Avoid:

    items: list=[]


Prefer:

    items: list=field(
        default_factory=list
    )


Mistake 5:

Thinking type annotations automatically validate values.

They do not provide automatic runtime validation.


Mistake 6:

Thinking frozen=True makes every nested object deeply
immutable.

It mainly prevents reassignment of the dataclass fields.
"""


# ============================================================
# 48. COMPLETE EXAMPLE
# ============================================================

"""
The following example combines several concepts from this
chapter.
"""


@dataclass(frozen=True)
class StudentProfile:

    name:str
    age:int
    courses:tuple[str,...]=()

    def course_count(self):
        return len(self.courses)


profile_one=StudentProfile(
    "Sana",
    22,
    ("Python","OOP")
)

profile_two=StudentProfile(
    "Sana",
    22,
    ("Python","OOP")
)

print(profile_one)

print(
    "Courses:",
    profile_one.course_count()
)

print(
    "Profiles equal:",
    profile_one==profile_two
)


"""
This example demonstrates:

    @dataclass
    frozen=True
    Automatic __init__()
    Automatic __repr__()
    Automatic __eq__()
    Type annotations
    Default values
    Custom methods
"""


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. A dataclass is a convenient way to create classes that
   mainly store data.

2. Dataclasses are provided by Python's dataclasses module.

3. We import dataclass using:

       from dataclasses import dataclass

4. We create a dataclass using:

       @dataclass
       class Person:
           name:str
           age:int

5. The @dataclass decorator can automatically generate
   __init__().

6. The generated __init__() initializes the declared fields.

7. Dataclasses can automatically generate __repr__().

8. __repr__() provides a useful representation of the object.

9. Dataclasses can automatically generate __eq__().

10. __eq__() compares objects based on their fields.

11. Dataclass fields are normally declared using type
    annotations.

12. Example:

       name:str
       age:int
       salary:float

13. Dataclass fields can have default values.

14. Example:

       country: str="Pakistan"

15. A field without a default value should normally appear
    before fields with default values.

16. The field() function provides additional control over
    dataclass fields.

17. field(default=value) can define a default value.

18. field(default_factory=list) can create a new list for each
    object.

19. default_factory is especially useful for mutable values
    such as lists and dictionaries.

20. field(repr=False) can prevent a field from appearing in the
    generated __repr__().

21. field(compare=False) can exclude a field from generated
    equality comparisons.

22. Dataclasses are mutable by default.

23. We can make a dataclass immutable-like using:

       @dataclass(frozen=True)

24. A frozen dataclass does not allow normal reassignment of
    its fields.

25. frozen=True does not automatically make nested mutable
    objects deeply immutable.

26. A dataclass can contain normal methods.

27. A dataclass can contain properties.

28. A dataclass can also use __post_init__().

29. __post_init__() runs automatically after the generated
    __init__().

30. __post_init__() is useful for validation and additional
    initialization.

31. Type annotations in dataclasses do not automatically
    perform runtime type checking.

32. Dataclasses can also use class variables with ClassVar.

33. Dataclasses can participate in inheritance.

34. Dataclasses are still normal Python classes.

35. They are mainly useful for reducing repetitive code.

36. Use a dataclass when a class primarily represents data.

37. Use a regular class when the class mainly contains complex
    behavior or requires highly customized initialization.

38. A dataclass does not replace every regular class.

39. The main benefit of a dataclass is reducing boilerplate
    while keeping the data structure clear.

A simple way to remember it is:

    Regular class
        → You write more of the common code yourself.

    Dataclass
        → Python generates common data-related code for you.

    @dataclass
        → automatic __init__, __repr__, __eq__, and more.

    frozen=True
        → prevents normal reassignment of fields.

    field()
        → gives additional control over individual fields.

The main idea to remember is:

    Use a dataclass when your class is primarily a clean,
    structured container for data and you want Python to handle
    the repetitive parts automatically.

In the next chapter, we will bring together many of the OOP
concepts learned in this folder by building a Real-World
Mini Project.
"""