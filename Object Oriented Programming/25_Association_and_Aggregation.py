"""
ASSOCIATION AND AGGREGATION
"""


# ============================================================
# 1. INTRODUCTION
# ============================================================

"""
In the previous chapter, we learned about Composition.

Composition represents a strong "has-a" relationship where one
object contains another object and usually controls its
lifecycle.

For example:

    Car has an Engine.

In this chapter, we will learn about two other relationships
between objects:

    1. Association
    2. Aggregation

These relationships help us describe how objects interact with
each other.

The main idea is:

    Association  → uses-a relationship

    Aggregation  → has-a relationship with weak ownership

    Composition  → has-a relationship with strong ownership
"""


# ============================================================
# 2. WHAT IS ASSOCIATION?
# ============================================================

"""
Association is a general relationship between two independent
objects.

One object uses, communicates with, or works with another
object.

The important point is:

    Both objects can exist independently.

For example:

    Teacher works at a School.

A Teacher can exist without a particular School object.

A School can also exist without a particular Teacher object.

Therefore, the relationship between them can be represented
as an association.
"""


# ============================================================
# 3. SIMPLE ASSOCIATION EXAMPLE
# ============================================================

class Teacher:

    def __init__(self,name):
        self.name=name

    def teach(self):
        print(f"{self.name} is teaching.")


class School:

    def __init__(self,name):
        self.name=name

    def conduct_class(self,teacher):
        print(f"{self.name} is conducting a class.")
        teacher.teach()


teacher_object=Teacher("Ayesha")
school_object=School("City School")

school_object.conduct_class(teacher_object)


"""
Here, School uses a Teacher object.

The School does not create the Teacher.

The Teacher does not depend on the School for its existence.

Both objects were created independently:

    teacher_object=Teacher(...)
    school_object=School(...)

The School simply uses the Teacher.

This is association.
"""


# ============================================================
# 4. UNDERSTANDING "USES-A"
# ============================================================

"""
Association is sometimes described as a "uses-a" relationship.

For example:

    School uses a Teacher.
    Customer uses a Bank.
    Doctor uses a Hospital.
    Driver uses a Car.

The objects can generally exist independently.

The relationship mainly tells us that the objects interact with
each other.
"""


# ============================================================
# 5. ASSOCIATION DOES NOT REQUIRE OWNERSHIP
# ============================================================

"""
In association, one object does not necessarily own the other.

For example:

    A School can work with a Teacher.

The School does not necessarily create or destroy the Teacher.

The Teacher can exist independently.

This is different from strong composition, where one object
typically owns and manages the other object's lifecycle.
"""


# ============================================================
# 6. ANOTHER ASSOCIATION EXAMPLE
# ============================================================

class Doctor:

    def __init__(self,name):
        self.name=name

    def examine_patient(self):
        print(f"Dr. {self.name} is examining the patient.")


class Patient:

    def __init__(self,name):
        self.name=name

    def visit_doctor(self,doctor):
        print(f"{self.name} is visiting the doctor.")
        doctor.examine_patient()


doctor_object=Doctor("Hassan")
patient_object=Patient("Bilal")

patient_object.visit_doctor(doctor_object)


"""
The Doctor and Patient are independent objects.

The Patient uses the Doctor.

Neither object needs to own the other.

This is association.
"""


# ============================================================
# 7. ASSOCIATION CAN BE ONE-WAY
# ============================================================

"""
An association does not have to be stored in both objects.

For example:

    Student → Teacher

A Student may have a reference to a Teacher.

The Teacher does not necessarily need a reference back to the
Student.
"""


class Instructor:

    def __init__(self,name):
        self.name=name

    def explain(self):
        print(f"{self.name} is explaining the topic.")


class Student:

    def __init__(self,name,instructor):
        self.name=name
        self.instructor=instructor

    def learn(self):
        print(f"{self.name} is learning.")
        self.instructor.explain()


instructor_object=Instructor("Mr.Ahmed")

student_object=Student(
    "Sara",
    instructor_object
)

student_object.learn()


"""
Here:

    Student uses Instructor.

The Student stores a reference to the Instructor.

The Instructor does not store a reference to the Student.

This is still an association.
"""


# ============================================================
# 8. ASSOCIATION CAN ALSO BE BIDIRECTIONAL
# ============================================================

"""
Objects can also have references to each other.

For example:

    Teacher ↔ Student

A Teacher can know about a Student.

A Student can know about a Teacher.

This is called a bidirectional association.
"""


class Mentor:

    def __init__(self,name):
        self.name=name
        self.student=None

    def guide(self):
        print(f"{self.name} is guiding the student.")


class Learner:

    def __init__(self,name):
        self.name=name
        self.mentor=None

    def study(self):
        print(f"{self.name} is studying.")


mentor_object=Mentor("Mr. Usman")
learner_object=Learner("Zain")

mentor_object.student=learner_object
learner_object.mentor=mentor_object

mentor_object.guide()
learner_object.study()


"""
Both objects now know about each other.

They are still independent objects.

This is a bidirectional association.
"""


# ============================================================
# 9. WHAT IS AGGREGATION?
# ============================================================

"""
Aggregation is a special type of "has-a" relationship.

In aggregation:

    One object contains or groups other objects,

but:

    The contained objects can exist independently.

This is sometimes described as:

    weak ownership

For example:

    Department has Professors.

A Department can contain several Professor objects.

But a Professor does not necessarily stop existing just
because the Department object is removed.

The Professor can be transferred to another department or
continue to exist independently.

Therefore, this relationship can be represented as
aggregation.
"""


# ============================================================
# 10. SIMPLE AGGREGATION EXAMPLE
# ============================================================

class Professor:

    def __init__(self,name):
        self.name=name

    def teach(self):
        print(f"Professor {self.name} is teaching.")


class Department:

    def __init__(self,name,professors):
        self.name=name
        self.professors=professors

    def show_professors(self):
        print(f"Department: {self.name}")

        for professor in self.professors:
            print(professor.name)


professor_one=Professor("Ali")
professor_two=Professor("Maria")

computer_department=Department(
    "Computer Science",
    [professor_one,professor_two]
)

computer_department.show_professors()


"""
Notice how the Professor objects were created separately:

    professor_one=Professor(...)
    professor_two=Professor(...)

Then they were passed to the Department:

    Department(..., [professor_one, professor_two])

The Department did not create the Professors.

The Professors can exist independently.

This is aggregation.
"""


# ============================================================
# 11. WHY IS THIS DIFFERENT FROM COMPOSITION?
# ============================================================

"""
The important difference is ownership and lifecycle.

Composition:

    Strong ownership

    The contained object is strongly associated with the
    container's lifecycle.

Aggregation:

    Weak ownership

    The contained object can exist independently of the
    container.

For example:

    Composition:
        House has Rooms.

    Aggregation:
        Department has Professors.

The exact modeling depends on the application's requirements,
but the lifecycle dependency is the key idea.
"""


# ============================================================
# 12. AGGREGATION DOES NOT MEAN COPYING OBJECTS
# ============================================================

"""
When we pass objects into an aggregation relationship, the
container normally stores references to those existing objects.

For example:
"""


class Employee:

    def __init__(self,name):
        self.name=name


class Team:

    def __init__(self,employees):
        self.employees=employees


employee_one=Employee("Hamza")
employee_two=Employee("Nida")

development_team=Team(
    [employee_one,employee_two]
)

print(development_team.employees[0].name)
print(development_team.employees[1].name)


"""
The Team stores references to existing Employee objects.

The employees were created outside the Team.

This is a common way to implement aggregation in Python.
"""


# ============================================================
# 13. INDEPENDENT LIFECYCLE
# ============================================================

"""
One of the most important ideas in aggregation is:

    The contained objects have an independent lifecycle.

For example:
"""


class Researcher:

    def __init__(self,name):
        self.name=name

    def work(self):
        print(f"{self.name} is doing research.")


class ResearchGroup:

    def __init__(self,researchers):
        self.researchers=researchers


researcher_one=Researcher("Omar")
researcher_two=Researcher("Noor")

research_team=ResearchGroup(
    [researcher_one,researcher_two]
)

researcher_one.work()
researcher_two.work()


"""
Even if the ResearchGroup object is no longer used, the
Researcher objects were created independently.

They are not inherently dependent on the ResearchGroup for
their existence.

This demonstrates the idea of aggregation.
"""


# ============================================================
# 14. REASSIGNING AN AGGREGATED OBJECT
# ============================================================

"""
Because the objects are independent, a Professor can be moved
from one Department to another.
"""


class Professor:

    def __init__(self,name):
        self.name=name


class Department:

    def __init__(self,name,professors=None):
        self.name=name
        self.professors=professors or []

    def add_professor(self,professor):
        self.professors.append(professor)

    def remove_professor(self,professor):
        self.professors.remove(professor)


professor_object=Professor("Farhan")

science_department=Department("Science")
business_department=Department("Business")

science_department.add_professor(professor_object)

print(science_department.professors[0].name)

science_department.remove_professor(professor_object)

business_department.add_professor(professor_object)

print(business_department.professors[0].name)


"""
The same Professor object can now belong to another Department.

The Professor itself was not destroyed when it was removed from
the first Department.

This is a good illustration of weak ownership.
"""


# ============================================================
# 15. COMPOSITION EXAMPLE FOR COMPARISON
# ============================================================

"""
Let's compare this with composition.

Suppose a Computer creates its own internal Processor.
"""


class Processor:

    def process(self):
        print("Processor is processing.")


class Computer:

    def __init__(self):
        self.processor=Processor()

    def run(self):
        self.processor.process()


my_computer=Computer()

my_computer.run()


"""
Here the Computer creates its Processor internally:

    self.processor = Processor()

The Processor is treated as an internal component of the
Computer.

This is a stronger ownership relationship and is commonly used
as an example of composition.
"""


# ============================================================
# 16. AGGREGATION VS COMPOSITION
# ============================================================

"""
Let's compare the two relationships.

Aggregation:

    Department has Professors.

The Professors:

    Can exist independently.
    Can move to another Department.
    Are created outside the Department.

Composition:

    Computer has an internal Processor.

The Processor:

    Is treated as a component of the Computer.
    Is created by the Computer in this example.
    Has a stronger lifecycle dependency.
"""


# ============================================================
# 17. SIDE-BY-SIDE EXAMPLE
# ============================================================

class Battery:

    def charge(self):
        print("Battery charging.")


class Smartphone:

    def __init__(self):
        self.battery=Battery()


"""
The Smartphone creates its Battery.

This is a strong ownership pattern:

    Smartphone
        |
        └── Battery

This is composition.
"""


class Player:

    def __init__(self,name):
        self.name=name


class FootballTeam:

    def __init__(self,players):
        self.players=players


player_one=Player("Rayan")
player_two=Player("Adeel")

football_team=FootballTeam(
    [player_one,player_two]
)


"""
The Player objects were created independently and then grouped
inside the FootballTeam.

This is aggregation:

    FootballTeam
        |
        ├── Player
        └── Player

The players can exist independently of this particular team.
"""


# ============================================================
# 18. ASSOCIATION VS AGGREGATION
# ============================================================

"""
Association and aggregation are related concepts, but they are
not exactly the same.

Association:

    General relationship between independent objects.

    Example:
        Teacher works with School.

Aggregation:

    A more specific "has-a" relationship where one object
    groups or contains other independent objects.

    Example:
        Department has Professors.

Therefore:

    Association → general interaction

    Aggregation → grouping/has-a relationship with weak
                  ownership
"""


# ============================================================
# 19. ASSOCIATION EXAMPLE: TEACHER AND SCHOOL
# ============================================================

"""
Let's build the requested Teacher and School example.
"""


class Teacher:

    def __init__(self,name):
        self.name=name

    def teach_subject(self,subject):
        print(f"{self.name} is teaching {subject}.")


class School:

    def __init__(self,name):
        self.name=name

    def arrange_class(self,teacher,subject):
        print(f"{self.name} arranged a class.")
        teacher.teach_subject(subject)


school_teacher=Teacher("Ms. Hina")

local_school=School("Green Valley School")

local_school.arrange_class(
    school_teacher,
    "Python Programming"
)


"""
The Teacher and School are independent objects.

Teacher was created independently.

School was created independently.

The School simply uses the Teacher.

Therefore:

    School uses Teacher.

This is association.
"""


# ============================================================
# 20. AGGREGATION EXAMPLE: DEPARTMENT AND PROFESSORS
# ============================================================

"""
Now let's build the requested Department and Professors
example.
"""


class Professor:

    def __init__(self,name,subject):
        self.name=name
        self.subject=subject

    def display_info(self):
        print(
            f"Professor: {self.name}, "
            f"Subject: {self.subject}"
        )


class Department:

    def __init__(self,name,professors):
        self.name=name
        self.professors=professors

    def display_department(self):
        print(f"Department: {self.name}")

        for professor in self.professors:
            professor.display_info()


physics_professor=Professor(
    "Dr. Imran",
    "Physics"
)

math_professor = Professor(
    "Dr. Sana",
    "Mathematics"
)

science_department=Department(
    "Science",
    [
        physics_professor,
        math_professor
    ]
)

science_department.display_department()


"""
The Professors were created before the Department.

The Department simply groups them.

The Professor objects can continue to exist independently.

Therefore:

    Department has Professors.

This is aggregation.
"""


# ============================================================
# 21. MOVING PROFESSORS BETWEEN DEPARTMENTS
# ============================================================

"""
The independent lifecycle becomes clearer when we move a
Professor from one Department to another.
"""


class Professor:

    def __init__(self,name):
        self.name=name


class Department:

    def __init__(self,name):
        self.name=name
        self.professors=[]

    def add_professor(self,professor):
        self.professors.append(professor)

    def show_professors(self):
        print(f"{self.name} Department:")

        for professor in self.professors:
            print(f"-{professor.name}")


professor_object=Professor("Dr. Kamran")

engineering_department=Department("Engineering")
science_department=Department("Science")

engineering_department.add_professor(professor_object)

engineering_department.show_professors()

engineering_department.professors.remove(professor_object)

science_department.add_professor(professor_object)

science_department.show_professors()


"""
The Professor object still exists.

Only its relationship with the Department changed.

This is possible because the Professor is independent of the
Department.
"""


# ============================================================
# 22. ASSOCIATION DOES NOT ALWAYS MEAN A CLASS ATTRIBUTE
# ============================================================

"""
An association can exist simply because one object receives
another object as an argument.

For example:
"""


class Customer:

    def __init__(self,name):
        self.name=name


class Cashier:

    def process_customer(self,customer):
        print(
            f"Cashier is processing {customer.name}."
        )


customer_object=Customer("Ahmed")
cashier_object=Cashier()

cashier_object.process_customer(customer_object)


"""
Cashier uses Customer during a method call.

The Cashier does not need to permanently store the Customer.

This is still an association.
"""


# ============================================================
# 23. ASSOCIATION CAN BE TEMPORARY
# ============================================================

"""
An association can be temporary.

For example:

    A Customer visits a Cashier.

The Cashier interacts with the Customer during a transaction.

After the transaction, the relationship may end.

Both objects can continue to exist independently.
"""


# ============================================================
# 24. AGGREGATION IS A STRONGER RELATIONSHIP THAN
#     GENERAL ASSOCIATION
# ============================================================

"""
A useful way to think about the relationships is:

    Association
        ↓
    General relationship
        ↓
    "uses-a"

    Aggregation
        ↓
    More specific relationship
        ↓
    "has-a" with weak ownership

    Composition
        ↓
    Stronger "has-a"
        ↓
    Strong ownership / lifecycle dependency

The boundaries between association, aggregation, and composition
can sometimes depend on how a particular system is modeled.

The important concept is the difference in ownership and
lifecycle.
"""


# ============================================================
# 25. REAL-WORLD COMPARISON
# ============================================================

"""
Consider a University.

Association:

    Student uses Professor.

The Student and Professor are independent.

Aggregation:

    Department has Professors.

The Professors can exist independently and may move to another
Department.

Composition:

    University has an internal component that is created and
    managed as part of the University object.

The important difference is how strongly the objects depend on
each other's lifecycle.
"""


# ============================================================
# 26. OWNERSHIP AND LIFECYCLE
# ============================================================

"""
Ownership answers the question:

    "Who is responsible for the contained object?"

Lifecycle answers the question:

    "Can the contained object exist independently?"

For aggregation:

    The contained objects can exist independently.

For composition:

    The contained objects are strongly associated with the
    owner and often share its lifecycle.

For association:

    There may be no ownership at all.
"""


# ============================================================
# 27. SIMPLE VISUAL REPRESENTATION
# ============================================================

"""
Association:

    Teacher ───────── School

    Teacher and School are independent.

    Relationship:
        uses / interacts with


Aggregation:

    Department ◇──── Professor
                 └── Professor

    Professors can exist independently.

    Relationship:
        has / groups


Composition:

    Car ◆──── Engine

    Engine is treated as a strongly owned component.

    Relationship:
        has / owns
"""


# ============================================================
# 28. PYTHON DOES NOT HAVE SPECIAL SYNTAX FOR THESE
#     RELATIONSHIPS
# ============================================================

"""
Python does not have separate keywords such as:

    association
    aggregation
    composition

These are object-oriented design concepts.

We normally implement them using:

    object references
    class attributes
    constructor parameters
    method parameters
    lists of objects

For example:

    self.engine=engine

or:

    self.professors=professors

The meaning comes from how the objects are related and managed.
"""


# ============================================================
# 29. LISTS OF OBJECTS AND AGGREGATION
# ============================================================

"""
Aggregation commonly involves a collection of objects.

For example:

    Department → Professors

A Department can store several Professor objects in a list.
"""


class Worker:

    def __init__(self, name):
        self.name = name


class CompanyTeam:

    def __init__(self,workers):
        self.workers=workers


worker_one=Worker("Usman")
worker_two=Worker("Fatima")
worker_three=Worker("Danish")

development_team=CompanyTeam(
    [
        worker_one,
        worker_two,
        worker_three
    ]
)

for worker in development_team.workers:
    print(worker.name)


"""
The CompanyTeam groups several independently created Worker
objects.

This is a common aggregation pattern.
"""


# ============================================================
# 30. AGGREGATION DOES NOT NECESSARILY MEAN WEAK CODE
# ============================================================

"""
The word "weak" in weak ownership does not mean the relationship
is unimportant.

It means the lifecycle dependency is weaker.

For example:

    Department has Professors.

The Department may depend on its Professors to perform its work,
but the Professor objects themselves can exist independently.

So "weak ownership" refers specifically to lifecycle and
ownership, not importance.
"""


# ============================================================
# 31. CHOOSING BETWEEN THE THREE RELATIONSHIPS
# ============================================================

"""
A simple decision guide:

Ask:

1. Are the objects simply interacting?

       Yes
       → Association

2. Does one object group or contain other objects, but those
   objects can exist independently?

       Yes
       → Aggregation

3. Does one object strongly own the contained objects, with
   their lifecycle closely tied together?

       Yes
       → Composition

These are conceptual guidelines rather than strict Python
syntax rules.
"""


# ============================================================
# 32. COMMON BEGINNER CONFUSION
# ============================================================

"""
A common mistake is thinking:

    "If one object contains another object, it must be
     composition."

Not necessarily.

Consider:

    Department contains Professors.

The Professors were created independently and can exist outside
the Department.

Therefore this can be modeled as aggregation.

Compare:

    Car creates and owns its Engine.

This represents a stronger ownership relationship and can be
modeled as composition.
"""


# ============================================================
# 33. ANOTHER COMPARISON
# ============================================================

"""
Association:

    Doctor → Patient

The Doctor interacts with the Patient.

Neither owns the other.

Aggregation:

    Hospital → Doctors

The Hospital groups Doctors.

Doctors can exist independently and can work elsewhere.

Composition:

    House → Rooms

The Rooms are treated as parts of the House in the model and
their lifecycle is strongly connected to the House.

The exact modeling depends on the requirements of the
application.
"""


# ============================================================
# 34. IMPORTANT DESIGN IDEA
# ============================================================

"""
Association, aggregation, and composition are ways of thinking
about relationships between objects.

They help us answer questions such as:

    Who uses whom?

    Who contains whom?

    Who owns whom?

    Can the contained object exist independently?

    What happens to the contained object when the owner is
    removed?

These questions help us design better classes.
"""


# ============================================================
# SUMMARY
# ============================================================

"""
Important points:

1. Association is a general relationship between two objects.

2. Association often represents a "uses-a" relationship.

3. In association, the objects are generally independent.

4. One object can use another object without owning it.

5. For example:

       School uses a Teacher.

6. A Teacher can exist independently of a particular School.

7. A School can also exist independently of a particular
   Teacher.

8. Association can be one-way or bidirectional.

9. Association can also be temporary.

10. Aggregation is a more specific "has-a" relationship.

11. Aggregation represents weak ownership.

12. In aggregation, the contained objects can exist
    independently of the container.

13. For example:

       Department has Professors.

14. Professor objects can be created independently.

15. A Professor can move from one Department to another.

16. Therefore, the Professor's lifecycle is not dependent on
    one particular Department.

17. Composition is different from aggregation.

18. Composition represents stronger ownership.

19. In composition, the contained object is strongly associated
    with the owner's lifecycle.

20. A common composition example is:

       Car has an Engine.

21. A common aggregation example is:

       Department has Professors.

22. A common association example is:

       Teacher works with School.

23. The main difference between aggregation and composition is
    ownership and lifecycle dependency.

24. Association:
       General interaction
       → "uses-a"

25. Aggregation:
       Weak ownership
       → "has-a"

26. Composition:
       Strong ownership
       → "has-a"

27. Python does not have special keywords for association,
    aggregation, or composition.

28. These relationships are normally created using object
    references.

29. Constructor parameters can be used to pass existing
    objects into another object.

30. Lists can be used to store multiple related objects.

31. Aggregation commonly uses a collection of independently
    created objects.

32. Association does not necessarily require storing the other
    object as an attribute.

33. Aggregation and composition can look very similar in Python
    code.

34. The difference is primarily about the intended ownership
    and lifecycle relationship.

35. A useful way to remember them is:

       Association
           ↓
       "uses-a"

       Aggregation
           ↓
       "has-a" + weak ownership

       Composition
           ↓
       "has-a" + strong ownership

36. Always think about the real-world relationship before
    choosing how classes should interact.

37. Do not choose inheritance simply because one class needs to
    use another class.

38. Use object relationships that accurately describe the
    problem you are solving.

The main idea to remember is:

    Association → objects interact.

    Aggregation → objects are grouped, but can exist
                  independently.

    Composition → objects are strongly owned as parts of
                  another object.

In the next chapter, we will learn about Class and Method
Decorators and see how decorators can modify or extend the
behavior of classes and their methods.
"""