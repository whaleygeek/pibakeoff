# A simple internet chat client and server. (c) 2013 @whaleygeek

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
  
  if phrase == "W":
    phrase = "Welcome to MyChat, please be friendly"
  elif phrase == "B":
    phrase = "I have to go now, thanks for chatting"
  elif phrase == "Q":
    phrase = "Tell me something I don't know about"
  print("me:" + phrase)
  network.say(phrase)
  