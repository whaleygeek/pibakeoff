# client.py  (c) 2013 @whaleygeek
#
# A demo client that pokes "hello" at a server once per second

import network
import time

network.call("localhost")

while network.isConnected():
  print("sending")
  network.say("hello")
  time.sleep(1)
  
