#Version 1.0: James Dalley
#December 2013

#Input high, output low program
# If connector pin7 (signal name GPIO4) goes high,
# connector pin26 (signal name GPIO7) goes low.
#
# The code runs but is not "good" code.
# Run it and look at the error warnings.
# Then look at the end of the ServoOutput.py code
# How can you modify this short code to be good!


# import library
import RPi.GPIO as GPIO

# set up pin/signal name inputs & outputs
GPIO.setmode(GPIO.BCM) # use BCM signalnames
GPIO.setup(7,GPIO.OUT) # conn pin26 is output
GPIO.setup(4,GPIO.IN)  # conn pin7 is input

while True:
	if GPIO.input(4)==True:  # pin7:input=hi 
		GPIO.output(7,False)# pin26:lo

	if GPIO.input(4)==False: # pin7:input=lo
		GPIO.output(7,True) # pin26:high
