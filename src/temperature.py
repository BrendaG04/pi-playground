"""
	Temperature Monitoring
		-Reads CPU Temperature and classifies thermal state.
"""

THERMAL_PATH = "/sys/class/thermal/thermal_zone0/temp"

#Custom Exception for temperature reading Errors
class TemperatureError(Exception):
	pass


#Read CPU temp in Celcius
def read_cpu_temp_c(path: str = THERMAL_PATH) -> float:
	try:
		with open(path, "r") as f:
		raw = f.read().strip()
		return int(raw)/1000.0
	except FileNotFoundError:
		raise TemperatureError(f"Thermal File not Found: {path}")
	except (ValueError, IOError) as e:
		rasie TemperatureError(f"Failed to Read Temperature: {e}")

#Classifies the temp in thermal states
def classify_temp(temp_c: float) -> str:
	if temp_c < 55:
		return "NORMAL"
	elif temp_c < 70:
		return "WARM"
	elif temp_c < 80: 
		return "HOT"
	else:
		return "CRITICAL"

#Converts celcius to fahrenheit
def celcius_to_fahrenheit(temp_c : float) -> float:
	return (temp_c * 9/5) + 32

