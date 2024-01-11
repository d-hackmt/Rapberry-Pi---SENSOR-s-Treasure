# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 12:22:16 2021

@author: srcdo
"""

import RPi.GPIO as gpio
import time
import requests
import random
import json

DT =20
SCK=21



HIGH=1
LOW=0

sample=0
val=0

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)


gpio.setup(SCK, gpio.OUT)

# Enter Your API key here
User1API = '1F2P837WKTCOUF85'
# URL where we will send the data, Don't change it
baseURL1 = 'https://api.thingspeak.com/update?api_key=%s' % User1API

def sms_send():
    url="https://www.fast2sms.com/dev/bulk"
    params={
  
        "authorization":"fvaKUPuNimZCWE8MOpB9YjLGs4nyeg6lzRqS71JXH5QFw3cktDIm3puGNrOFLP2Bq0AzjDfsWtVCTe6x",
        "sender_id":"SMSINI",
        "message":"Overload bridge",
        "language":"english",
        "route":"p",
        "numbers":"8459575041"
    }
    rs=requests.get(url,params=params)

def readCount():
  i=0
  Count=0
 # print Count
 # time.sleep(0.001)
  gpio.setup(DT, gpio.OUT)
  gpio.output(DT,1)
  gpio.output(SCK,0)
  gpio.setup(DT, gpio.IN)

  while gpio.input(DT) == 1:
      i=0
  for i in range(24):
        gpio.output(SCK,1)
        Count=Count<<1

        gpio.output(SCK,0)
        #time.sleep(0.001)
        if gpio.input(DT) == 0: 
            Count=Count+1
            #print Count
        
  gpio.output(SCK,1)
  Count=Count^0x800000
  #time.sleep(0.001)
  gpio.output(SCK,0)
  return Count  


sample= readCount()
flag=0
#lcdclear()
while 1:
  count= readCount()
  w=0
  w=(count-sample)/106
  conn = baseURL1 + '&field4=%s' % (w)
  request = urllib.request.Request(conn)
  responce = urllib.request.urlopen(request)
  responce.close()
  if w < 0:
    w=0.0
  print(w,"gm")
  if str(w) > '100':
    print("Bridge Overloaded")
    sms_send()
    
  
  time.sleep(3)

