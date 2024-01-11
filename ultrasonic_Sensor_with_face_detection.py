# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 18:16:46 2021

@author: srcdo
"""

#Libraries
import RPi.GPIO as GPIO
import time
import tkinter as tk
from tkinter import * 
from tkinter import ttk, LEFT, END
import time
import numpy as np
import cv2
import os
from PIL import Image , ImageTk     
from PIL import Image
import requests
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 24
GPIO_ECHO = 23
buzzer = 13 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.output(buzzer, False)


################################Things Speak################################
import urlopen
import urllib
# Enter Your API key here
User1API = '2SG86G1Q6J1J9TSA'
# URL where we will send the data, Don't change it
baseURL1 = 'https://api.thingspeak.com/update?api_key=%s' % User1API

################Location#################################################
import json
location_req_url='http://api.ipstack.com/103.51.95.183?access_key=fcdaeccb61637a12fdf64626569efab0'
r = requests.get(location_req_url)
location_obj = json.loads(r.text)
        
lat = location_obj['latitude']
lon = location_obj['longitude']
latitude = lat
longitude = lon
print(str(latitude))
print(str(longitude))
msg ="May be terrorist detected...Here I attached object:Latitude is:"+str(latitude)+"Langitude is:"+str(longitude)

########################Ultrasonic Sensor###############################
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

#############################Send SMS########################################
def sms_send():
    url="https://www.fast2sms.com/dev/bulk"
    params={
  
        "authorization":"ex2cWMEQjKBZbXmk4qtNCOHighwzp5uT38Un0rsoJDGR1PlIAyuHqjseXzLTO58p6yNEf0bit2kIPgBR",
        "sender_id":"SMSINI",
        "message":msg,
        "language":"english",
        "route":"p",
        "numbers":"9607181257"
    }
    rs=requests.get(url,params=params)


##########################Faec Authentication################################
def Test_database():
    global id
    flag=0
    recognizer = cv2.face.LBPHFaceRecognizer_create(1, 8, 8, 8, 100)
#    recognizer = cv2.face.FisherFaceRecognizer(0, 3000);
    
    recognizer.read('trainingdata.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    font = cv2.FONT_HERSHEY_SIMPLEX
    #iniciate id counter
    id = 0
    # names related to ids: example ==> Marcelo: id=1,  etc
    names = ['None', 'Mrunalini', 'Aniruddha', 'Vinod Sir'] 
    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height
    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    while True:
        ret, img =cam.read()
#       img = cv2.flip(img, -1) # Flip vertically
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray,1.3,8,minSize = (int(minW), int(minH)))

        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            
            # If confidence is less them 100 ==> "0" : perfect match
            
            if (confidence < 60):
               
                id = id
                name = names[id]
                confidence = "  {0}%".format(round(100 - confidence))      
                cv2.putText(img,str(name),(x+5,y-5),font,1,(255,255,255),2)
                cv2.putText(img,str(confidence),(x+5,y+h-5),font,1,(255,255,0),1)
                cam.release()
                cv2.destroyAllWindows()
                while True:
                    dist = distance()
                    print ("Measured Distance = %.1f cm" % dist)
                    conn = baseURL1 + '&field3=%s' % (dist)
                    request = urllib.request.Request(conn)
                    responce = urllib.request.urlopen(request)
                    responce.close()
                    if dist < 30:
                        print("object detected")
                        Test_database()
                
               
            else:
                id = "unknown Person Identified..it may be terrorist"
                confidence = "  {0}%".format(round(100 - confidence))
                cv2.putText(img,str(id),(x+5,y-5),font,1,(255,255,255),2)
                cv2.putText(img,str(confidence),(x+5,y+h-5),font,1,(255,255,0),1)  
                GPIO.output(buzzer, True)
                time.sleep(1)
                GPIO.output(buzzer, False)
                sms_send()
                cam.release()
                cv2.destroyAllWindows()
                while True:
                    dist = distance()
                    print ("Measured Distance = %.1f cm" % dist)
                    conn = baseURL1 + '&field3=%s' % (dist)
                    request = urllib.request.Request(conn)
                    responce = urllib.request.urlopen(request)
                    responce.close()
                    if dist < 30:
                        print("object detected")
                        Test_database()
                
                
        

#        time.sleep(0.2)
        cv2.imshow('camera',img)
        
#        print(flag)
        if flag==10:
            flag=0
            cam.release()
            cv2.destroyAllWindows()
           

        if cv2.waitKey(1) == ord('Q'):
            break

        
def ultrasonic():
    
    dist = distance()
    print ("Measured Distance = %.1f cm" % dist)
    conn = baseURL1 + '&field3=%s' % (dist)
    request = urllib.request.Request(conn)
    responce = urllib.request.urlopen(request)
    responce.close()
    if dist < 30:
        print("object detected")
        Test_database()

        
###############################Main Call################################ 
if __name__ == '__main__':
    try:
        while True:
            ultrasonic()
                
            
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
