from gpiozero import LED
import time

led = LED(17)

for _ in range(30):
    led.on()
    time.sleep(0.2)
    led.off()
    time.sleep(0.2)
    
led.off()
    
    
