from smbus2 import SMBus
from mlx90614 import MLX90614
import time
from time import sleep
while True:
    
        bus = SMBus(1)
        sensor = MLX90614(bus, address=0x5A)
        print ("Tempreture is :",sensor.get_obj_temp())
        print(type(sensor.get_obj_temp()))
        bus.close()
        sleep(1)
        
                   
        
