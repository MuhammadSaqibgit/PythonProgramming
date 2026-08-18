"""
OPERATOR OVERLOADING
"""


# ============================================================
# 1. INTRODUCTION TO OPERATOR OVERLOADING
# ============================================================

"""
In the previous chapter, we learned about Magic Methods.

Magic methods allow our custom objects to work with Python's
built-in operations.

Operator overloading is one of the important uses of magic
methods.

Operator overloading means:

    Giving a Python operator a specific meaning for our
    custom objects.

For example, Python already knows how to add numbers:

    10+20

It knows how to concatenate strings:

    "Hello "+"Python"

But what should happen if we write:

    object1+object2

where object1 and object2 are objects created from our own
class?

Python does not automatically know what addition should mean
for our custom objects.

We can define that behavior using a magic method such as:

    __add__()

This is called operator overloading.
"""


# ============================================================
# 2. WHAT IS AN OPERATOR?
# ============================================================

"""
An operator is a symbol that performs an operation.

Some common Python operators are:

    +       Addition
    -       Subtraction
    *       Multiplication
    /       Division
    ==      Equal to
    <       Less than
    >       Greater than
    <=      Less than or equal to
    >=      Greater than or equal to

For example:
"""


first_number=10
second_number=5

print(first_number+second_number)
print(first_number-second_number)
print(first_number*second_number)
print(first_number==second_number)
print(first_number<second_number)


"""
Python already knows how these operators work with integers.

Operator overloading allows us to define similar behavior for
objects created from our own classes.
"""


# ============================================================
# 3. WHY DO WE NEED OPERATOR OVERLOADING?
# ============================================================

"""
Suppose we create a Point class.

A point has:

    x coordinate
    y coordinate

Now suppose we have:

    point_one
    point_two

It would be convenient to write:

    point_one+point_two

and get a new point containing the sum of their coordinates.

For example:

    (2,3)+(4,5)

could produce:

    (6,8)

But Python does not automatically know that this is what we
want.

We can teach Python this behavior using:

    __add__()
"""


# ============================================================
# 4. __add__() METHOD
# ============================================================

"""
The magic method:

    __add__()

is used to define the behavior of:

    +

For example:

    object1+object2

is associated with:

    object1.__add__(object2)
"""


# ============================================================
# 5. SIMPLE __add__() EXAMPLE
# ============================================================

class Point:

    def __init__(self,x_coordinate,y_coordinate):
        self.x=x_coordinate
        self.y=y_coordinate

    def __add__(self,other):
        new_x=self.x+other.x
        new_y=self.y+other.y

        return Point(new_x,new_y)


first_point=Point(2,3)
second_point=Point(4,5)

result_point=first_point+second_point

print(result_point.x)
print(result_point.y)


"""
The expression:

    first_point+second_point

causes Python to use:

    first_point.__add__(second_point)

Our __add__() method adds the corresponding coordinates and
returns a new Point object.

So:

    (2,3)+(4,5)

becomes:

    (6,8)
"""


# ============================================================
# 6. MAKING THE RESULT EASIER TO READ
# ============================================================

"""
We can combine operator overloading with __str__() from the
previous chapter.
"""


class Coordinate:

    def __init__(self,horizontal,vertical):
        self.horizontal=horizontal
        self.vertical=vertical

    def __add__(self,other):
        return Coordinate(
            self.horizontal+other.horizontal,
            self.vertical+other.vertical
        )

    def __str__(self):
        return f"({self.horizontal},{self.vertical})"


location_one=Coordinate(3,4)
location_two=Coordinate(5,2)

combined_location=location_one+location_two

print(combined_location)


"""
Output:

    (8,6)

Now our custom Coordinate objects behave naturally with +.
"""


# ============================================================
# 7. THE GENERAL IDEA OF __add__()
# ============================================================

"""
The general pattern is:

    class ClassName:

        def __add__(self, other):
            # define addition
            return ...


When we write:

    object_a+object_b

Python can use:

    object_a.__add__(object_b)

The parameter:

    self

refers to the object on the left side.

The parameter:

    other

refers to the object on the right side.

For example:

    first_point+second_point

means conceptually:

    first_point.__add__(second_point)
"""


# ============================================================
# 8. OVERLOADING -
# ============================================================

"""
The subtraction operator:

    -

can be overloaded using:

    __sub__()

For example:
"""


class Vector:

    def __init__(self,x_value,y_value):
        self.x=x_value
        self.y=y_value

    def __sub__(self,other):
        return Vector(
            self.x-other.x,
            self.y-other.y
        )

    def __str__(self):
        return f"({self.x}, {self.y})"


vector_one=Vector(10,8)
vector_two=Vector(3,2)

difference_vector=vector_one-vector_two

print(difference_vector)


"""
The expression:

    vector_one-vector_two

uses:

    vector_one.__sub__(vector_two)

The result is:

    (7,6)
"""


# ============================================================
# 9. OVERLOADING *
# ============================================================

"""
The multiplication operator:

    *

can be overloaded using:

    __mul__()

For example, we can multiply a Vector by a number.
"""


class Vector:

    def __init__(self,x_value,y_value):
        self.x=x_value
        self.y=y_value

    def __mul__(self,number):
        return Vector(
            self.x*number,
            self.y*number
        )

    def __str__(self):
        return f"({self.x},{self.y})"


direction_vector=Vector(4,3)

scaled_vector=direction_vector*3

print(scaled_vector)


"""
The expression:

    direction_vector*3

uses:

    direction_vector.__mul__(3)

The result is:

    (12,9)
"""


# ============================================================
# 10. OVERLOADING ==
# ============================================================

"""
The equality operator:

    ==

can be overloaded using:

    __eq__()

For example:
"""


class Rectangle:

    def __init__(self,length,width):
        self.length=length
        self.width=width

    def __eq__(self,other):
        return (
            self.length==other.length
            and self.width==other.width
        )


rectangle_one=Rectangle(10,5)
rectangle_two=Rectangle(10,5)
rectangle_three=Rectangle(8,4)

print(rectangle_one==rectangle_two)
print(rectangle_one==rectangle_three)


"""
The first comparison is:

    True

because both rectangles have the same dimensions.

The second comparison is:

    False

because the dimensions are different.

The expression:

    rectangle_one==rectangle_two

can use:

    rectangle_one.__eq__(rectangle_two)
"""


# ============================================================
# 11. OVERLOADING <
# ============================================================

"""
The less-than operator:

    <

can be overloaded using:

    __lt__()

For example, we can compare products based on their prices.
"""


class Product:

    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __lt__(self,other):
        return self.price<other.price


cheap_product=Product("Notebook",5)
expensive_product=Product("Backpack",30)

print(cheap_product<expensive_product)


"""
The result is:

    True

because:

    5<30

Python uses:

    cheap_product.__lt__(expensive_product)
"""


# ============================================================
# 12. COMMON OPERATOR MAGIC METHODS
# ============================================================

"""
Here are some important operator magic methods:

    Operator        Magic Method

    +               __add__()
    -               __sub__()
    *               __mul__()
    /               __truediv__()
    //              __floordiv__()
    %               __mod__()
    **              __pow__()

    ==              __eq__()
    !=              __ne__()
    <               __lt__()
    <=              __le__()
    >               __gt__()
    >=              __ge__()

There are many more magic methods, but these are some of the
most commonly encountered ones.
"""


# ============================================================
# 13. OPERATOR OVERLOADING DOES NOT CHANGE THE OPERATOR
# ============================================================

"""
Operator overloading does not create a new operator.

We are simply defining what an existing operator means when it
is used with our custom objects.

For example:

    +

already exists in Python.

We are only telling Python:

    "When + is used with objects of this class, perform this
     particular operation."
"""


# ============================================================
# 14. SAME OPERATOR, DIFFERENT BEHAVIOR
# ============================================================

"""
The + operator already behaves differently depending on the
objects being used.

For integers:
"""


print(10+20)


"""
For strings:
"""


print("Hello "+"Python")


"""
For lists:
"""


print([1,2]+[3,4])


"""
The same operator:

    +

has different behavior depending on the operands.

Operator overloading allows our custom classes to participate
in this same idea.
"""


# ============================================================
# 15. CUSTOM VECTOR EXAMPLE
# ============================================================

"""
Let's create a more complete Vector class.

A vector can contain multiple coordinate values.

For simplicity, we will use a two-dimensional vector.
"""


class Vector:

    def __init__(self,x_component,y_component):
        self.x=x_component
        self.y=y_component

    def __add__(self,other):
        return Vector(
            self.x+other.x,
            self.y+other.y
        )

    def __str__(self):
        return f"Vector({self.x},{self.y})"


movement_one=Vector(4,7)
movement_two=Vector(2,5)

total_movement=movement_one+movement_two

print(total_movement)


"""
We can think of this as:

    (4,7)+(2,5)

which gives:

    (6,12)

The Vector class now behaves naturally with +.
"""


# ============================================================
# 16. ADDING MORE OPERATORS TO VECTOR
# ============================================================

"""
We can define several operators for the same class.

For example:

    +   → vector addition
    -   → vector subtraction
    *   → scalar multiplication
"""


class Vector:

    def __init__(self,x_component,y_component):
        self.x=x_component
        self.y=y_component

    def __add__(self,other):
        return Vector(
            self.x+other.x,
            self.y+other.y
        )

    def __sub__(self,other):
        return Vector(
            self.x-other.x,
            self.y-other.y
        )

    def __mul__(self,multiplier):
        return Vector(
            self.x*multiplier,
            self.y*multiplier
        )

    def __str__(self):
        return f"({self.x},{self.y})"


base_vector=Vector(6,8)
change_vector=Vector(2,3)

print("Addition:",base_vector+change_vector)
print("Subtraction:",base_vector-change_vector)
print("Multiplication:",base_vector*2)


"""
The class now supports:

    vector+vector
    vector-vector
    vector*number

This makes the class feel much more natural to use.
"""


# ============================================================
# 17. RETURNING A NEW OBJECT
# ============================================================

"""
Notice that our operator methods usually return a new object.

For example:
"""


class Point:

    def __init__(self,x_value,y_value):
        self.x=x_value
        self.y=y_value

    def __add__(self,other):
        return Point(
            self.x+other.x,
            self.y+other.y
        )


point_a=Point(1,2)
point_b=Point(3,4)

point_c=point_a+point_b


"""
point_a and point_b remain unchanged.

A new Point object is returned and stored in point_c.

This is often a useful design for mathematical objects such as
vectors and points.
"""


# ============================================================
# 18. OPERATOR OVERLOADING AND IMMUTABILITY
# ============================================================

"""
When an operator method returns a new object instead of changing
the existing object, the original objects remain unchanged.

For example:

    result=point_a+point_b

does not necessarily modify:

    point_a
    point_b

Instead, it creates a new result.

This makes operations easier to reason about.
"""


# ============================================================
# 19. OVERLOADING == FOR CUSTOM OBJECTS
# ============================================================

"""
Equality should represent something meaningful for the class.

For a Student class, we might compare:

    student ID

For a Product class, we might compare:

    name and price

For a Point class, we might compare:

    x and y coordinates
"""


class Point:

    def __init__(self,x_value,y_value):
        self.x=x_value
        self.y=y_value

    def __eq__(self,other):
        return (
            self.x==other.x
            and self.y==other.y
        )

    def __str__(self):
        return f"({self.x},{self.y})"


point_one=Point(5,7)
point_two=Point(5,7)
point_three=Point(8,2)

print(point_one==point_two)
print(point_one==point_three)


"""
This makes equality meaningful for Point objects.

Two Point objects are considered equal when their coordinates
are equal.
"""


# ============================================================
# 20. OVERLOADING < FOR CUSTOM OBJECTS
# ============================================================

"""
We can also define a meaningful ordering.

For example, suppose we have a class representing a test
result.

We can compare students according to their scores.
"""


class TestResult:

    def __init__(self,student_name,marks):
        self.student_name=student_name
        self.marks=marks

    def __lt__(self,other):
        return self.marks<other.marks

    def __str__(self):
        return f"{self.student_name}: {self.marks}"


result_one=TestResult("Sara",72)
result_two=TestResult("Hamza",88)

print(result_one<result_two)


"""
The comparison now makes sense:

    Sara's score<Hamza's score

because:

    72<88
"""


# ============================================================
# 21. OPERATOR OVERLOADING WITH MULTIPLE OPERATORS
# ============================================================

"""
A class can define several operator behaviors at the same time.
"""


class Money:

    def __init__(self,amount):
        self.amount=amount

    def __add__(self,other):
        return Money(self.amount+other.amount)

    def __sub__(self,other):
        return Money(self.amount-other.amount)

    def __eq__(self,other):
        return self.amount==other.amount

    def __lt__(self,other):
        return self.amount<other.amount

    def __str__(self):
        return f"${self.amount}"


wallet_one=Money(500)
wallet_two=Money(200)

print("Addition:",wallet_one+wallet_two)
print("Subtraction:",wallet_one-wallet_two)
print("Equal:",wallet_one==wallet_two)
print("Less than:",wallet_one<wallet_two)


"""
The Money class now supports several operators naturally.
"""


# ============================================================
# 22. WHY OPERATOR OVERLOADING IS USEFUL
# ============================================================

"""
Without operator overloading, we might need to create methods
such as:

    add_vector()
    subtract_vector()
    multiply_vector()
    compare_vector()

For example:

    vector_one.add_vector(vector_two)

But with operator overloading, we can write:

    vector_one+vector_two

The second form is shorter, clearer, and more natural when the
operation has a mathematical meaning.
"""


# ============================================================
# 23. OPERATOR OVERLOADING MAKES CLASSES FEEL NATIVE
# ============================================================

"""
A well-designed custom class can feel like a built-in Python
type.

For example, after implementing __len__(), we can write:

    len(custom_object)

After implementing __eq__(), we can write:

    object1==object2

After implementing __add__(), we can write:

    object1+object2

Instead of learning a completely separate API, Python users
can use familiar language features.

This is one of the main benefits of operator overloading.
"""


# ============================================================
# 24. OPERATOR OVERLOADING AND READABILITY
# ============================================================

"""
Good operator overloading should make code easier to read.

For mathematical classes, this can be very useful.

For example:

    total_vector=vector_a+vector_b

is immediately understandable.

Compare it with:

    total_vector=vector_a.add_vector(vector_b)

Both can work, but the first version matches the mathematical
meaning of the operation.
"""


# ============================================================
# 25. DO NOT OVERLOAD OPERATORS ARBITRARILY
# ============================================================

"""
Operator overloading should be meaningful.

For example, using + to combine two vectors makes sense.

But defining + to delete an object would be confusing.

Good operator overloading should match what users naturally
expect the operator to mean.

For example:

    + → addition or combining
    - → subtraction or difference
    * → multiplication or scaling
    == → equality
    < → ordering

The behavior should be intuitive.
"""


# ============================================================
# 26. TYPE CHECKING IN OPERATOR METHODS
# ============================================================

"""
When writing operator methods, it is often useful to consider
what type of object is being passed as `other`.

For example:
"""


class Distance:

    def __init__(self,meters):
        self.meters=meters

    def __add__(self,other):
        if not isinstance(other,Distance):
            return NotImplemented

        return Distance(self.meters+other.meters)

    def __str__(self):
        return f"{self.meters} meters"


first_distance=Distance(100)
second_distance=Distance(250)

total_distance=first_distance+second_distance

print(total_distance)


"""
The check:

    isinstance(other,Distance)

makes sure that the operation is being performed with another
Distance object.

If the operation is not supported, returning:

    NotImplemented

is a standard way to tell Python that this operand type is not
supported by this implementation.
"""


# ============================================================
# 27. __add__() WITH A NUMBER
# ============================================================

"""
Operator overloading does not require both operands to be
objects of the same class.

For example, we can define a class where:

    custom_object + number

is meaningful.
"""


class Counter:

    def __init__(self,value):
        self.value=value

    def __add__(self,number):
        return Counter(self.value+number)

    def __str__(self):
        return str(self.value)


counter_object=Counter(10)

new_counter=counter_object+5

print(new_counter)


"""
Here:

    counter_object+5

calls:

    counter_object.__add__(5)

The method adds the number to the stored value.
"""


# ============================================================
# 28. REVERSE OPERATORS
# ============================================================

"""
Python also provides reverse operator methods.

For example:

    __radd__()

can define behavior when the custom object appears on the
right side of +.

For example:

    5+object

may use:

    object.__radd__(5)

This is useful when we want our custom class to support
operations where the custom object appears on the right side.

We will keep reverse operators outside the main focus of this
chapter, but it is useful to know that they exist.
"""


# ============================================================
# 29. A PRACTICAL VECTOR EXAMPLE
# ============================================================

"""
Let's build a complete Vector class.

This example demonstrates:

    __init__()
    __str__()
    __add__()
    __sub__()
    __mul__()
    __eq__()
    __lt__()
"""


class Vector:

    def __init__(self,x_component,y_component):
        self.x=x_component
        self.y=y_component

    def __str__(self):
        return f"Vector({self.x},{self.y})"

    def __add__(self,other):
        return Vector(
            self.x+other.x,
            self.y+other.y
        )

    def __sub__(self,other):
        return Vector(
            self.x-other.x,
            self.y-other.y
        )

    def __mul__(self,multiplier):
        return Vector(
            self.x*multiplier,
            self.y*multiplier
        )

    def __eq__(self,other):
        if not isinstance(other,Vector):
            return NotImplemented

        return (
            self.x==other.x
            and self.y==other.y
        )

    def __lt__(self,other):
        if not isinstance(other,Vector):
            return NotImplemented

        self_length_squared=self.x**2+self.y**2
        other_length_squared=other.x**2+other.y**2

        return self_length_squared<other_length_squared


first_vector=Vector(3,4)
second_vector=Vector(1,2)

print("First vector:",first_vector)
print("Second vector:",second_vector)

print("Addition:",first_vector+second_vector)
print("Subtraction:",first_vector-second_vector)
print("Multiplication:",first_vector*2)

print("Equal:",first_vector==second_vector)
print("Less than:",first_vector<second_vector)


"""
Our Vector class now supports familiar Python operators.

The class feels much more natural to use because we can write:

    first_vector + second_vector
    first_vector - second_vector
    first_vector * 2
    first_vector == second_vector
    first_vector < second_vector
"""


# ============================================================
# 30. UNDERSTANDING self AND other
# ============================================================

"""
When we write:

    vector_a+vector_b

Python can think of it approximately as:

    vector_a.__add__(vector_b)

Therefore:

    self
        → vector_a

    other
        → vector_b

For example:
"""


class Pair:

    def __init__(self,first_value,second_value):
        self.first=first_value
        self.second=second_value

    def __add__(self,other):
        return Pair(
            self.first+other.first,
            self.second+other.second
        )


pair_one=Pair(10,20)
pair_two=Pair(5,8)

pair_three=pair_one+pair_two


"""
During:

    pair_one+pair_two

the method behaves conceptually like:

    pair_one.__add__(pair_two)

So:

    self  → pair_one
    other → pair_two
"""


# ============================================================
# 31. OPERATOR OVERLOADING IS NOT THE SAME AS METHOD OVERLOADING
# ============================================================

"""
Operator overloading and method overloading are different
concepts.

Operator overloading:

    Defines how operators work with custom objects.

Examples:

    __add__()
    __sub__()
    __eq__()

Method overloading traditionally means having multiple methods
with the same name but different parameter lists.

Python does not support traditional method overloading in the
same way as languages such as Java or C++.

Do not confuse these two concepts.
"""


# ============================================================
# 32. BUILT-IN TYPES ALSO USE SPECIAL METHODS
# ============================================================

"""
Operator overloading is not something only custom classes use.

Python's built-in types also implement special methods.

For example:

    10+20

works because integers have appropriate special behavior.

Similarly:

    "Hello "+"World"

works because strings define how + should behave.

Our custom classes can participate in the same protocol by
implementing the appropriate magic methods.
"""


# ============================================================
# 33. OPERATOR OVERLOADING AND PYTHON'S DATA MODEL
# ============================================================

"""
Python uses a system of special methods to define how objects
behave.

This is often called Python's data model.

For example:

    __len__()
    __str__()
    __eq__()
    __add__()

are part of this system.

By implementing these methods, our classes can integrate with
Python's syntax and built-in operations.

You do not need to memorize every special method.

Learn them as you encounter the behavior you need to customize.
"""


# ============================================================
# 34. WHEN SHOULD YOU USE OPERATOR OVERLOADING?
# ============================================================

"""
Operator overloading is particularly useful when the operation
has a natural meaning for your object.

Good examples include:

    Vector+Vector
    Point+Point
    Money+Money
    Date+TimeDelta
    Matrix*Matrix

Comparison operators can also make sense for:

    scores
    prices
    distances
    dates
    measurements

The important rule is:

    Use operators when the meaning is clear and intuitive.
"""


# ============================================================
# 35. WHEN SHOULD YOU AVOID OPERATOR OVERLOADING?
# ============================================================

"""
Avoid operator overloading when the operation would be
confusing or surprising.

For example, if:

    employee1+employee2

means:

    delete employee2

that would be a poor design.

A user reading the code would reasonably expect + to represent
some form of addition or combination.

Good class design should make operator behavior predictable.
"""


# ============================================================
# 36. SUMMARY OF THE MAIN OPERATORS
# ============================================================

"""
The operators covered in this chapter are:

    +       → __add__()

    -       → __sub__()

    *       → __mul__()

    ==      → __eq__()

    <       → __lt__()


For example:

    object_a+object_b

uses:

    object_a.__add__(object_b)

Similarly:

    object_a-object_b

uses:

    object_a.__sub__(object_b)

    object_a*object_b

uses:

    object_a.__mul__(object_b)

    object_a==object_b

uses:

    object_a.__eq__(object_b)

    object_a<object_b

uses:

    object_a.__lt__(object_b)
"""


# ============================================================
# 37. FINAL PRACTICAL EXAMPLE
# ============================================================

"""
Let's create a simple Point class one final time.

This is a good example because adding points has an intuitive
meaning in this context.
"""


class Point:

    def __init__(self,x_coordinate,y_coordinate):
        self.x=x_coordinate
        self.y=y_coordinate

    def __add__(self,other):
        if not isinstance(other,Point):
            return NotImplemented

        return Point(
            self.x+other.x,
            self.y+other.y
        )

    def __sub__(self,other):
        if not isinstance(other,Point):
            return NotImplemented

        return Point(
            self.x-other.x,
            self.y-other.y
        )

    def __eq__(self,other):
        if not isinstance(other,Point):
            return NotImplemented

        return (
            self.x==other.x
            and self.y==other.y
        )

    def __lt__(self,other):
        if not isinstance(other,Point):
            return NotImplemented

        self_distance=self.x**2+self.y**2
        other_distance=other.x**2+other.y**2

        return self_distance<other_distance

    def __str__(self):
        return f"Point({self.x},{self.y})"


start_point=Point(2,3)
end_point=Point(5,7)

sum_point=start_point+end_point
difference_point=end_point-start_point

print("Start point:",start_point)
print("End point:",end_point)
print("Added points:",sum_point)
print("Difference:",difference_point)
print("Points equal:",start_point==end_point)
print("Start point<End point:",start_point<end_point)


"""
The Point class now works naturally with:

    +
    -
    ==
    <

This is the main purpose of operator overloading.
"""


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. Operator overloading means defining how operators behave
   when they are used with custom objects.

2. Python already supports operators for built-in types.

3. For example:

       10+20

   works because Python knows how addition works for integers.

4. Python does not automatically know what:

       object1+object2

   should mean for every custom class.

5. We can define this behavior using magic methods.

6. The + operator can be overloaded using:

       __add__()

7. The - operator can be overloaded using:

       __sub__()

8. The * operator can be overloaded using:

       __mul__()

9. The == operator can be overloaded using:

       __eq__()

10. The < operator can be overloaded using:

        __lt__()

11. For example:

        point_a+point_b

    can use:

        point_a.__add__(point_b)

12. In an operator method:

        self

    refers to the object on the left side of the operator.

13. The parameter:

        other

    generally refers to the object or value on the right side.

14. Operator overloading can make mathematical classes such
    as Vector and Point much easier to use.

15. For example:

        vector_a+vector_b

    is more natural than:

        vector_a.add_vector(vector_b)

16. Operator overloading can make custom classes feel similar
    to Python's built-in types.

17. Good operator overloading should have an intuitive meaning.

18. The + operator should generally represent some form of
    addition or combination.

19. The - operator should generally represent subtraction or
    difference.

20. The * operator should generally represent multiplication
    or scaling.

21. The == operator should represent meaningful equality.

22. The < operator should represent a meaningful ordering.

23. Operator overloading does not create new operators.

24. It defines how existing Python operators behave for custom
    objects.

25. Built-in Python types also use special methods internally.

26. Operator overloading is closely related to Python's data
    model and magic methods.

27. Returning a new object from an operator method is often
    useful for mathematical objects because the original
    objects remain unchanged.

28. Returning NotImplemented is a standard way to indicate that
    an operator implementation does not support the other
    operand's type.

29. There are many other operator-related magic methods in
    Python.

30. You do not need to memorize all of them at once. Learn the
    ones that are useful for the classes you create.

The main idea to remember is:

    Operator overloading allows custom objects to work with
    familiar Python operators.

For example:

    object1+object2
        → __add__()

    object1-object2
        → __sub__()

    object1*object2
        → __mul__()

    object1==object2
        → __eq__()

    object1<object2
        → __lt__()

By defining these methods, we can make our custom classes feel
natural and "native" to Python.

In the next chapter, we will compare Composition and
Inheritance and learn when an object should contain another
object instead of inheriting from it.
"""