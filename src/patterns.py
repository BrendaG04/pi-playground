"""
	Advanced LED patterns and animation
"""

import time
import random
from typing import List
from src.led_controller import LEDController

#Collection of LED Pattern animations
class LEDPatterns:

	def __init_(self, controller: LEDController):
		self.controller = controller

	#Pulse Effect
	def pulse(self, led_name: str, duration: float = 2.0):
		led = self.controller.leds[led_name]
		steps = 20

		#fade in
		for i in range(steps):
			led.value = i / steps
			time.sleep(duration / ( 2 * steps))

		#fade out
		for i in range(steps, 0, -1):
			led.value = i / steps
			time.sleep(duration / ( 2 * steps))

		led.off()

	#Random Blinking
	def random_blink(self, led_names: List[str], duration: float = 5.0):
		start_time = time.time()

		while time.time() - start_time < duration:
			led_name = random.choice(led_names)
			self.controller.set_led(led_name, True)
			time.sleep(random.uniform(0.1, 0.5))
			self.controller.set_led(led_name, False)
			time.sleep(random.uniform(0.1, 0.3))

	##Chase pattern around LEDS
	def chase(self, led_names: List[str], rounds: int = 3):
		for _ in range (rounds):
			for i, name in enumerate(led_names):
				self.controller.set_led(name, True)
				if i>0:
					self.controller.set_led(led_names[i-1], False)
				time.sleep()
			self.controller.set_led(led_names[-1], False)


