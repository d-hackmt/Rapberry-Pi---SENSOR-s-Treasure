from subprocess import call
import speech_recognition as sr
import serial
import RPi.GPIO as GPIO
r = sr.Recognizer()
print("Please talk...")
with sr.Microphone() as source:
    #read the audio data from the default microphone
    audio_data = r.record(source, duration=10)
    print("Recognizing...")
    #os.save("v.mp3")
    # convert speech to text
    data = r.recognize_google(audio_data)
    print("Recognised Speech:"+data)
        
"""
Note:-follow the link so that you can setting your USB

https://www.youtube.com/watch?v=aN5NgqCw_i4


file name:-Webcam as Microphone.txt
#Edit alsa config file as shown
sudo nano /usr/share/alsa/alsa.conf 

defaults.ctl.card 1
defaults.pcm.card 1
defaults.pcm.device 0
defaults.pcm.subdevice 0

#These card values are for USB Mic and Rpi's 3.5mm jack audio out.
sudo nano ~/.asoundrc 

pcm.!default {
         type asym
         playback.pcm {
                 type plug
                 slave.pcm "hw:1,0"
         }
         capture.pcm {
                 type plug
                 slave.pcm "hw:1,0"
         } 
 }

 ctl.!default {
        type hw
        card 1
}

#Copy paste the above settings in asound.conf as well
sudo nano /etc/asound.conf

Library Installation:
1. sudo apt-get update 
2. sudo apt-get upgrade 
3. sudo apt-get install portaudio19-dev 
4. sudo pip install pyaudio

sudo apt-get install espeak
sudo pip3 install SpeechRecognition
sudo pip3 install PyAudio
apt-get install flac



"""
