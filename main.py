def add_student():
    name = input("Please enter the Student's Name: ")
    std = int(input("Please enter the Student's Class: "))
    id = int(input("Please enter the Student ID: "))

print("Welcome to Student Login Database!")
print("1. Add Students,\n2. Enquire Student details\n")
print("Type 1 or 2 to move forward.")

while True:
    try:
        inp = int(input("Please enter the action number: "))
    except:
        print("\nPlease enter a valid number.\n")  
    else:     
        if inp == 1:
            add_student()
            break
        elif inp == 2:
            pass
            break
        else:
            print("\nPlease enter either 1 or 2.\n")