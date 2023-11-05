class User:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        return

    def login(self, password):
        print("User can login")
        return

# Defind a child class of User, Student
class Student(User):
    def __init__(self, id, name, age):
        super().__init__(id,name,age)
        self.mark = None
        return
    def do_assignment(self):
        print("Student need to do assignment")
        return

class Lecture(User):
    def __init__(self, id, name, age, salary):
        super().__init__(id,name,age)
        self.salary = salary
        return

    def grade(self, student: object, grade):
        print("Mark")
        student.mark = grade
        return

    def give_lecture(self):
        print("Giving lecture")
        return

# Create a new instance in Student
std = Student(1, "Lan", 20)
std.login("bobolan")

ltr = Lecture(1,'ads',23, 213)

ltr.grade(std, 10)
print(std.mark)
