# Importing modules
import spidev # To communicate with SPI devices
from time import sleep
import datetime
# To add delay
# Start SPI connection
spi = spidev.SpiDev() # Created an object
spi.open(0,0) 

import time,os
import Adafruit_CharLCD as LCD

import sys
import urlopen
import urllib

from time import sleep
# Enter Your API key here
User1API = '1F2P837WKTCOUF85' 

# URL where we will send the data, Don't change it
baseURL1 = 'https://api.thingspeak.com/update?api_key=%s' % User1API

import RPi.GPIO as GPIO
import time

sensor = 21


GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)
# Raspberry Pi pin configuration:
lcd_rs        = 12 
lcd_en        = 16
lcd_d4        = 6
lcd_d5        = 13
lcd_d6        = 19
lcd_d7        = 26
lcd_backlight = 4



# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2


# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)
# Read MCP3008 data
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
def ir():
  A = GPIO.input(sensor)
  conn = baseURL1 + '&field3=%s' % (A)
  request = urllib.request.Request(conn)
  responce = urllib.request.urlopen(request)
  responce.close()
  if GPIO.input(sensor):
    print ("water Detected")
  else:
    print ("water not Detected")
    
###################
lcd.message('Water Contamination')
time.sleep(2) 
lcd.clear()
Vclear = 1.0
V_cal = 1.7

while True:
  PH_out = analogInput(0) # Reading from CH0
  data =  PH_out
  PH_val = (data *10) / float(1023)
  PH = round(PH_val, 2) # Round off to 2 decimal places
  PH = PH /V_cal	
  print ("PH : ",PH)
  lcd.message('PH:')
  lcd.message ("%.1f"% PH)
  TUR_out = analogInput(1) # Reading from CH0
  data =  TUR_out
  #ntu = (data - 912.5)/-0.279;
  #voltage = (data *10) / float(1023)
  voltage = data * (5.000 / 1023.000)
  turbidity = 100.00 - (voltage / Vclear) * 100.00
  #PH = round(PH_val, 2) # Round off to 2 decimal places
  lcd.write8(0xc0)
  print ("turbidity : ",turbidity)
  lcd.message('Turbidity:')
  lcd.message ("%.1f"% turbidity)
  lcd.message ("% ")
  PH1 = '%.f' % PH 					   
  TUR1= '%.f' % turbidity
  if (PH < 2 ):
    lcd.clear()
    lcd.message('Low PH Value')
    print ("Low PH value ")
    os.system ('echo "Low PH Value" | mail -s "Water Contamination" srcdocs190@gmail.com')
    time.sleep(1)
  if (PH > 11 ):
    print ("High PH value ")
    lcd.clear()
    lcd.message('High PH Value')
    os.system ('echo "High PH Value" | mail -s "Water Contamination" srcdocs190@gmail.com')
    time.sleep(2)
  if (turbidity > 50 ):
    lcd.clear()
    lcd.message('Turbidity level\n Increases')
    print ("Turbidity level Increases")
    os.system ('echo "Turbidity level Increases" | mail -s "Water Contamination" manjusha1.srccode@gmail.com')
    time.sleep(2)

  # Sending the data to thingspeak
  conn = baseURL1 + '&field1=%s&field2=%s' % (PH1, TUR1)
  request = urllib.request.Request(conn)
  responce = urllib.request.urlopen(request)
  #print conn.read()
  responce.close()
  sleep(2)
  lcd.clear()
  ir()

