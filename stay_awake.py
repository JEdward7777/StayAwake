#!/usr/bin/env python3
from threading import Thread,Event
import easygui
import time
import random
import sys

delay = 10
history = ""

done = False


class Beeper(Thread):
    def __init__(self):
        Thread.__init__(self)
        self._stop = Event()

    def run(self):
        self._stop.clear()
        time.sleep(3)
        i = 0
        while not self._stop.is_set() and i < 20:
            print( "\a" )
            time.sleep(0.2)
            i += 1
            
    def stop(self):
        self._stop.set()

message = " ".join( sys.argv[1:] )
flipped = False

if message.strip() == "ask":
    message = easygui.enterbox( "Message?" )
    flipped = easygui.ynbox( "Flip polarity?" )

while not done:
    beeper = Beeper()

    #make a default one which can get accidentally pressed without making the dialog go away.
    choices = [ ":-)", "^", "v", "exit" ]
    choice = ":-)"
    beeper.start()
    while choice == ":-)":
        choice = easygui.buttonbox( str(delay) + " status? " + message+ " \n" + history, choices=choices )
    beeper.stop()

    if choice == "^":
        if not flipped:
            delay /= .8
        else:
            delay *= .8
        history += "^"
    elif choice == "v":
        if not flipped:
            delay *= .8
        else:
            delay /= .8
        history += "v"
    else:
        done = True

    #add some random difference to the delay so that
    #if there are multiple delays running they don't all pile up on eachother.
    delay *= (random.random()*(1.1-.9)+.9)

    if not done: time.sleep( delay )
