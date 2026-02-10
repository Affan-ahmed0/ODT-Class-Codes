from machine import Pin
import time

Button1 = Pin(3,Pin.IN,Pin.PULL_UP) #Pull up refers to the pull up resistor that is in the board, saying Pin.PULL_UP means that
Button2 = Pin(19,Pin.IN,Pin.PULL_UP)
Green = Pin(4,Pin.OUT)
Blue = Pin(21,Pin.OUT)
Yellow = Pin(18,Pin.OUT)

print(Button1.value() + Button2.value())
while True:
    time.sleep(0.01)
    if Button1.value()==0:
        Green.on()
        Blue.off()
        Yellow.off()
        print ("green")
        time.sleep(0.01)
        Green.off()
    if Button2.value()==0:
        Blue.on()
        Green.off()
        Yellow.off()
        print ("blue")
        time.sleep(0.01)
        Blue.off()
    if Button1.value() + Button2.value()==0:
        Yellow.on()
        print ("none")
        time.sleep(0.01)
        Yellow.off()

