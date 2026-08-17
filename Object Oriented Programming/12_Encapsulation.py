"""
ENCAPSULATION
"""


# ============================================================
# 1. INTRODUCTION TO ENCAPSULATION
# ============================================================

"""
Encapsulation is one of the important concepts of
Object-Oriented Programming.

Encapsulation means combining data and the methods that work
with that data inside a single class.

It also means controlling how the internal data of an object
can be accessed and changed.

In simple words:

    Encapsulation=Data+Methods+Controlled Access

Instead of allowing outside code to freely change important
internal data, we can provide controlled methods or properties
to manage that data.

This helps protect the internal state of an object.
"""


# ============================================================
# 2. WHY DO WE NEED ENCAPSULATION?
# ============================================================

"""
Suppose we create a BankAccount class.

A bank account has a balance.

If we allow the balance to be changed directly, someone could
accidentally assign an invalid value:

    account.balance=-50000

This could make the object inconsistent.

Instead, we can control how the balance changes.

For example:

    deposit()
    withdraw()

These methods can check whether an operation is valid before
changing the balance.
"""


# ============================================================
# 3. WITHOUT ENCAPSULATION
# ============================================================

"""
Let's first see a simple example where the balance can be
changed directly.

There is no control over the data.
"""


class SimpleAccount:

    def __init__(self,balance):
        self.balance=balance


simple_account=SimpleAccount(5000)

print("Original Balance:",simple_account.balance)

simple_account.balance=-10000

print("Changed Balance:",simple_account.balance)


"""
The problem is that the balance can now contain an invalid
value.

This is one of the problems encapsulation helps us solve.
"""


# ============================================================
# 4. BUNDLING DATA AND METHODS TOGETHER
# ============================================================

"""
One important part of encapsulation is bundling related data
and methods together inside a class.

For example, a BankAccount class can contain:

Data:
    owner
    balance

Methods:
    deposit()
    withdraw()
    show_balance()

The data and the operations that work with that data belong
together inside the same class.
"""


class BankAccount:

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        self.balance-=amount

    def show_balance(self):
        print("Balance:",self.balance)


account_record=BankAccount("Hassan",5000)

account_record.deposit(2000)
account_record.withdraw(1000)

account_record.show_balance()


# ============================================================
# 5. CONTROLLED ACCESS TO DATA
# ============================================================

"""
The previous example bundles the data and methods together,
but the balance is still publicly accessible.

A better design is to treat the balance as internal data and
allow it to be changed through controlled operations.

We can use a protected-style attribute:

    self._balance

The single underscore communicates that the attribute is
intended for internal use.

We can then provide methods such as:

    deposit()
    withdraw()

to control how the balance changes.
"""


class SecureAccount:

    def __init__(self,owner,balance):
        self.owner=owner
        self._balance=balance

    def deposit(self,amount):
        if(amount>0):
            self._balance+=amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self,amount):
        if(amount<=0):
            print("Withdrawal amount must be positive.")
        elif(amount>self._balance):
            print("Insufficient balance.")
        else:
            self._balance-=amount

    def show_balance(self):
        print("Balance:",self._balance)


secure_account=SecureAccount("Mariam",10000)

secure_account.deposit(3000)
secure_account.withdraw(2500)

secure_account.show_balance()


# ============================================================
# 6. VALIDATING DATA THROUGH METHODS
# ============================================================

"""
Encapsulation allows us to put validation logic inside the
class.

For example, a deposit should not accept zero or a negative
amount.

A withdrawal should not allow more money to be withdrawn
than the current balance.

The class controls these operations.
"""


class CustomerAccount:

    def __init__(self,owner,balance):
        self.owner=owner
        self._balance=balance

    def deposit(self,amount):
        if(amount<=0):
            print("Deposit must be greater than zero.")
            return

        self._balance+=amount
        print("Deposit successful.")

    def withdraw(self,amount):
        if(amount<=0):
            print("Withdrawal must be greater than zero.")
            return

        if(amount>self._balance):
            print("Insufficient funds.")
            return

        self._balance-=amount
        print("Withdrawal successful.")

    def show_balance(self):
        print("Current Balance:",self._balance)


customer_account=CustomerAccount("Ali",8000)

customer_account.deposit(2000)
customer_account.withdraw(1500)

customer_account.show_balance()

customer_account.withdraw(20000)


# ============================================================
# 7. USING PRIVATE-STYLE DATA
# ============================================================

"""
We can use a double underscore when we want to make an
attribute private-style.

For example:

    self.__balance

Python applies name mangling to this attribute.

This makes accidental access more difficult.

However, remember that Python does not provide absolute
private access in the same way as languages such as Java
or C++.

The purpose is mainly to protect internal implementation
details and avoid accidental access or name conflicts.
"""


class PrivateAccount:

    def __init__(self,balance):
        self.__balance=balance

    def show_balance(self):
        print("Balance:",self.__balance)


private_account=PrivateAccount(12000)

private_account.show_balance()

# Direct access using __balance will not normally work.

# print(private_account.__balance)


# ============================================================
# 8. ENCAPSULATION WITH PRIVATE DATA AND METHODS
# ============================================================

"""
We can combine private-style data with methods that control
access to that data.

The outside code does not need to know how the balance is
stored internally.

It simply uses the public methods provided by the class.
"""


class ControlledAccount:

    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance

    def deposit(self,amount):
        if(amount>0):
            self.__balance+=amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self,amount):
        if(amount<=0):
            print("Invalid withdrawal amount.")
        elif(amount>self.__balance):
            print("Insufficient balance.")
        else:
            self.__balance-=amount
            print("Withdrawal successful.")

    def show_balance(self):
        print("Balance:",self.__balance)


controlled_account=ControlledAccount("Noor",15000)

controlled_account.deposit(2500)
controlled_account.withdraw(4000)

controlled_account.show_balance()


# ============================================================
# 9. ENCAPSULATION WITH PROPERTIES
# ============================================================

"""
Encapsulation can also be implemented using properties.

A property allows us to control how an attribute is read or
changed.

For example, we can store the actual balance internally as:

    self._balance

and expose it through:

    @property
    def balance(self):

The setter can validate a new value before storing it.
"""


class PropertyAccount:

    def __init__(self,balance):
        self.balance=balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,new_balance):
        if(new_balance>=0):
            self._balance=new_balance
        else:
            raise ValueError("Balance cannot be negative.")


property_account=PropertyAccount(5000)

print("Balance:",property_account.balance)

property_account.balance=7500

print("Updated Balance:",property_account.balance)


# ============================================================
# 10. WHY PROPERTY ALONE IS NOT ENOUGH
# ============================================================

"""
A property can control how an attribute is accessed and
modified.

However, encapsulation is a broader concept.

Encapsulation is not simply:

    @property

It is about designing a class so that its internal data and
the operations that control that data are kept together and
accessed in a controlled way.

Properties, naming conventions, and methods can all be used
together to achieve encapsulation.
"""


# ============================================================
# 11. BANK ACCOUNT EXAMPLE
# ============================================================

"""
Let's create a more realistic BankAccount class.

The account will contain:

    owner
    _balance

The balance will not be changed directly by normal program
operations.

Instead, the account provides:

    deposit()
    withdraw()

This gives the class control over changes to its internal
state.
"""


class BankAccount:

    def __init__(self,owner,balance):
        self.owner=owner
        self._balance=balance

    @property
    def balance(self):
        return self._balance

    def deposit(self,amount):
        if(amount<=0):
            raise ValueError(
                "Deposit amount must be greater than zero."
            )

        self._balance+=amount

    def withdraw(self,amount):
        if(amount<=0):
            raise ValueError(
                "Withdrawal amount must be greater than zero."
            )

        if(amount>self._balance):
            raise ValueError(
                "Insufficient balance."
            )

        self._balance-=amount


bank_account=BankAccount("Ayesha",10000)

print("Owner:",bank_account.owner)
print("Balance:",bank_account.balance)

bank_account.deposit(3000)

print("After Deposit:",bank_account.balance)

bank_account.withdraw(2500)

print("After Withdrawal:",bank_account.balance)


# ============================================================
# 12. WHY IS BALANCE READ-ONLY?
# ============================================================

"""
In the previous example, balance has a getter but no setter.

That means we can read:

    bank_account.balance

but we cannot normally write:

    bank_account.balance=50000

The balance can only be changed through:

    deposit()

or:

    withdraw()

This is an example of controlled access.

The class decides how the balance is allowed to change.
"""


class ProtectedBankAccount:

    def __init__(self,balance):
        self._balance=balance

    @property
    def balance(self):
        return self._balance

    def deposit(self,amount):
        if(amount>0):
            self._balance+=amount

    def withdraw(self,amount):
        if(0<amount<=self._balance):
            self._balance-=amount


protected_account=ProtectedBankAccount(7000)

print("Balance:",protected_account.balance)

protected_account.deposit(1000)

print("Balance:",protected_account.balance)

protected_account.withdraw(2000)

print("Balance:",protected_account.balance)


# ============================================================
# 13. WHAT IF WE TRY TO CHANGE BALANCE DIRECTLY?
# ============================================================

"""
Because balance is a read-only property, assigning a new value
to it will raise an AttributeError.

For example:

protected_account.balance=50000

There is no balance setter.

The correct approach is to use the methods provided by the
class.
"""


# Uncomment the following line to see the error.

# protected_account.balance=50000


# ============================================================
# 14. INTERNAL STATE
# ============================================================

"""
The internal state of an object means the data that represents
the current condition of that object.

For a BankAccount, the internal state may include:

    owner
    balance

For example:

A balance of 5000 means the account is currently holding
5000 units of currency.

Encapsulation helps protect this internal state from invalid
changes.
"""


class Wallet:

    def __init__(self,owner,amount):
        self.owner=owner
        self._amount=amount

    @property
    def amount(self):
        return self._amount

    def add_money(self,value):
        if(value>0):
            self._amount+=value

    def spend_money(self,value):
        if(0<value<=self._amount):
            self._amount-=value


wallet_object=Wallet("Bilal",3000)

print("Amount:",wallet_object.amount)

wallet_object.add_money(1000)
wallet_object.spend_money(500)

print("Final Amount:",wallet_object.amount)


# ============================================================
# 15. ENCAPSULATION PROTECTS DATA FROM INVALID OPERATIONS
# ============================================================

"""
Without encapsulation, outside code may perform operations
that do not make sense.

For example:

    account.balance=-5000

With encapsulation, the class can decide:

    Negative balances are not allowed.

The class can reject the operation instead of allowing an
invalid state.
"""


class SavingsAccount:

    def __init__(self,balance):
        if(balance<0):
            raise ValueError("Initial balance cannot be negative.")

        self._balance=balance

    @property
    def balance(self):
        return self._balance

    def deposit(self,amount):
        if(amount<=0):
            raise ValueError("Deposit must be positive.")

        self._balance+=amount

    def withdraw(self,amount):
        if(amount<=0):
            raise ValueError("Withdrawal must be positive.")

        if(amount>self._balance):
            raise ValueError("Insufficient balance.")

        self._balance-=amount


savings_account=SavingsAccount(20000)

savings_account.deposit(5000)
savings_account.withdraw(3000)

print("Savings Balance:",savings_account.balance)


# ============================================================
# 16. ENCAPSULATION HIDES IMPLEMENTATION DETAILS
# ============================================================

"""
Another benefit of encapsulation is that users of a class do
not need to know how the class internally performs its work.

For example, someone using BankAccount only needs to know:

    deposit()
    withdraw()
    balance

They do not need to know exactly how the balance is stored
or how the validation is implemented.
"""


class DigitalWallet:

    def __init__(self,owner,balance):
        self.owner=owner
        self._balance=balance

    @property
    def balance(self):
        return self._balance

    def deposit(self,amount):
        if(amount>0):
            self._balance+=amount

    def withdraw(self,amount):
        if(0<amount<=self._balance):
            self._balance-=amount


digital_wallet=DigitalWallet("Mariam",5000)

digital_wallet.deposit(1500)
digital_wallet.withdraw(1000)

print("Wallet Balance:",digital_wallet.balance)


# ============================================================
# 17. BENEFIT: DATA PROTECTION
# ============================================================

"""
The first major benefit of encapsulation is data protection.

The class can prevent invalid values from entering its internal
state.

For example:

    balance>=0

can be enforced by the class.

This reduces the possibility of incorrect data.
"""


class Inventory:

    def __init__(self,quantity):
        if(quantity<0):
            raise ValueError(
                "Quantity cannot be negative."
            )

        self._quantity=quantity

    @property
    def quantity(self):
        return self._quantity

    def add_stock(self,amount):
        if(amount<=0):
            raise ValueError(
                "Stock amount must be positive."
            )

        self._quantity+=amount

    def remove_stock(self,amount):
        if(amount<=0):
            raise ValueError(
                "Removal amount must be positive."
            )

        if(amount>self._quantity):
            raise ValueError(
                "Not enough stock."
            )

        self._quantity-=amount


inventory_record=Inventory(50)

inventory_record.add_stock(20)
inventory_record.remove_stock(15)

print("Available Stock:",inventory_record.quantity)


# ============================================================
# 18. BENEFIT: CONTROLLED ACCESS
# ============================================================

"""
The second major benefit is controlled access.

Instead of allowing outside code to directly change internal
data, the class provides specific operations.

For example:

    deposit()
    withdraw()

Each operation can have its own rules.
"""


class TicketCounter:

    def __init__(self,available_tickets):
        self._available_tickets=available_tickets

    @property
    def available_tickets(self):
        return self._available_tickets

    def purchase(self,quantity):
        if(quantity<=0):
            print("Quantity must be positive.")
            return

        if(quantity>self._available_tickets):
            print("Not enough tickets available.")
            return

        self._available_tickets-=quantity
        print("Purchase successful.")


ticket_counter=TicketCounter(100)

ticket_counter.purchase(5)

print(
    "Tickets Remaining:",
    ticket_counter.available_tickets
)


# ============================================================
# 19. BENEFIT: EASIER MAINTENANCE
# ============================================================

"""
The third major benefit is easier maintenance.

Suppose the rules for withdrawing money change.

Without encapsulation, many parts of the program might directly
change the balance.

With encapsulation, the withdrawal logic is located inside
withdraw().

We can update the logic in one place.
"""


class ModernBankAccount:

    def __init__(self,balance):
        self._balance=balance

    @property
    def balance(self):
        return self._balance

    def withdraw(self,amount):
        if(amount<=0):
            raise ValueError("Amount must be positive.")

        if(amount>self._balance):
            raise ValueError("Insufficient balance.")

        # Additional withdrawal rules can be added here.

        self._balance-=amount


modern_account=ModernBankAccount(10000)

modern_account.withdraw(2000)

print("Balance:",modern_account.balance)


# ============================================================
# 20. ENCAPSULATION AND MAINTAINABILITY
# ============================================================

"""
Imagine that later we want to add a withdrawal fee.

Because withdrawal is controlled by one method, we can update
the logic there.

For example:

    withdrawal_fee=50

The rest of the program does not need to know how the
calculation is performed.

This is one reason encapsulation makes programs easier to
maintain.
"""


class FeeBasedAccount:

    def __init__(self,balance):
        self._balance=balance

    @property
    def balance(self):
        return self._balance

    def withdraw(self,amount):
        withdrawal_fee=50
        total_amount=amount+withdrawal_fee

        if(total_amount>self._balance):
            raise ValueError(
                "Insufficient balance."
            )

        self._balance-=total_amount


fee_account=FeeBasedAccount(10000)

fee_account.withdraw(2000)

print("Remaining Balance:",fee_account.balance)


# ============================================================
# 21. ENCAPSULATION IS NOT JUST "HIDING DATA"
# ============================================================

"""
Encapsulation is sometimes described simply as "data hiding".

Data hiding is an important part of encapsulation, but
encapsulation is broader.

Encapsulation means:

- Keeping related data and methods together.
- Controlling how internal data is accessed.
- Protecting the object's internal state.
- Providing a clear interface for using the object.

Therefore, encapsulation is about designing the class and
controlling how the outside world interacts with it.
"""


# ============================================================
# 22. ENCAPSULATION VS DIRECT ACCESS
# ============================================================

"""
Without encapsulation:

    account.balance=-5000

The outside code directly changes the internal state.

With encapsulation:

    account.deposit(500)
    account.withdraw(200)

The class controls how the state changes.

This gives the class more responsibility for maintaining
valid data.
"""


# ============================================================
# 23. COMPLETE BANK ACCOUNT EXAMPLE
# ============================================================

"""
Let's create a complete BankAccount class.

Requirements:

1. The owner should be publicly readable.
2. The balance should be protected from direct modification.
3. The balance should be readable through a property.
4. Deposits must be positive.
5. Withdrawals must be positive.
6. A withdrawal cannot exceed the current balance.
7. The balance should only change through controlled methods.

This is a practical example of encapsulation.
"""


class BankAccount:

    def __init__(self,owner,initial_balance):
        if(initial_balance<0):
            raise ValueError(
                "Initial balance cannot be negative."
            )

        self.owner=owner
        self._balance=initial_balance

    @property
    def balance(self):
        return self._balance

    def deposit(self,amount):
        if(amount<=0):
            raise ValueError(
                "Deposit amount must be greater than zero."
            )

        self._balance+=amount

        print(
            f"{amount} deposited successfully."
        )

    def withdraw(self,amount):
        if(amount<=0):
            raise ValueError(
                "Withdrawal amount must be greater than zero."
            )

        if(amount>self._balance):
            raise ValueError(
                "Insufficient balance."
            )

        self._balance-=amount

        print(
            f"{amount} withdrawn successfully."
        )

    def show_account(self):
        print("Owner:", self.owner)
        print("Balance:", self.balance)


bank_customer=BankAccount(
    "Noor",
    15000
)

bank_customer.show_account()

bank_customer.deposit(5000)

bank_customer.show_account()

bank_customer.withdraw(3000)

bank_customer.show_account()


# ============================================================
# 24. WHAT THE OUTSIDE CODE CAN AND CANNOT DO
# ============================================================

"""
With our BankAccount class, outside code can do:

    bank_customer.owner

    bank_customer.balance

    bank_customer.deposit(5000)

    bank_customer.withdraw(3000)

But the outside code should not directly manipulate:

    bank_customer._balance

The class provides controlled operations instead.

This is the basic idea behind encapsulation.
"""


# ============================================================
# 25. ENCAPSULATION WITH A PRIVATE ATTRIBUTE
# ============================================================

"""
We can also use a private-style attribute for the balance.

This makes the intention even stronger:

    self.__balance

The outside code should interact with the balance through
public methods and properties.
"""


class PrivateBankAccount:

    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self,amount):
        if(amount<=0):
            raise ValueError(
                "Deposit must be positive."
            )

        self.__balance+=amount

    def withdraw(self,amount):
        if(amount<=0):
            raise ValueError(
                "Withdrawal must be positive."
            )

        if(amount>self.__balance):
            raise ValueError(
                "Insufficient balance."
            )

        self.__balance-=amount


private_bank_account=PrivateBankAccount(
    "Bilal",
    12000
)

print("Owner:",private_bank_account.owner)
print("Balance:",private_bank_account.balance)

private_bank_account.deposit(3000)

print(
    "Updated Balance:",
    private_bank_account.balance
)


# ============================================================
# 26. A SIMPLE WAY TO REMEMBER ENCAPSULATION
# ============================================================

"""
Think of a BankAccount like a real bank.

You do not walk into a bank and directly change the bank's
internal database.

Instead, you request an operation:

    Deposit money.
    Withdraw money.

The bank checks the request and then updates its records.

Similarly, an encapsulated class controls how its internal
data is changed.

The object exposes a controlled interface instead of allowing
unrestricted modification of its internal state.
"""


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. Encapsulation is an important concept of Object-Oriented
   Programming.

2. Encapsulation means bundling related data and methods
   together inside a class.

3. It also means controlling how the internal state of an
   object is accessed and modified.

4. Encapsulation helps protect an object's internal state.

5. A class can use methods to control changes to its data.

6. Properties can be used to control how attributes are
   read and changed.

7. A single underscore can indicate that an attribute is
   intended for internal use:

       self._balance

8. A double underscore can provide name mangling:

       self.__balance

9. Python does not provide absolute private access like
   some languages such as Java and C++.

10. A read-only property can expose internal data without
    allowing direct modification.

11. A BankAccount is a good example of encapsulation:

       owner
       _balance

    with controlled methods:

       deposit()
       withdraw()

12. The class can validate operations before changing its
    internal state.

13. Main benefits of encapsulation include:

    - Data protection
    - Controlled access
    - Reduced invalid data
    - Easier maintenance
    - Clearer class design
    - Hiding implementation details

A simple way to remember:

    Encapsulation=Data+Methods+Controlled Access

Instead of allowing outside code to freely manipulate
important data, the class provides a controlled interface
for working with that data.

In the next chapters, we will learn about inheritance,
which allows one class to reuse and extend the behavior
of another class.
"""