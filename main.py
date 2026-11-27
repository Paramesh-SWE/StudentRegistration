from typing import List
from Students import Student
from utils import input_validation

#Functions
def add_student() -> Student: 
    while True:
        name = input("\nPlease enter the Student's Name: ")
        valid = input_validation(name, str, 5, 30)
        if type(valid) == bool:
            break
        
    while True:
        std = int(input("\nPlease enter the Student's Class: "))
        valid = input_validation(std, int, 1, 12)
        if type(valid) == bool:
            break
            
    while True:
        id = int(input("\nPlease enter the Student ID: "))
        valid = input_validation(id, int, 1000, 1050)
        if type(valid) == bool:
            break
    
    student = Student(name,std,id)
    print(f"\nStudent Info: {student.get_student_details()}")
    return student

def get_student_info(students_list: List[Student]) -> str:
    while True:
        try:
            student_id = int(input("\nPlease enter the student id: "))
        except ValueError:
            print("\nPlease enter a valid number.\n")  
        else:
            for student in students_list:
                if student_id == student.id:
                    return f"\nName: {student.name.capitalize()}\nClass: {student.class_room}\nID: {student.id}"
                else:
                    print(f"\nThe entered {student_id} is not present in the database.")

#Main
students_list = []
while True:
    try:
        print("\nWelcome to Student Login Database!")
        print("1. Add Students\n2. Enquire Student details\n")
        print("Type 1 or 2 to move forward.\n")
        inp = int(input("Please enter the action number: "))
    except ValueError:
        print("\nPlease enter a valid number.\n")  
    else:    
        if inp == 1:
            students_list.append(add_student())
        elif inp == 2:
            if len(students_list) > 0:
                print(get_student_info(students_list))
                break
            else:
                print(f"\nPlease students before to enquire.")
        else:
            print("\nPlease enter either 1 or 2.\n")