from heating08 import Heating
from lights08 import DimmableLight
from lights08 import Light
from musicplayer08 import MusicPlayer


def check_on_off(capsys, device, name, type=None, setting=0, detail=""):
    assert capsys.readouterr().out == f"{name} has been initialised\n"

    device.switch_on()
    expected_output = f"{name} is on{detail}\n"
    if type is not None:
        expected_output += f" {name} {type} is set to {setting}\n"
    assert capsys.readouterr().out == expected_output

    device.switch_off()
    expected_output = f"{name} is off\n"
    assert capsys.readouterr().out == expected_output

    with capsys.disabled():
        print()
        print(f"tested {name} on/off successfully")


def check_up_down(capsys, device, name, type, setting, increment):
    assert capsys.readouterr().out == f"{name} has been initialised\n"

    device.up()
    setting += increment
    expected_output = f" {name} {type} is set to {setting}\n"
    assert capsys.readouterr().out == expected_output

    device.down()
    setting -= increment
    expected_output = f" {name} {type} is set to {setting}\n"
    assert capsys.readouterr().out == expected_output

    with capsys.disabled():
        print()
        print(f"tested {name} up/down successfully")


def test_devices(capsys):
    check_on_off(capsys, Light("ceiling light"), "ceiling light")
    check_on_off(capsys, Light("floor lamp"), "floor lamp")
    check_on_off(capsys, Light("table lamp"), "table lamp")
    check_on_off(capsys, DimmableLight("spot light", 350), "spot light", type="brightness", setting=350)
    check_on_off(capsys, Heating(), "heating", type="temperature", setting=18)
    check_on_off(capsys, MusicPlayer(), "music player", type="volume", setting=7, detail=" (paused)")

    check_up_down(capsys, DimmableLight("spot light", 350), "spot light", "brightness", 350, 10)
    check_up_down(capsys, Heating(), "heating", "temperature", 18, 1)
    check_up_down(capsys, MusicPlayer(), "music player", "volume", 7, 1)
