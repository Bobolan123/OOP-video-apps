from user03 import User

class Student(User):
    def __init__(self, name, user_id, programme):
        super().__init__(name, user_id)
        self.programme = programme
        self.modules = []
        self.group = "students"