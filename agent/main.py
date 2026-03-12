import time
import threading
from gpiozero import LED, Button

button = Button(2)
red = LED(17)
green = LED(27)
blue = LED(22)
yellow = LED(24)
white = LED(23)

is_running = False

def cycle_colors():
	leds = [
		(red, "RED"),
		(green, "GREEN"),
		(blue, "BLUE"),
		(yellow, "YELLOW"),
		(white, "WHITE"),
	]

	while is_running:
		for led, name in leds:
			if not is_running:
				break

			led.on()
			print(f"{name} ON")
			time.sleep(1)
			led.off()
			print(f"{name} OFF")

def pressed():
	global is_running
	
	if not is_running:
		is_running = True
		print("===========Cycle Started!!!===================")
		threading.Thread(target=cycle_colors).start()
	else:
		is_running = False
		released()

def released():
	red.off()
	green.off()
	white.off()
	yellow.off()
	blue.off()
	print("===============Stopped====================")

button.when_pressed = pressed


from signal import pause
pause()

'''
  if __name__ == "__main__":
	try:
		cycle_colors()
	except KeyboardInterrupt:
		red.off()
		green.off()
		white.off()
		yellow.off()
		blue.off()
		print("Stopped.")
'''
