import time,os
from time import sleep
import glob
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/28*'
#device_folder = glob.glob('/sys/bus/w1/devices/28*')[0]
device_file = base_dir + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f
while True:
        temp_c,temp_f = read_temp()
        print( "Temp: ",temp_c)


#https://iot4beginners.com/temperature-sensor-with-raspberry-pi-ds18b20/
