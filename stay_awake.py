import easygui
import time

delay = 10

done = False

while not done:
    time.sleep( delay )

    #make a default one which can get accidentally pressed without making the dialog go away.
    choices = [ ":-)", "^", "v", "exit" ]
    choice = ":-)"
    while choice == ":-)":
        choice = easygui.buttonbox( str(delay) + " status?", choices=choices )

    if choice == "^":
        delay /= .8
    elif choice == "v":
        delay *= .8
    else:
        done = True

