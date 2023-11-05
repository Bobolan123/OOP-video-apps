from user03 import User

class Staff(User):
    def __init__(self, name, user_id, job):
        super().__init__(name, user_id)
        self.job = job
        self.modules = []
        self.group = "staffs"