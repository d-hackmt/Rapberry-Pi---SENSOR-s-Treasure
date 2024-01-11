import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode(GPIO.BCM)
Soil = 21

GPIO.setup(Soil, GPIO.IN)
GPIO.setwarnings(False) 

    
while True:
  got_something = GPIO.input(Soil)
  print(got_something)
  if got_something:
    print("Moisture Low")
   
    time.sleep(0.2)
   
  else:
    print("Moisture High")
    setup()
    loop()
    time.sleep(0.2)
