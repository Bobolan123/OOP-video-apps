from user10 import User

class Academic(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.modules = []
        return



    def attached_to(self, module):
        return module in self.modules

