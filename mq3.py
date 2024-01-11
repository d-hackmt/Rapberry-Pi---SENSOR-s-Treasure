import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # This command is to Disable Warning....!!!!

MQ_3 = 19
buzzer = 25
GPIO.setup(19, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)
while True:
    j=GPIO.input(MQ_3)
    print(j)
    if j==0 :
        print('Smoke Detected!')
        time.sleep(1)
        GPIO.output(buzzer, False)
        time.sleep(1)
       
       
    else :
        print ('Smoke Not Detected!')
        time.sleep(1)
        GPIO.output(buzzer, True)
