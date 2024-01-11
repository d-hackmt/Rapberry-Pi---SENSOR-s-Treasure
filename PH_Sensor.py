

import Adafruit_ADS1x15
import serial
import time

rate = [0]*10
amp = 100
GAIN = 2/3  
curState = 0
stateChanged = 0

ser = serial.Serial ("/dev/ttyS0", 9600)


def send_to_prcessing1(data1):   # for PH Sensor
        ser.write(str(data1).encode())

        
def ph():
        adc = Adafruit_ADS1x15.ADS1115()
        while True:
                Signal = adc.read_adc(0, gain=GAIN)   
                Signal = (Signal*10)/float(3023)
                Signal = (round(Signal,2))
                Signal = Signal / 4.7
                Signal = (round(Signal,1))
                if Signal < 6.9:
                       Signal = 0.0 
                print("PH value:" + str(Signal))
                send_to_prcessing1(Signal)
                time.sleep(2)
        

                    
ph()

