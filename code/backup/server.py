# server.py  (c) 2013 @whaleygeek
#
# A simple server that just prints anything it receives

import network
import time

def heard(phrase):
  print(phrase)
  
network.wait(whenHearCall=heard)
print("connected")

while network.isConnected():
  print("waiting")
  time.sleep(4)
  
print("disconnected")
