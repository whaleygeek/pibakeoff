# A simple internet chat client and server. (c) 2013 @whaleygeek

import network
import sys

def heard(phrase):
  print("them:" + phrase)

print("MyChat internet chat program")

if (len(sys.argv) >= 2):
  network.call(sys.argv[1], whenHearCall=heard)
else:  
  network.wait(whenHearCall=heard)

print("Connected!")
network.say("Welcome to MyChat - please be nice!")

while network.isConnected():
  #phrase = raw_input() #python2
  phrase = input() # python3
  print("me:" + phrase)
  network.say(phrase)
  