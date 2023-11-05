from person03 import Person

class User(Person):
    def __init__(self, name, user_id):
        super().__init__(name)
        self.user_id = user_id