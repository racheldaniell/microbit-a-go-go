# CODE HW 2 - PART 2 - Raspberry Pi reactions
# this code file generates the reaction of the Rasp Pi to the Microbit pin value msg
# for full project, reaction will be that Rasp Pi writes to multiple e-ink papers or displays
# the text is portions of redacted, later released, government documents

# first import what you need to run the code
from gpiozero import DigitalInputDevice
from time import sleep

# define your variables  
# 2 variables to reference Rasp Pi pins
# 2 varialbes for holding the redacted text from OIG investigation into torture techniques later released

pin0 = DigitalInputDevice(17)
pin1 = DigitalInputDevice(27)

pi_redact1 = "In cramped confinement, the detainee is placed in a confined space, typically a small or large box, which is usually dark. Confinement in the smaller space lasts no more than two hours and in the larger space it can last up to 18 hours."
pi_redact2 = "The application of the waterboard technique involves binding the detainee to a bench with his feet elevated above his head. The detainee's head is immobilized and an interrogator places a cloth over the detainee's mouth and nose while pouring water onto the cloth in a controlled manner. Airflow is restricted for 20 to 40 seconds and the technique produces the sensation of drowning and suffocation."

# project development note: 
# alternately, the redacted text portions could be stored and displayed as image files

# code below structures how Rasp Pi reacts to input from Microbit
# results should display the redacted text and write it on screen (for this stage of development)
# (in future stage, this will be altered to write to e-ink screen or small display)

while True:
	sleep(0.1)
	if pin0.value == 1:
		print(pi_redact1)
		# in development:
		# here the print command needs to output to the e-ink display
	if pin1.value == 1:
		print(pi_redact2)
		# in development:
		# here the print command needs to output to the e-ink display



# notes from development process:
# considering whether OS file open type process wanted, if so
# import os