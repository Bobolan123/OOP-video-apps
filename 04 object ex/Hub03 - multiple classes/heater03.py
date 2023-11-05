class Heater:
    def __init__(self, name = "heating", setting = 15, maximum = 30, increment = 1):
        self.on = False
        self.name = name
        self.type = "temperature"  # degrees C
        self.setting = setting
        self.maximum = maximum
        self.increment = increment
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
            self.print_setting()
        else:
            print(self.name + " is off")

    def up(self):
        self.change_setting(+self.increment)

    def down(self):
        self.change_setting(-self.increment)

    def change_setting(self, change):
        self.setting += change
        if self.setting > self.maximum:
            self.setting = self.maximum
        elif self.setting < 0:
            self.setting = 0
        self.print_setting()

    def print_setting(self):
        print(f" {self.name} {self.type} is set to {self.setting}")
