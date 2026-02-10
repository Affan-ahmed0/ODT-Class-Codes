from machine import Pin
from time import sleep

B1 = Pin(21,Pin.IN,Pin.PULL_UP)
B2 = Pin(18,Pin.IN,Pin.PULL_UP)

while True:
    x = B1.value()
    y = B2.value()
    
        
    if x==0 and y==0:
        print ("Both Buttons Pressed")
        
    elif x==0:
        print("Button 1 Pressed") #elif statement runs if the previous statements aren't true
    
    elif y==0:
        print("Button 2 Pressed")
        
    sleep(0.2)
