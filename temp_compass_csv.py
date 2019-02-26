# this code checks sensor readings for temp and compass and creates a csv file

# start by importing the code library for microbit
from microbit import *

# have microbit take  readings on a loop every 10 secs
while True:

    # set some variables for temp and compass readings
    mbctemp = temperature()
    mbcomp = compass.heading()

    # open a .csv file and write to it
    # note that numbers need to be converted to strings for write process
    # put in the comma as concatenated text
    with open('enviro_log.csv', 'w') as my_file:
        my_file.write((str(mbctemp))+","+str(mbcomp))
    
    # display what is in your CSV for the user  
    with open('enviro_log.csv') as my_file:
        content = my_file.read()
        display.scroll("CURRENTLY: ")
        display.scroll(content)
    print(content)
    sleep(10000)


    


