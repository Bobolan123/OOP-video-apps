class MusicPlayer:
    def __init__(self):
        self.on = False
        self.playing = False
        self.name = "music player"
        self.type = "volume"
        self.setting = 7
        self.maximum = 11
        self.increment = 1
        print(f"{self.name} has been initialised")

    def switch_on(self):
        self.on = True
        self.status()

    def switch_off(self):
        if self.playing:
            self.pause()
        self.on = False
        self.status()

    def status(self):
        if self.on:
            if self.playing:
                print(self.name + " is playing")
            else:
                print(self.name + " is on (paused)")
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

    def play(self):
        if not self.on:
            self.switch_on()
        self.playing = True
        self.status()

    def pause(self):
        self.playing = False
        self.status()
