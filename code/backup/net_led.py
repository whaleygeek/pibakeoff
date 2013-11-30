# net_led.py  (c) 2013 @whaleygeek
#
# A network LED client - showing a LED that reflects remote switch status
#
# Connects to, and polls, a switch server once per second,
# and updates the LED status to reflect that of the switch.

import RPi.GPIO as GPIO
import time
import sys
import network

SERVER_IP = sys.argv[1]
LED = 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

def heard(phrase):
  a = phrase[0]
  if a == "0":
    GPIO.output(LED, False)
  else:
    GPIO.output(LED, True)

network.call(SERVER_IP, whenHearCall=heard)
while network.isConnected():
  network.say("?")
  time.sleep(1)    


