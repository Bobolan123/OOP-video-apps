class Person:
    def __init__(self, name):
        self.name = name
        self.group = None

    def send_message(self, message):
        print(f" '{message}' sent to {self.name}")
