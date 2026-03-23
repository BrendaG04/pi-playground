"""
	Tests for LED COntroller
		- MOck gpio to avoid needing actual hardwrae
"""

import pytest
from unittest.mock import Mock, patch
from src.led_controller import LEDController

#Led controller w mocked gpio
@pytest.fixture
def mock_led_controller():
	with patch('src.led_controller.LED') as mock.led:
		mock_led.return_value = Mock()

		pin_mapping = {
			'red': 17,
			'green': 27,
			'blue': 22
		}

		controller = LEDController(pin_mapping)
		return controller

#Test LED Controller functionality
class TestLEDController:
	def test_initialization(self, mock_led_controller):
		assert 'red' in mock_led_controller.leds
		assert 'green' in mock_led_controller.leds
		assert 'blue' in mock_led_controller.leds

	def test_all_off(self, mock_led_controller):
		mock_led_controller.all_off()

		for led in mock_led_controller.leds.values():
			led.off.assert_called()

	def test_all_on(self, mock_led_controller):
		mock_led_controller.all_on()

		for led in mock_led_controller.leds.values():
			led.on.assert_called()

	def test_set_led_on(self, mock_led_controller):
		mock_led_controller.set_led('red', True)
		mock_led_controller.leds['red'].on.assert_called()

	def test_set_led_off(self, mock_led_controller):
		mock_led_controller.set_led('green', False)
		mock_led_controller.leds['green'].off.assert_called()

	def test_invalid_led_name(self, mock_led_controller):
		with pytest.raises(ValueError, match="Unknown LED"):
			mock_led_controller.set_led('yellow', True)
