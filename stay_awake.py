from threading import Thread,Event
import easygui
import time

delay = 10

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
            print "\a"
            time.sleep(0.2)
            i += 1
            
    def stop(self):
        self._stop.set()



while not done:
    beeper = Beeper()

    #make a default one which can get accidentally pressed without making the dialog go away.
    choices = [ ":-)", "^", "v", "exit" ]
    choice = ":-)"
    beeper.start()
    while choice == ":-)":
        choice = easygui.buttonbox( str(delay) + " status?", choices=choices )
    beeper.stop()

    if choice == "^":
        delay /= .8
    elif choice == "v":
        delay *= .8
    else:
        done = True

    if not done: time.sleep( delay )
