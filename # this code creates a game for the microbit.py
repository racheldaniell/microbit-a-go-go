# this code creates a game for the microbit
# the game displays random numbers and asks user if they are odd or even
# the game gives feedback on accuracy of user response

# import items needed first
from microbit import *
import random

# game instructions are displayed first to user
display.scroll("game time!")
display.scroll("when I show you a # - press button A if odd OR B if even")
display.scroll(" - OR to end UNPLUG")
sleep(1000)

# then loop of game begins
while True:
    # this variable sets up a blinking happy face animation for use later when user correct
    success = [Image.HAPPY, Image.SURPRISED, Image.HAPPY]
    # the random number generator is set to generate numbers
    # only numbers of 2 characters will be used so user can see them easily
    num = random.randint(1, 9)
    numtype = ""
    display.show(num)
    if num % 2 == 0:
        numtype = "even"
    else:
        numtype = "odd"
    sleep(2000)
    # if/elif statements evaluate correctness of user input and display feedback
    if button_a.was_pressed() and (numtype == "odd"):
        display.show(success, delay=200)
    elif button_b.was_pressed() and (numtype == "even"):
        display.show(success, delay=200)
    elif button_a.get_presses() == 0 and button_b.get_presses() == 0:
        # this display gives feedback to user if they did not press anything
        display.scroll("hi?")
    else:
        # a sad face is displayed when user gets it wrong...
        display.show(Image.SAD)
    # get_presses at end ensure button press logs are cleared regardless of previous input
    button_a.get_presses()
    button_b.get_presses()
    sleep(1000)




