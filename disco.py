import RPi.GPIO as GPIO
import time

def LightOne():
	GPIO.output(14, GPIO.HIGH)
	GPIO.output(15, GPIO.LOW)
	GPIO.output(18, GPIO.LOW)

def LightTwo():
	GPIO.output(14, GPIO.LOW)
	GPIO.output(15, GPIO.HIGH)
	GPIO.output(18, GPIO.LOW)


def LightThree():
	GPIO.output(14, GPIO.LOW)
	GPIO.output(15, GPIO.LOW)
	GPIO.output(18, GPIO.HIGH)

GPIO.setmode(GPIO.BCM)
GPIO.setup([14, 15, 18, 23, 24, 25], GPIO.OUT)
GPIO.output([23, 24, 25], GPIO.LOW)

x = 1.0

try:
	while x > 0:
		LightOne()
		time.sleep(x)
		LightTwo()
		time.sleep(x)
		LightThree()
		time.sleep(x)
		x -= 0.5
	x = 1.0
	while x < 5:
		LightOne()
		time.sleep(x)
		LightTwo()
		time.sleep(x)
		LightThree()
		time.sleep(x)
		x += 1.0
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
