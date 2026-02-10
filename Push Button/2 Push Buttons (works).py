from machine import Pin
from time import sleep

B1 = Pin(21,Pin.IN,Pin.PULL_UP)
B2 = Pin(18,Pin.IN,Pin.PULL_UP)

while True:
    x = B1.value()
    y = B2.value()
    
    if x==0 and y==1:
        print("Button 1 Pressed")
    
    if x==1 and y==0:
        print("Button 2 Pressed")
    
    if x==0 and y==0:
        print ("Both Buttons Pressed")
        
    sleep(0.2)