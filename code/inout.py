#import libraries
import RPi.GPIO as GPIO
import time

# set up pin/signal name IO
GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(2,GPIO.IN)
GPIO.setup(4,GPIO.IN)

try:
        while True:
                if GPIO.input(4)==True:
                        GPIO.output(7,False)
                        GPIO.output(8,True)

                if GPIO.input(4)==False:
                        GPIO.output(7,True)
                        GPIO.output(8,False)

                if GPIO.input(2)==True:
                        GPIO.output(25,True)
                        time.sleep(0.25) 
                        GPIO.output(25,False)
                        time.sleep(0.25)

except:
        GPIO.cleanup()

