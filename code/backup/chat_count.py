# A simple internet chat client and server. (c) 2013 @whaleygeek

import network
import sys

them = 1
me = 1

def heard(phrase):
  global them
  print("them:" + str(them) + phrase)
  them = them + 1

if (len(sys.argv) >= 2):
  network.call(sys.argv[1], whenHearCall=heard)
else:  
  network.wait(whenHearCall=heard)

while network.isConnected():
  #phrase = raw_input() #python2
  phrase = input() # python3
  print("me:" + str(me) + phrase)
  me = me + 1
  network.say(phrase)
  