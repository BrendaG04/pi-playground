"""
	LED Controller with patterns and effects
"""

import time
from typing import List
from gpiozero import LED

#Manages Multiple LEDs w various patterns
class LEDController:

	#Initialize led controller
	def __init__(self, pi_mapping:dict):
		self.leds = {name: LED(pin) for name in pin_mapping.items()}

	#Turns off all LEDS
	def all_off(self):
		for led in self.leds.values:
			led.off()

	#Turns on all LEDS
	def all_on(self):
		for led in self.leds.values:
			led.on()

	#Setting specific LED state
	def set_led(self, name:str, state:bool):
		if name not in self.leds:
			raise ValueError(f"Unknown LED: {name}")

		if state:
			self.leds[name].on()
		else:
			self.leds[name].off()

	#Blink a specific led
	def blink(self, name:str, times: int = 3, delay: float = 0.5):
		if name not in self.leds:
			raise ValueError(f"Unknown LED: {name}")

		for _ in range(times):
			self.leds[name].toggle()
			time.sleep(delay)
			self.leds[name].toggle()
			time.sleep(delay)

	#Back and forth pattern
	def pattern_back_forth(self, led_names: List[str], iterations: int = 3):
		for _ in range(iterations):
			for name in led_names:
				self.leds[name].on()
				time.sleep(0.1)
				self.leds[name].off()

	#Displays the binary counter on LEDS
	def pattern_binary_counter(self, led_names: List[str], count_to: int = 16):
		for i in range(count_to):
			binary = format(i, f'0{len(led_names)}b')
			for led_name, bit in zip(led_names, binary):
				self.leds[led_name].value = int(bit)
			time.sleep(0.5)
		self.all_off()

	#Turns off all leds and cleanups
	def cleanup(self):
		self.all_off()
