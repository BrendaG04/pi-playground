import time
from temperature import read_cpu_temp_c, classify_temp

from gpiozero import LED

green = LED(27)
yellow = LED(24)
red = LED(17)

def all_off():
	green.off()
	red.off()
	yellow.off()

def show_state(state: str):
	all_off()

	if state == "NORMAL":
		green.on()
	elif state == "WARM":
		yellow.on()
	elif state == "HOT":
		red.on()

def run_test_step(step: int) -> str:
	all_off()
	if step % 3 == 0:
		green.on()
		return "TEST_GREEN"
	elif step % 3 == 1:
		yellow.on()
		return "TEST_YELLOW"
	else:
		red.on()
		return "TEST_RED"

def main():
	try:
		while True:
			temp_c = read_cpu_temp_c()
			state = classify_temp(temp_c)
			show_state(state)
			print(f"temp={temp_c:.2f}C state={state}")
			time.sleep(2)
	except KeyboardInterrupt:
		all_off()
		print("\nStopped.")

if __name__ == "__main__":
	main()

