from ceilinglight03 import CeilingLight
from floorlamp03 import FloorLamp
from heater03 import Heater
from musicplayer03 import MusicPlayer
from spotlight03 import SpotLight
from tablelamp03 import TableLamp


def chosen(device, command):
    if device.name in command or device.name.replace(" ", "") in command:
        return True
    else:
        return False


ceiling_light = CeilingLight()
floor_lamp = FloorLamp()
table_lamp = TableLamp()
spot_light = SpotLight()
music_player = MusicPlayer()
heating = Heater()
oven = Heater("oven" ,150, 300, 10)

devices = [ceiling_light, floor_lamp, table_lamp, spot_light, music_player, heating, oven]

name = input("What is your name? ")
print(f"Hello {name}")

while True:
    print()
    command = input(f"What next, {name}? ")
    command = f" {command.lower()} "

    if "system off" in command:
        break

    device_chosen = None
    for device in devices:
        if chosen(device, command):
            device_chosen = device
            break

    if device_chosen is None:
        print(f"Sorry {name}, I do not understand that")
    else:
        if " on " in command:
            device_chosen.switch_on()
        elif " off " in command:
            device_chosen.switch_off()
        elif " up " in command and hasattr(device_chosen, "up"):
            device_chosen.up()
        elif " down " in command and hasattr(device_chosen, "down"):
            device_chosen.down()
        elif " play " in command and hasattr(device_chosen, "play"):
            device_chosen.play()
        elif " pause " in command and hasattr(device_chosen, "pause"):
            device_chosen.pause()
        else:
            print(f"Sorry {name}, I do not understand that")

for device in devices:
    device.switch_off()

print(f"Bye bye, {name}")
