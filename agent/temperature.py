THERMAL_PATH = "/sys/class/thermal/thermal_zone0/temp"

def read_cpu_temp_c(path: str = THERMAL_PATH) -> float:
	with open(path, "r") as f:
		raw = f.read().strip()
	return int(raw)/1000.0

def classify_temp(temp_c: float) -> str:
	if temp_c < 55:
		return "NORMAL"
	if temp_c <= 70:
		return "WARM"
	return "HOT"

