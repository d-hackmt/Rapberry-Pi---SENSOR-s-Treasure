

import Adafruit_ADS1x15
import serial
import time

rate = [0]*10
amp = 100
GAIN = 2/3  
curState = 0
stateChanged = 0

ser = serial.Serial ("/dev/ttyS0", 9600)


def send_to_prcessing1(data1):   # for tempreture Sensor
        ser.write(str(data1).encode())



        
def tempreture():
        adc = Adafruit_ADS1x15.ADS1115()
        while True:
                Signal = adc.read_adc(0, gain=GAIN)   
                send_to_prcessing1(Signal)
                message = str(Signal / 3.5) +"C"
                print("Tempreture:" + str(Signal))
                send_to_prcessing1(message)
                time.sleep(0.5)
        

                    
tempreture()

