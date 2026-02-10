from machine import Pin
import time

Button1 = Pin(3,Pin.IN,Pin.PULL_UP) #Pull up refers to the pull up resistor that is in the board, saying Pin.PULL_UP means that
Button2 = Pin(19,Pin.IN,Pin.PULL_UP)
Green = Pin(4,Pin.OUT)
Blue = Pin(21,Pin.OUT)

while True:
    time.sleep(0.01)
    if Button1.value() == 0:
       print ("Works")
       Green.on()
       Blue.off()
       time.sleep(0.2)
    else :
        print ("Nope")
        Blue.on()
        Green.off()
        time.sleep(0.2)
    
    