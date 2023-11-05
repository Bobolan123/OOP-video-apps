class CeilingLight:
    def __init__(self):
        self.on = False
        self.name = "ceiling light"
        print(f"{self.name} has been initialised")

    def switch_on(self):
        self.on = True
        self.status()

    def switch_off(self):
        self.on = False
        self.status()

    def status(self):
        if self.on:
            print(self.name + " is on")
        else:
            print(self.name + " is off")
