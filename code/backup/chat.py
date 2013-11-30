# chat.py  (c) 2013 @whaleygeek
#
# A simple internet-chat application

import network
import sys

def heard(phrase):
  print("them:" + phrase)

if (len(sys.argv) >= 2):
  network.call(sys.argv[1], whenHearCall=heard)
else:  
  network.wait(whenHearCall=heard)

while network.isConnected():
  #phrase = raw_input() #python2
  phrase = input() # python3
  print("me:" + phrase)
  network.say(phrase)
  