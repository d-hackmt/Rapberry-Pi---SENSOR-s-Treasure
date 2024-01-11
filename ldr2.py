import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LDR = 16
buzzer = 20
GPIO.setup(LDR, GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)
while True:
  got_something = GPIO.input(LDR)
  print(got_something)
  if got_something:
    print("LDR OFF")
    GPIO.output(buzzer,GPIO.LOW)
    time.sleep(0.2)
   
  else:
    print("LDR ON")
    GPIO.output(buzzer,GPIO.HIGH)
    time.sleep(0.2)
