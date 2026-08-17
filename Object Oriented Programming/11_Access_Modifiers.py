"""
ACCESS MODIFIERS
"""


# ============================================================
# 1. INTRODUCTION TO ACCESS MODIFIERS
# ============================================================

"""
Access modifiers are used to describe who should be allowed
to access the data and methods of a class.

In languages such as Java and C++, access modifiers are an
important part of the language.

For example, they provide keywords such as:

    public
    protected
    private

Python takes a different approach.

Python does not have strict access modifiers in the same way
as Java or C++.

Instead, Python mainly uses naming conventions to communicate
how an attribute or method should be used.

Python follows a philosophy that can be summarized as:

"We are all consenting adults."

This means Python generally trusts programmers to use class
members responsibly.

Python provides conventions and mechanisms for indicating
different levels of intended access, but it does not usually
prevent access completely.
"""


# ============================================================
# 2. PYTHON'S APPROACH TO ACCESS
# ============================================================

"""
In Python, members of a class are commonly divided into:

1. Public members
2. Protected members
3. Private members

These are indicated by naming conventions.

Public:
    variable

Protected:
    _variable

Private:
    __variable

It is important to understand that these do not work exactly
like public, protected, and private members in Java or C++.
"""


# ============================================================
# 3. PUBLIC MEMBERS
# ============================================================

"""
A public member is the default type of member in Python.

If we create an attribute without a leading underscore,
it is considered public.

Example:

self.name

Public members can normally be accessed from outside the class.
"""


class Student:

    def __init__(self,name):
        self.name=name


student_record=Student("Ayesha")

print("Student Name:",student_record.name)


# ============================================================
# 4. PUBLIC METHODS
# ============================================================

"""
Methods are also public by default.

If a method does not start with an underscore, it is normally
considered public.

Public methods are intended to be used by code outside the
class.
"""


class Calculator:

    def add(self,first_number,second_number):
        return first_number+second_number


calculator_object=Calculator()

result=calculator_object.add(10,20)

print("Result:",result)


# ============================================================
# 5. WHEN TO USE PUBLIC MEMBERS
# ============================================================

"""
Use public members when they are part of the normal interface
of your class.

For example, a Student class may intentionally expose:

    name

A BankAccount class may intentionally provide methods such as:

    deposit()
    withdraw()
    show_balance()

These members are meant to be used by code outside the class.
"""


class BankAccount:

    def __init__(self,owner):
        self.owner=owner

    def show_owner(self):
        print("Account Owner:",self.owner)


account_record=BankAccount("Hassan")

print("Owner:",account_record.owner)

account_record.show_owner()


# ============================================================
# 6. PROTECTED MEMBERS
# ============================================================

"""
A protected member is usually indicated by a single underscore.

Example:

self._balance

The single underscore is a convention that means:

"This member is intended for internal use or use by subclasses."

Python does not completely prevent access to a protected member.

It is still possible to access it from outside the class.

The underscore is mainly a signal to other programmers.
"""


class Employee:

    def __init__(self,salary):
        self._salary=salary


employee_record=Employee(60000)

print("Salary:",employee_record._salary)


# ============================================================
# 7. WHY USE A SINGLE UNDERSCORE?
# ============================================================

"""
The single underscore communicates an intention.

When another programmer sees:

    _salary

they understand that the attribute is not intended to be
part of the normal public interface.

It does NOT mean:

"This attribute cannot be accessed."

It means more like:

"Please treat this as an internal implementation detail."
"""


class Product:

    def __init__(self,price):
        self._price=price

    def show_price(self):
        print("Price:",self._price)


product_item=Product(2500)

product_item.show_price()

# This is technically possible,
# but _price is intended for internal use.
print("Internal Price:",product_item._price)


# ============================================================
# 8. PROTECTED METHODS
# ============================================================

"""
The single underscore can also be used with methods.

For example:

    _calculate_tax()

This communicates that the method is intended for internal
use or for use by subclasses.
"""


class Invoice:

    def calculate_total(self,price):
        tax=self._calculate_tax(price)
        return price+tax

    def _calculate_tax(self,price):
        return price*0.05


invoice_record=Invoice()

print("Total:",invoice_record.calculate_total(1000))


# ============================================================
# 9. PRIVATE MEMBERS
# ============================================================

"""
Python uses a double underscore at the beginning of a name
to trigger name mangling.

Example:

self.__password

This is commonly described as a private member.

However, Python's private mechanism is different from the
strict private access found in languages such as Java and C++.

Python changes the name internally so that it is harder to
access accidentally.
"""


class UserAccount:

    def __init__(self,password):
        self.__password=password


user_record=UserAccount("secret123")

# Direct access using __password will not work normally.

# print(user_record.__password)


# ============================================================
# 10. NAME MANGLING
# ============================================================

"""
When Python sees a name beginning with double underscores,
it performs name mangling.

For example:

self.__password

inside the UserAccount class is internally changed roughly to:

self._UserAccount__password

The class name is added to the beginning of the attribute.

This makes accidental access or accidental name conflicts
less likely.

It does not provide absolute security.
"""


class Account:

    def __init__(self,pin):
        self.__pin=pin


account_object=Account(1234)

# The following would normally cause an AttributeError:

# print(account_object.__pin)

# The name-mangled form can technically be accessed:

print("PIN:",account_object._Account__pin)


# ============================================================
# 11. WHY IS NAME MANGLING USED?
# ============================================================

"""
Name mangling is mainly useful for avoiding accidental name
conflicts, especially when inheritance is involved.

Suppose a parent class and a child class both use the same
double-underscore attribute name.

Python mangles the names using the respective class names.

This helps keep the two attributes separate.
"""


class Parent:

    def __init__(self):
        self.__value="Parent Value"

    def show_parent_value(self):
        print(self.__value)


class Child(Parent):

    def __init__(self):
        super().__init__()
        self.__value="Child Value"

    def show_child_value(self):
        print(self.__value)


child_object=Child()

child_object.show_parent_value()
child_object.show_child_value()


# ============================================================
# 12. UNDERSTANDING THE NAME-MANGLING RESULT
# ============================================================

"""
In the previous example, these two attributes are different:

Parent's:

    self.__value

becomes approximately:

    self._Parent__value

Child's:

    self.__value

becomes approximately:

    self._Child__value

Therefore, both values can exist inside the same object.
"""


class BaseClass:

    def __init__(self):
        self.__code="Base Code"

    def show_base_code(self):
        print("Base:",self.__code)


class DerivedClass(BaseClass):

    def __init__(self):
        super().__init__()
        self.__code="Derived Code"

    def show_derived_code(self):
        print("Derived:",self.__code)


derived_object=DerivedClass()

derived_object.show_base_code()
derived_object.show_derived_code()

print("Base Attribute:",
      derived_object._BaseClass__code)

print("Derived Attribute:",
      derived_object._DerivedClass__code)


# ============================================================
# 13. PUBLIC VS PROTECTED VS PRIVATE
# ============================================================

"""
The naming conventions can be summarized as:

Public:
    name

Protected:
    _name

Private:
    __name

Public:
    Intended for normal external use.

Protected:
    Intended mainly for internal use and subclasses.

Private:
    Intended to avoid accidental access and name conflicts
    through name mangling.
"""


class Example:

    def __init__(self):
        self.public_data="Public"
        self._protected_data="Protected"
        self.__private_data="Private"


example_object=Example()

print(example_object.public_data)

print(example_object._protected_data)

# print(example_object.__private_data)

print(example_object._Example__private_data)


# ============================================================
# 14. ACCESS MODIFIERS IN JAVA/C++ VS PYTHON
# ============================================================

"""
Python's approach is different from languages such as Java
and C++.

In Java or C++, access modifiers can be enforced by the
language.

For example:

public
    Generally accessible.

protected
    Access is restricted according to language rules.

private
    Access is restricted to the class according to language
    rules.

Python does not provide these exact access restrictions.

Instead:

name
    Public by default.

_name
    Protected by convention.

__name
    Name mangling is applied.

Therefore, Python relies more on conventions and programmer
discipline than strict access control.
"""


# ============================================================
# 15. SIMPLE COMPARISON TABLE
# ============================================================

"""
---------------------------------------------------------------
Python Name        Meaning                  Strictly Hidden?
---------------------------------------------------------------
name               Public                   No
_name              Protected by convention  No
__name             Private/name mangling    No
---------------------------------------------------------------

The important point is:

Python does not make these members completely inaccessible.

The underscore patterns communicate how the programmer
intends the member to be used.
"""


# ============================================================
# 16. PUBLIC MEMBER EXAMPLE
# ============================================================

"""
A public member is appropriate when outside code is expected
to use it directly.
"""


class Car:

    def __init__(self,brand):
        self.brand=brand


family_car=Car("Toyota")

print("Brand:", family_car.brand)


# ============================================================
# 17. PROTECTED MEMBER EXAMPLE
# ============================================================

"""
A protected member can be useful for implementation details
that may also be used by subclasses.

For example, a base class may provide an internal method
that subclasses can use.
"""


class Vehicle:

    def __init__(self):
        self._engine_status="Stopped"

    def _start_engine(self):
        self._engine_status="Running"


class Motorcycle(Vehicle):

    def start(self):
        self._start_engine()
        print("Motorcycle engine:",self._engine_status)


motorcycle_object=Motorcycle()

motorcycle_object.start()


# ============================================================
# 18. PRIVATE MEMBER EXAMPLE
# ============================================================

"""
A private-style member can be useful when we want to reduce
the possibility of accidental access or name conflicts.

For example, an object may contain an internal identifier
that should not normally be accessed directly.
"""


class Record:

    def __init__(self,record_id):
        self.__record_id=record_id

    def show_record_id(self):
        print("Record ID:",self.__record_id)


record_object=Record(101)

record_object.show_record_id()


# ============================================================
# 19. ACCESSING PRIVATE MEMBERS
# ============================================================

"""
Remember that double underscores do not create absolute
security.

Python's name mangling changes:

    __record_id

to approximately:

    _Record__record_id

Therefore, it is technically possible to access it using
the mangled name.

However, this should normally be avoided because it bypasses
the intended interface of the class.
"""


class Document:

    def __init__(self,title):
        self.__title=title


document_object=Document("Python Notes")

# Not recommended in normal code.
print(document_object._Document__title)


# ============================================================
# 20. WHY NOT MAKE EVERYTHING PRIVATE?
# ============================================================

"""
It is not necessary to make every attribute private.

Python encourages simple and readable code.

Use public members when they are intentionally part of the
class interface.

Use a single underscore when something is intended to be
internal.

Use double underscores when name mangling can help prevent
accidental conflicts or accidental access.

The goal is not to hide everything.

The goal is to communicate how the class should be used.
"""


# ============================================================
# 21. ACCESS MODIFIERS AND PROPERTIES
# ============================================================

"""
Properties can be combined with underscore conventions.

For example, we can store a value internally as:

self._balance

and expose it through a property:

@property
def balance(self):
    return self._balance

This provides a clean public interface while keeping the
internal implementation separate.
"""


class BankAccount:

    def __init__(self,balance):
        self._balance=balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,new_balance):
        if(new_balance>=0):
            self._balance=new_balance
        else:
            raise ValueError("Balance cannot be negative.")


account_record=BankAccount(5000)

print("Balance:",account_record.balance)

account_record.balance=7500

print("Updated Balance:",account_record.balance)


# ============================================================
# 22. WHEN TO USE PUBLIC MEMBERS
# ============================================================

"""
Use public members when:

- The member is part of the normal interface.
- Other parts of the program are expected to use it.
- There is no need to hide implementation details.

Example:

customer.name
customer.email

These can reasonably be public attributes depending on
the design of the class.
"""


class Customer:

    def __init__(self,name,email):
        self.name=name
        self.email=email


customer_record=Customer(
    "Mariam",
    "mariam@example.com"
)

print(customer_record.name)
print(customer_record.email)


# ============================================================
# 23. WHEN TO USE PROTECTED MEMBERS
# ============================================================

"""
Use a single underscore when:

- The member is an implementation detail.
- You want to communicate that outside code should normally
  not access it.
- Subclasses may reasonably need to use it.

Remember:

The single underscore is a convention, not a strict
restriction.
"""


class FileProcessor:

    def __init__(self,filename):
        self._filename=filename

    def _validate_filename(self):
        return "." in self._filename

    def process(self):
        if self._validate_filename():
            print("Processing:",self._filename)
        else:
            print("Invalid filename.")


file_processor=FileProcessor("report.txt")

file_processor.process()


# ============================================================
# 24. WHEN TO USE PRIVATE MEMBERS
# ============================================================

"""
Use double underscores when:

- You want name mangling.
- You want to reduce accidental name conflicts.
- A member should be strongly treated as an internal
  implementation detail.
- You are designing a class hierarchy where similarly named
  internal attributes could conflict.

Do not use double underscores simply because you want
absolute security.

Python's double underscore mechanism is not a security feature.
"""


class Configuration:

    def __init__(self,secret_key):
        self.__secret_key=secret_key

    def is_configured(self):
        return self.__secret_key is not None


configuration_object=Configuration("ABC123")

print(
    "Configuration Ready:",
    configuration_object.is_configured()
)


# ============================================================
# 25. COMPLETE PRACTICAL EXAMPLE
# ============================================================

"""
Let's combine public, protected, and private members.

We will create a BankAccount class.

Public:
    owner

Protected:
    _balance

Private:
    __account_number

The account number is treated as an internal detail.

The balance is protected by convention and can be controlled
through methods.
"""


class BankAccount:

    def __init__(self,owner,account_number,balance):
        self.owner=owner
        self._balance=balance
        self.__account_number=account_number

    def deposit(self, amount):
        if(amount>0):
            self._balance+=amount

    def show_balance(self):
        print("Balance:",self._balance)

    def show_account_number(self):
        print("Account Number:",self.__account_number)


bank_account=BankAccount(
    "Hassan",
    "ACC-1025",
    5000
)

# Public member
print("Owner:",bank_account.owner)

# Protected member
print("Balance:",bank_account._balance)

# Private-style member should normally be accessed through
# a public method.
bank_account.show_account_number()

bank_account.deposit(2000)

bank_account.show_balance()


# ============================================================
# 26. IMPORTANT DIFFERENCE FROM JAVA/C++
# ============================================================

"""
In Java or C++, you may see code such as:

private int balance;

The language itself restricts direct access according to
its access rules.

In Python:

self.__balance

does not mean that the value is completely inaccessible.

Python performs name mangling.

Similarly:

self._balance

does not mean that Python will prevent external code from
accessing it.

The programmer can still write:

object._balance

Python simply communicates:

"This is intended to be internal."

Therefore, Python's approach is more about conventions,
readability, and programmer responsibility.
"""


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. Python does not have strict access modifiers in the same
   way as Java or C++.

2. Python generally follows the idea that programmers are
   responsible for using objects correctly.

3. Public members are the default.

4. A public member has no leading underscore:

   name

5. Public members are intended for normal external use.

6. A single leading underscore indicates a protected-style
   member:

   _name

7. A single underscore is a convention, not a strict
   restriction.

8. Protected-style members are generally intended for
   internal use or use by subclasses.

9. A double leading underscore triggers name mangling:

   __name

10. Name mangling changes the internal name approximately to:

    _ClassName__name

11. Name mangling helps prevent accidental name conflicts
    and accidental access.

12. Double underscores do not provide absolute privacy or
    security.

13. You can technically access a name-mangled attribute using
    its mangled name, although this is normally discouraged.

14. Use public members when they are part of the normal
    interface of the class.

15. Use a single underscore when a member is intended to be
    internal but may reasonably be used by subclasses.

16. Use double underscores when name mangling is useful for
    avoiding accidental conflicts or strongly signaling an
    internal implementation detail.

Simple comparison:

    name
        Public

    _name
        Protected by convention

    __name
        Private-style with name mangling

The most important idea is:

Python does not focus on completely preventing access.
Instead, it uses naming conventions and name mangling to
communicate how class members are intended to be used.

In the next chapter, we will learn about encapsulation and
how it helps combine data and the methods that control that
data inside a class.
"""