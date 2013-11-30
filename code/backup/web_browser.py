# web_browser.py  (c) 2013 @whaleygeek
#
# A very simple web browser

import network
import time

# CONFIGURATION

host      = "localhost"
port      = 80
url       = "/index.html"
proto_ver = "HTTP/1.0"
state     = 0


def handleResponse(data):
  pass # ignore response status line
  
def handleHeader(data):
  pass # ignore header
  
def handleBody(data):
  print(data)
  
def heard(msg):  
  global state
  if (state == 0): # response
    handleResponse(msg)
    state = 1
  elif (state == 1): # headers
    if (len(msg.strip()) != 0): # not end of headers
      handleHeader(msg)
    else: # end of headers
      state = 2
  elif (state == 2): # body
    handleBody(msg)
  

# main program starts here

network.call("localhost", port=port, whenHearCall=heard)
network.say("GET " + url + " " + proto_ver)
network.say("")
network.say("")

while network.isConnected():
  time.sleep(1)


  