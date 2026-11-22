class Student:
    def __init__(self, name: str, class_room: int, id: int):
        self.name = name
        self.class_room = class_room
        self.id = id
        
    def get_name(self):
        return f"The student name is {self.name}"
    
    def get_class(self):
        return f"The student classroom is {self.class_room}"
    
    def get_id(self):
        return f"The student ID is {self.id}"
    
    def get_student_details(self):
        return {
            "Name": self.name,
            "Class": self.class_room,
            "ID": self.id
        }


if __name__ == "__main__":
    test1 = Student("Paramesh",12,38)
    print(test1.name)
    print(test1.class_room)
    print(test1.id)
    print(test1.get_name())
    print(test1.get_student_details())