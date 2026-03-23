"""
	Main file - will run LED Pattern on the real breadboard connected to the Raspberry Pi
"""

from led_controller import LEDController
from patterns import LEDPatterns
import time

pin_mapping = {
	'red': 17,
	'green': 27,
	'blue': 22,
	'yellow': 24,
	'white': 23
	}

controller = LEDController(pin_mapping)

print("All on....")
controller.all_on()
time.sleep(1)
