"""
Conditional Structures (Type of Control Structure):

A control Structure or a selection structure selects a statement or a 
set of statements to execute on the basis of conditions.

Types of Conditional Structures:-

1) if Statement:

if statement is a decision making statement. It is used to execute or skip a 
statement by checking a condition.

Syntax:

if(condition):
    statement1
    ::::::::::
    ::::::::::
    statementN
"""

# if Statement

temperature=35
if(temperature>30):
    print("It's hot outside")


"""
2) if-else Statement:

if-else statement is another type of conditional structure. It executes one block
of statement when the condition is true and the other when condition is false.
--> Both blocks of statements can be never be executed.
--> Both blocks of statements can be never be skipped.

Syntax:

(i) Simple if-else Statment:

if(condition):
    statement1
    ::::::::::
    ::::::::::
    statementN
else:
    statement1
    ::::::::::
    ::::::::::
    statementN

(ii) Short hand if-else Statement:

print("Statement inside if" if(condition) else "Statement inside else")
    
"""

# if-else Statement

# (i) Simple if-else Statement

number=10
if(number%2==0):
    print("Even Number")
else:
    print("Odd Number")

# (ii) Short hand if-else Statement

print("Even Number" if(number%2==0) else "Odd Number")

even_or_odd_num="Even Number" if(number%2)==0 else "Odd Number"
print(even_or_odd_num)


"""
3) Multiple if-else Statements:

if-else-if statement can be used to choose one block of statements from many 
blocks of statements.

Syntax:

(i) Simple if-else-if Statment:

if(condition):
    statement1
    ::::::::::
    ::::::::::
    statementN
elif(condition):
    statement1
    ::::::::::
    ::::::::::
    statementN
elif(condition):
    statement1
    ::::::::::
    ::::::::::
    statementN
::::::::::::::::
::::::::::::::::
else:
    statement1
    ::::::::::
    ::::::::::
    statementN

(ii) Short hand if-else-if Statement:

print("Statement inside if" if(condition) else "Statement inside elif" if(condition) else "Statment inside else")
    
"""

# if-else-if Statments

# (i) Simple if-else-if Statements

x=9
if(x>0):
    print("Positive Number")
elif(x<0):
    print("Negative Number")
else:
    print("Zero")

# (ii) Short hand if-else-if Statement

print("Positive Number" if(x>0) else "Negative Number" if(x<0) else "Zero")

positive_or_negative_or_zero="Positive Number" if(x>0) else "Negative Number" if(x<0) else "Zero"
print(positive_or_negative_or_zero)


"""
4) Nested if-else Statements:

A statement inside another statement is known as nested if-else statements.

Syntax:

if(condition):
    if(condition):
        statement1
        ::::::::::
        ::::::::::
        statementN
    elif(condition):
        statement1
        ::::::::::
        ::::::::::
        statementN
    else:
        statement1
        ::::::::::
        ::::::::::
        statementN
elif(condition):
    if(condition):
        statement1
        ::::::::::
        ::::::::::
        statementN
    elif(condition):
        statement1
        ::::::::::
        ::::::::::
        statementN
    else:
        statement1
        ::::::::::
        ::::::::::
        statementN
else:
    if(condition):
        statement1
        ::::::::::
        ::::::::::
        statementN
    elif(condition):
        statement1
        ::::::::::
        ::::::::::
        statementN
    else:
        statement1
        ::::::::::
        ::::::::::
        statementN   
"""

# Nested if-else statements

marks=75
if(marks>=40):
    if(marks>=80 and marks<=100):
        print("Pass: Grade A")
    elif(marks>=60 and marks<80):
        print("Pass: Grade B")
    else:
        print("Pass: Grade C")
else:
    print("Fail")


"""
5) match Statements:

The match statement in Python is used to compare a value against multiple possible patterns 
and execute the code associated with the matching pattern.

Syntax:

match expression:
    case 1:
        statement1
        ::::::::::
        ::::::::::
        statementN
    case 2:
        statement1
        ::::::::::
        ::::::::::
        statementN
    ::::::::::::::
    ::::::::::::::
    case N:
        statement1
        ::::::::::
        ::::::::::
        statementN 
    case _:
        statement1
        ::::::::::
        ::::::::::
        statementN 
"""

# match statment

day=2
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")

number1=10
number2=15
operator="*"
match operator:
    case "+":
        print(number1+number2)
    case "-":
        print(number1-number2)
    case "*":
        print(number1*number2)
    case "/":
        print(number1/number2)
    case _:
        print("Invalid Operation")

