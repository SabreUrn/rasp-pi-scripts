import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

GPIO.output(14, GPIO.LOW)
GPIO.output(15, GPIO.HIGH)
GPIO.output(18, GPIO.HIGH)

input("Press enter to continue.")
GPIO.cleanup()