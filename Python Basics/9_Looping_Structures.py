"""
Looping Structures (Type of Control Structure):

A type of control Structure that repeats a statement or set of staements
is known as looping structure. It is also known as repetitive or 
iterative structure.

Types of Looping Structures:-

1) Counter Controlled Loops:

A type of loop depends on the value of variable known as counter variable 
is called counter controlled loop.

Example:

for loop.

==> for loop:-

for loop executes one or more statements for given number of times. 

Syntax:

for counter_variable in range(initialization, termination):
    statement1
    ::::::::::
    ::::::::::
    statementN

=> increment/decrement:-

Increment means increasing the loop variable, usually by 1. 
Decrement means decreasing the loop variable, usually by 1.

Syntax:

for counter_variable in range(initialization, termination, increment/decrement):
    statement1
    ::::::::::
    ::::::::::
    statementN
"""

# for loop

for counter_variable1 in range(1,4):
    print(counter_variable1)

for counter_variable2 in range(1,5,2):
    print(counter_variable2)

# Table of a given number using for loop

n=int(input("Enter a number: "))
for counter_variable3 in range(1,11):
    print(n,"X",counter_variable3,"=",n*counter_variable3)


"""
2) Sentinal Controlled Loops:

A type of loop depends on the value of variable known as sentinal variable 
is called sentinal controlled loop.

Example:

while loop.

==> while loop:-

A while loop executes one or more statements while the given condition 
remains true.

Syntax:

sentinal_variable=sentinal_value
while(condition):
    statement1
    ::::::::::
    ::::::::::
    statementN
    sentinal_variable=sentinal_variable+1
"""

# while loop

sentinal_variable1=1
while(sentinal_variable1<4):
    print(sentinal_variable1)
    sentinal_variable1+=1

# Table of a given number using while loop

number=int(input("Enter a number: "))
sentinal_variable2=1
while(sentinal_variable2<=10):
    print(number,"X",sentinal_variable2,"=",number*sentinal_variable2)
    sentinal_variable2+=1

"""
(1) break statement:-

break statement is used to immediately stop a loop or exit a statement.

(2) continue statement:-

continue statement is used inside loops to skip the rest of the code in
the current iteration and jump directly to the next iteration of the loop.
"""

# break statement

for i in range(1,6):
    if(i==3):
        break # exits the loop when i=3
    else:
        print(i)


# continue statement

for i in range(1,6):
    if(i==3):
        continue # skip iteration when i=3
    else:
        print(i)

"""
In other programming languages like C++ we have another type of loop
called as do-while loop. In python we don't have a do-while loop but
we can achieve the same affect using while loop in python.

==> do-while loop:-

A do-while loop is a loop that executes its code at least once, and 
then checks the condition.
"""

# do-while loop using while loop

j=0
while(True):
    print(j)
    j+=1
    if(j>0):
        break

k=0
while True:
    print(k)
    k+=1
    if(k>=5):
        break


"""
Nestrd loops:-

A loop within a loop is called nested loop.
"""

# Nested loop

for x in range(1,3):
    print("Outer Loop")
    for y in range(1,6):
        print("Inner Loop")


"""
--> We can also use an else statement with for loop and while loop.
The else statement should be executed when for and while loops are 
completed.
"""

# for loop with else

for m in range(1,3):
    print("I am in for loop")
else:
    print("I am in else")

# while loop with else

n=1
while(n<=2):
    print("I am in while loop")
    n+=1
else:
    print("I am in else")
