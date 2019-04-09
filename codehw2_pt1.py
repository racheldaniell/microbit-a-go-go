# CODING HW 2 - python code part 1 (microbit/input)
# This code sets up a structure for reactions to touch input on the Microbit
# this takes the triggering from Microbit to push results in Raspberry Pi via writing to pins
# this is a draft stage toward the final needed for project which is a user interaction touch resulting in a changed display
# note that in the full project, the touch area will be with a secondary material rather than direct
# expected material is specialized tape or specialized paint

# first import microbit code library

from microbit import *


# store redacted text title preview in variables

mb_redact1 = "Cramped Confinement"
mb_redact2 = "The Waterboard Technique"

# create while loop that will react when pins touched
# first reaction is to display the short title of the redacted text
# next reaction is to write to pins which will each transmit to the connected Rasp Pi

while True:
    if pin0.is_touched():
        display.scroll(mb_redact1)
        sleep(500)
        pin0.write_digital(1)
        sleep(5000)
        pin0.write_digital(0)
    if pin1.is_touched():
        display.scroll(mb_redact2)
        sleep(500)
        pin1.write_digital(1)
        sleep(5000)
        pin1.write_digital(0)

# notes during development:
# the pin touches were tested both with alligator clips and finger touch with success
