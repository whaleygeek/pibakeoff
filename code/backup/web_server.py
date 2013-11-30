# web_server.py  (c) 2013 @whaleygeek
#
# A very simple single-threaded web server.

import network
import time

port  = 80
state = 0

def handleRequest(line):
  print("request:" + line)

def handleHeader(line):
  print("header:" + line)

def handleBody(line):
  global network
  network.say("HTTP/1.0 200 OK") # response
  network.say("") # end of response headers(none)
  network.say("<html><body><H1>Hello Web Server</H1></body></html>")
  
def heard(line):
  global state
  global network
  
  if (state == 0): # GET / HTTP/1.0
    handleRequest(line)
    state = 1
    
  elif (state == 1): # headers
    if (len(line.strip()) == 0): # blank separator
      state = 2
    else:
      handleHeader(line)
      
  elif (state == 2): # body
    # This is a GET so just send the body
    handleBody(line)
    network.hangUp() # done
    

# main program starts here

while True:  
  network.wait(port=port, whenHearCall=heard)
  print("connected")

  while network.isConnected():
    # Nothing else to do, but could run other code here
    time.sleep(1)

  print("disconnected")





