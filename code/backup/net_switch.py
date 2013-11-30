# net_switch.py  (c) 2013 @whaleygeek
#
# A network switch server - showing a remotely polled switch
#
# Any message from the client causes this server to send the 
# present status of the switch

import RPi.GPIO as GPIO
import time
import network

SWITCH = 10
GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH, GPIO.IN)

def heard(phrase):
  if (GPIO.input(SWITCH)):
    network.say("1")
  else:
    network.say("0")

while True:
  network.wait(whenHearCall=heard)
  while network.isConnected():
    time.sleep(1)
    
