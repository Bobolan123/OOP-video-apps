from lights08 import Light

class ColouredLight(Light):
    def __init__(self, name, colour):
        super().__init__(name)
        self.colour = colour

cl = ColouredLight("Light", "red")

cl.status()
cl.switch_on()
if cl.on:
    print("and is coloured", cl.colour)