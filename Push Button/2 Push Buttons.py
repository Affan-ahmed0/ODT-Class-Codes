from machine import Pin
from time import sleep
#importing necessary modules

#power input for the buttons
B1 = Pin(21,Pin.IN,Pin.PULL_UP)
B2 = Pin(18,Pin.IN,Pin.PULL_UP)
#power output of the buttons
x = B1.value()
y = B2.value()
#reading the value offrom the output of the buttons pressed
while True: #always looping
    if x == 0: #B1 is on
        print("Button 1 Pressed")

    if y == 0: #B2 is on
        print("Button 2 Pressed")
    
    if x==0 and y==0: #Both B1 and B2 pressed
        print("Both Buttons Pressed")
    sleep(0.2) #runs the code every 2 milliseconds
