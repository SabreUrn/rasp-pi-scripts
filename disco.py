import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

try:
	while True:
		GPIO.output(14, GPIO.HIGH)
		GPIO.output(15, GPIO.LOW)
		GPIO.output(18, GPIO.LOW)
		time.sleep(1)
		GPIO.output(14, GPIO.LOW)
		GPIO.output(15, GPIO.HIGH)
		GPIO.output(18, GPIO.LOW)
		time.sleep(1)
		GPIO.output(14, GPIO.LOW)
		GPIO.output(15, GPIO.LOW)
		GPIO.output(18, GPIO.HIGH)
		time.sleep(1)
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
