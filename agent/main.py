import time
from gpiozero import LED

red = LED(17)
green = LED(27)
blue = LED(22)
yellow = LED(24)
white = LED(23)

def cycle_colors():
	leds = [
		(red, "RED"),
		(green, "GREEN"),
		(blue, "BLUE"),
		(yellow, "YELLOW"),
		(white, "WHITE"),
	]

	while True:
		for led, name in leds:
			led.on()
			print(f"{name} ON")
			time.sleep(1)
			led.off()
			print(f"{name} OFF")

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

