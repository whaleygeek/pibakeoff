# A simple proxy  (c) 2013 @whaleygeek
#
# Starts a server on a nominated local port
# when an incoming connection arrives, it is accepted
# then an outgoing client connection is made to the remote host/port
# all data is forwarded in both directions

import network
import sys
import time

def trace(msg):
  print("proxy:" + msg)

  
class Proxy():
  def __init__(self, localPort, remoteServer, remotePort):
    self.localPort    = localPort
    self.remoteServer = remoteServer
    self.remotePort   = remotePort
 
  def localIncoming(self, msg):
    print("local:" + msg)
    self.remote.say(msg)
    
    
  def remoteIncoming(self, msg):
    print("remote:" + msg)
    self.local.say(msg)
    
    
  def run(self):
    #trace("waiting")
    self.wait()

    #trace("looping") 
    while (self.local != None and self.remote != None):
      #YUK busy wait
      time.sleep(1)
      
    #trace("finishing")
    self.close()
    
    #trace("finished")
      
      
  def wait(self):
    self.local  = network.Connection()
    self.remote = network.Connection()
    
    self.local.whenHungUp(self.close)
    self.remote.whenHungUp(self.close)
    
    #trace("Waiting for incoming local connection")
    self.local.wait(whenHearCall=self.localIncoming, port=self.localPort)
    #trace("local connection connected")

    #trace("connecting to remote")
    self.remote.call(remoteServer, whenHearCall=self.remoteIncoming, port=self.remotePort)
    #trace("remote connection connected")
      
      
  def close(self):
    #trace("closing")
    
    #trace("hangup remote")
    r = self.remote
    if (r != None):
      self.remote = None
      r.hangUp()
    
    #trace("hangup local")
    l = self.local
    if (l != None):
      self.local = None
      l.hangUp()
    
  
# Main entry point  

if (len(sys.argv) < 4):
  print("usage: proxy <localPort> <remoteServer> <remotePort>")
else:
  localPort    = int(sys.argv[1])
  remoteServer = sys.argv[2]
  remotePort   = int(sys.argv[3])
  
  proxy = Proxy(localPort, remoteServer, remotePort)
  proxy.run()
    


    


  
  
  