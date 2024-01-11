

import RPi.GPIO as GPIO
import time

sensor = 21
buzzer = 26
global count
count = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.output(buzzer,False)
#oled
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess
RST = 0
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image1 = Image.new('1', (width, height))
draw = ImageDraw.Draw(image1)
padding = -2
top = padding
bottom = height-padding
x = 0
font = ImageFont.load_default()

print("***********Rain Sensor Ready.....***********")
print(" ")

while True:
         print("---------------------------------")
         i = GPIO.input(sensor)
         print(i)
         disp.clear()
         disp.display()
         image = draw.text((x, top+16),"Rain Sensor:"+str(i) ,  font=font, fill=255)
         disp.image(image1)
         disp.display()
         disp.clear()
         time.sleep(1)
         if i==0:
            print("Rain Detected")
            GPIO.output(buzzer,True)
            time.sleep(1)
            GPIO.output(buzzer,False)
         else:
            print("Rain not Detected")
            
        

