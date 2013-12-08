#Version 1.2    James Dent, Frank Everest, David Whale, 8th December 2013
#This program is adapted from James Dent's tkinter flashcards.

from tkinter import *
import math

def calcHypotenuse(*ignore):
    a = value_a.get()   #store value from input
    b = value_b.get()   #store value from input
    asquared = float(a) * float(a)
    bsquared = float(b) * float(b)
    csquared = asquared + bsquared
    c = math.sqrt(csquared)
    #Send the result to the screen:
    txt = Label(app, text="Hypotenuse is " + str(c))
    txt.grid(row=8, sticky=W)

root = Tk()
root.resizable(0,0)         #stop window from being resizedroot = Tk()
app = Frame(root)	    #create a frame
app.grid()		    #use a grid to layout the frame
root.title("Pythagoras")    #Graphical User Interface (GUI) title.
root.geometry("400x600")    #set GUI size

# create a Label and import the picture 
picture = Label(app)
picture.grid(row=0, columnspan=3, sticky=W)

# 'sticky = W' means left aligned (West)
pythagoras = PhotoImage(file="pythagoras.gif")

#needs to be in same directory
picture["image"] = pythagoras


#create a label and display text on four lines:
lbl = Label(app, text="this will calculate the length")
lbl.grid(row=1, columnspan=3, sticky=W)
lbl = Label(app, text="of the hypotenuse (c)")
lbl.grid(row=2, columnspan=3, sticky=W)
lbl = Label(app, text="for a right-angled triangle")
lbl.grid(row=3, columnspan=3, sticky=W)
lbl = Label(app, text="with sides (a) and (b).")
lbl.grid(row=4, columnspan=3, sticky=W)

#create an on-screen button for the side a:
lbl = Label(app, text="Enter length of side a:")
lbl.grid(row=5, columnspan=3, sticky=W)
#get the value typed in:
value_a = Entry(app, width=10)
value_a.grid(row=5, column=10, sticky=W)

#create an on-screen button for the side b:
lbl = Label(app, text="Enter length of side b:")
lbl.grid(row=6, columnspan=3, sticky=W)
#get the value typed in:
value_b = Entry(app, width=10)
value_b.grid(row=6, column=10, sticky=W)

def ledON():
  GPIO.output(LED, False) # on, see card 12

def ledOFF():
  GPIO.output(LED, True) # off, see card 12

onBtn = Button(app, text='turn it on', command=ledON)
onBtn.grid(row=8, column=1, sticky=W)
offBtn = Button(app, text='turn it off', command=ledOFF)
offBtn.grid(row=8, column=2, sticky=W)

calc = Button(app, text="Calculate!", command=calcHypotenuse)
calc.grid(row=7, column=1, sticky=W)
root.mainloop()
