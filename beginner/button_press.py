from gpiozero import LED, Button
from signal import pause

import time

button = Button(2)
led  = LED(17)

def pressed():
	led.on()
	print("ON!")

def released():
	led.off()
	print("OFF!")

button.when_pressed = pressed
button.when_released = released
pause()
