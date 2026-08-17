"""
In this file, you will learn how data and methods are defined
in a class. The purpose is to give you a basic understanding
of how data and methods are accessed from a class by an object.
We will study these concepts in more detail in the upcoming topics.
"""

class Student:
    student_name="Empty"  # You can provide any default value, I provide Empty
    student_age=0
    student_roll_number=0
    student_class="Empty"

student1=Student()
student1.student_name="Muhammad Ahmad"
student1.student_age=15
student1.student_roll_number=39
student1.student_class="9th Class"

print(f"Student Name: {student1.student_name}")
print(f"Student Age: {student1.student_age}")
print(f"Student Roll Number: {student1.student_roll_number}")
print(f"Student Class: {student1.student_class}")



class Car:
    car_name="Empty" 
    car_model=0
    car_color="Empty"
    def start_engine(self): # Method
        print("Engine is Started")

car1=Car()
car1.car_name="Civic"
car1.car_model=2026
car1.car_color="Black"

print(f"Car Name: {car1.car_name}")
print(f"Car Model: {car1.car_model}")
print(f"Car Color: {car1.car_color}")

car1.start_engine()

