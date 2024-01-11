import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # This command is to Disable Warning....!!!!

GPIO.setup(21, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
while True:
        GPIO.output(21, True)
        GPIO.output(26, True)
        time.sleep(3)
        GPIO.output(21, False)
        GPIO.output(26, False)
        time.sleep(1)
