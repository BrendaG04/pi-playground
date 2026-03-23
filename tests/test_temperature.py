"""
	Tests for temperature pattern
"""
import pytest
from agent.temperature import classify_temp
from src.temperature import (
	classify_temp,
	celsius_to_fahrenheit,
	read_cpu_temp_c,
	TemperatureError
)


#Test temp classification
class TestClassifyTtemp:

	def test_normal_temp(self):
		assert classify_temp(40.0) == "NORMAL"
		assert classify_temp(54.9) == "NORMAL"

	def test_warm_temp(self):
		assert classify_temp(55.0) == "WARM"
		assert classify_temp(65.0) == "WARM"
		assert classify_temp(69.9) == "WARM"

	def test_hot_temp(self):
		assert classify_temp(70.0) == "HOT"
		assert classify_temp(75.0) == "HOT"
		assert classify_temp(79.9) == "HOT"

	def test_critical_temp(self):
		assert classify_temp(80.0) == "CRITICAL"
		assert classify_temp(85.0) == "CRITICAL"


	def test_boundary_conditions(self):
		assert classify_temp(54.99) == "NORMAL"
		assert classify_temp(55.00) == "WARM"
		assert classify_temp(69.99) == "WARM"
		assert classify_temp(70.00) == "HOT"

	def test_invalid_temp(self):
		with pytest.raises(ValueError):
			classify_temp(-10.0)

#Test temp unit conversions
class TestTemperatureConversion:

	def test_celsius_to_fahrenheit(self):
		assert celsius_to_fahrenheit(0) == 32
		assert celsius_to_fahrenheit(100) == 212
		assert celsius_to_fahrenheit(37) == pytest.approx(98.6, rel=0.1)

	def test_freezing_point(self):
		assert celsius_to_fahrenheit(0) == 32

	def test_boiling_point(self):
		assert celsius_to_fahrenheit(100) == 212

#Test temp file reading
class TestReadTemperature:

	def test_read_real_temp(self)"
		try:
			temp = read_cpu_temp_c()
			assert 20 < temp < 100
		except TemperatureError:
			pytest.skip("Not running on Raspberry Pi")

	def test_invalid_path(self):
		with pytest.raises(TemperatureError):
			read_cpu_temp_c("/nonexistent/path")
