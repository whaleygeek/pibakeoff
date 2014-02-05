# A simple internet chat client and server. (c) 2013 @whaleygeek

import network
import sys
import random

def heard(phrase):
  print("them:" + phrase)

def getRandom():
  p = random.choice([
    "Tell me about your mother?", 
    "What is your name?",
    "Do you want to play a game?",
    "What colour are your eyes?"
  ])
  return p

if (len(sys.argv) >= 2):
  network.call(sys.argv[1], whenHearCall=heard)
else:  
  network.wait(whenHearCall=heard)

while network.isConnected():
  #phrase = raw_input() #python2
  phrase = input() # python3
  if phrase == "random":
    phrase = getRandom()
    
  print("me:" + phrase)
  network.say(phrase)
  