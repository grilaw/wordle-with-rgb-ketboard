from openrgb import OpenRGBClient
from openrgb.utils import DeviceType
from openrgb.utils import RGBColor



cli = OpenRGBClient()
keyboard = cli.get_devices_by_type(DeviceType.KEYBOARD)[0]
#print(mobo)

#print("Светодиоды на клавиатуре:")
#for i, led in enumerate(mobo.leds):
#    print(f"{i}: {led.name}")

def set_keyboard_color(letter, state):
    color_map = {
        "green": RGBColor(0, 255, 0),
        "yellow": RGBColor(255, 255, 0),
        "red": RGBColor(255, 0, 0)
    }

    color = color_map.get(state, RGBColor(255, 255, 255))
    key_led = None
    letter = str("KEY: " + letter.upper())
    for led in keyboard.leds:
        if led.name.upper() == letter:
            key_led = led
        # Меняем цвет на нужный
            key_led.set_color(color)
            break

#set_keyboard_color("D", yellow)