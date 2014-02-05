# A simple internet chat client and server. (c) 2013 @whaleygeek

import network
import sys

def heard(phrase):
  print("them:" + phrase)
  if phrase == "hello":
    network.say("hello, how are you today?")
  elif phrase == "bye":
    network.say("Are you going already?")
  elif phrase == "help":
    network.say("What can I do to help?")
  elif phrase == "advice":
    network.say("Never wear cufflinks with short sleeved shirts")

if (len(sys.argv) >= 2):
  network.call(sys.argv[1], whenHearCall=heard)
else:  
  network.wait(whenHearCall=heard)

while network.isConnected():
  #phrase = raw_input() #python2
  phrase = input() # python3
  print("me:" + phrase)
  network.say(phrase)
  