class Light:
    def __init__(self, name):
        self.on = False
        self.name = name
        self.radio_button = None
        print(f"{self.name} has been initialised")

    def set_widget(self, radio_button):
        self.radio_button = radio_button

    def switch_on(self):
        self.on = True
        self.status()

    def switch_off(self):
        self.on = False
        self.status()

    def status(self):
        if self.radio_button is not None:
            self.radio_button.set(self.on)
        if self.on:
            print(self.name + " is on")

        else:
            print(self.name + " is off")


class DimmableLight(Light):
    def __init__(self, name, brightness):
        self.type = "brightness"  # lumens
        self.setting = brightness
        self.maximum = 500
        self.increment = 10
        self.slider = None
        super().__init__(name)

    def set_widgets(self, radio_button, slider):
        self.radio_button = radio_button
        self.slider = slider
        self.slider.set(self.setting)

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
        if self.slider is not None:
            self.slider.set(self.setting)
        self.print_setting()

    def print_setting(self):
        print(f" {self.name} {self.type} is set to {self.setting}")
